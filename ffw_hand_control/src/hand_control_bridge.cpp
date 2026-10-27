// SPDX-License-Identifier: Apache-2.0
// No Python, filesystem I/O or synchronous service calls in control callbacks.
// A C++ ROS executor, not a claim of hard-real-time execution.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <memory>
#include <set>
#include <string>
#include <stdexcept>
#include <vector>
#include <unordered_map>
#include <nlohmann/json.hpp>
#include <rclcpp/rclcpp.hpp>
#include <rcl_interfaces/srv/set_parameters_atomically.hpp>
#include <sensor_msgs/msg/joint_state.hpp>
#include <std_msgs/msg/string.hpp>
#include <std_msgs/msg/u_int8.hpp>
#include <std_msgs/msg/float64_multi_array.hpp>
#include <std_srvs/srv/set_bool.hpp>
#include <trajectory_msgs/msg/joint_trajectory.hpp>
#include <urdf/model.h>
using Json=nlohmann::json;
using Trajectory=trajectory_msgs::msg::JointTrajectory;
using State=sensor_msgs::msg::JointState;
using SetConfig=rcl_interfaces::srv::SetParametersAtomically;
using SetBool=std_srvs::srv::SetBool;
using Clock=std::chrono::steady_clock;
static double seconds(){return std::chrono::duration<double>(Clock::now().time_since_epoch()).count();}
static bool finite(const std::vector<double> &v){return std::all_of(v.begin(),v.end(),[](double x){return std::isfinite(x);});}
static double normalize(double x,double low,double high){return std::clamp((x-low)/(high-low),0.0,1.0);}

class HandControl final:public rclcpp::Node {
  struct Hand {
    std::string side,letter;
    std::vector<std::string> names,arms;
    std::vector<double> opened,closed;
    double open_current=0,closed_current=0,raw_open=0,raw_closed=1;
    double trigger=0,trigger_time=0,heartbeat=0;
    bool enabled=false,held=false,saw_disabled=false,resume_allowed=false;
    bool resume_active=false;
    double resume_start=0;
    std::vector<double> resume_arms,resume_hands;
    uint8_t save_pose=0;
    rclcpp::Publisher<Trajectory>::SharedPtr arm_pub,hand_pub;
    rclcpp::Publisher<std_msgs::msg::Float64MultiArray>::SharedPtr effort_pub;
    rclcpp::Subscription<Trajectory>::SharedPtr input;
    rclcpp::Subscription<std_msgs::msg::UInt8>::SharedPtr teleop_sub,save_sub;
    rclcpp::Service<SetBool>::SharedPtr hold_service,resume_service;
  };
  std::array<Hand,2> hands_;
  std::string profile_;
  bool configured_=false,ready_=false,paused_=false,have_model_=false;
  double resume_duration_=0;
  std::unordered_map<std::string,std::pair<double,double>> measured_;
  rclcpp::Subscription<State>::SharedPtr follower_states_,arm_hand_states_;
  double trigger_min_=-.1,trigger_max_=1.1,deadband_=0;
  urdf::Model model_;
  Json last_config_;
  rclcpp::Service<SetConfig>::SharedPtr apply_;
  rclcpp::Service<SetBool>::SharedPtr pause_;
  rclcpp::Subscription<State>::SharedPtr raw_states_,virtual_sub_;
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr description_;
  rclcpp::Publisher<State>::SharedPtr virtual_pub_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr status_;
  rclcpp::TimerBase::SharedPtr timer_;
  uint64_t calls_=0;
  double total_us_=0,max_us_=0;
  bool limits_ok(const std::array<Hand,2> &hands) const {
    if(!have_model_) return false;
    for(const auto &h:hands) for(size_t i=0;i<20;++i){
      auto j=model_.getJoint(h.names[i]);
      if(!j || !j->limits) return false;
      const auto &l=*j->limits;
      if(!std::isfinite(l.lower) || !std::isfinite(l.upper) || h.opened[i]<l.lower || h.opened[i]>l.upper || h.closed[i]<l.lower || h.closed[i]>l.upper) return false;
    }
    return true;
  }
  void configure(const Json &config){
    if(config.at("schema")!=1 || config.at("profile")!=profile_) throw std::runtime_error("Wrong schema/profile");
    auto candidate=hands_;
    const double low=config.at("trigger_min"),high=config.at("trigger_max");
    const double deadband=config.at("deadband"),change=config.at("change_limit");
    if(!std::isfinite(low) || !std::isfinite(high) || low==high || !std::isfinite(deadband) || deadband<0 || deadband>=1 || !std::isfinite(change) || change<0 || change>1) throw std::runtime_error("Invalid trigger calibration");
    for(auto &h:candidate){
      const auto &v=config.at(h.side);
      auto names=v.at("names").get<std::vector<std::string>>();
      auto opened=v.at("open").get<std::vector<double>>(),closed=v.at("closed").get<std::vector<double>>();
      if(names.size()!=20 || opened.size()!=20 || closed.size()!=20 || !finite(opened) || !finite(closed)) throw std::runtime_error("Invalid hand dimensions/values");
      for(size_t i=0;i<20;++i) if(names[i]!="finger_"+h.letter+"_joint"+std::to_string(i+1)) throw std::runtime_error("Invalid hand joint order");
      h.names=names;h.opened=opened;h.closed=closed;
      h.open_current=v.at("open_current");h.closed_current=v.at("closed_current");h.raw_open=v.at("raw_open");h.raw_closed=v.at("raw_closed");
      if(!std::isfinite(h.open_current) || !std::isfinite(h.closed_current) || std::min(h.open_current,h.closed_current)<0 || std::max(h.open_current,h.closed_current)>910 || !std::isfinite(h.raw_open) || !std::isfinite(h.raw_closed) || h.raw_open==h.raw_closed) throw std::runtime_error("Invalid current/physical trigger calibration");
      if(configured_ && config.at(h.side)!=last_config_.at(h.side) && (h.trigger>change || seconds()-h.trigger_time>.5)) throw std::runtime_error("Release triggers and provide fresh input before changing presets");
    }
    if(have_model_ && !limits_ok(candidate)) throw std::runtime_error("Preset exceeds follower URDF limits");
    hands_=std::move(candidate);trigger_min_=low;trigger_max_=high;deadband_=deadband;last_config_=config;configured_=true;ready_=limits_ok(hands_);
  }
  bool begin_resume(Hand &h){
    if(resume_duration_<=0) return true;
    if(!ready_ || h.names.size()!=20) return false;
    std::vector<double> arms,hands;
    const double stamp=seconds();
    for(const auto *names:{&h.arms,&h.names}){
      auto &values=names==&h.arms?arms:hands;
      for(const auto &name:*names){
        auto it=measured_.find(name);
        if(it==measured_.end() || stamp-it->second.second>.5) return false;
        values.push_back(it->second.first);
      }
    }
    h.resume_arms=std::move(arms);h.resume_hands=std::move(hands);
    h.resume_start=stamp;h.resume_active=true;
    RCLCPP_INFO(get_logger(), "%s: resume from measured pose over %.2f seconds",h.side.c_str(),resume_duration_);
    return true;
  }
  void blend_resume(Hand &h,std::vector<double> &positions,bool arm){
    if(!h.resume_active) return;
    const double t=std::clamp((seconds()-h.resume_start)/resume_duration_,0.0,1.0);
    const double alpha=t*t*(3.0-2.0*t);
    const auto &start=arm?h.resume_arms:h.resume_hands;
    for(size_t i=0;i<positions.size();++i) positions[i]=start[i]+alpha*(positions[i]-start[i]);
    // Both hand and arm outputs use the same clock. Complete after arm output.
    if(arm && t>=1.0) h.resume_active=false;
  }
  void hand_command(Hand &h,double amount){
    h.trigger=amount;h.trigger_time=seconds();
    if(!ready_ || paused_ || h.held || !h.enabled || seconds()-h.heartbeat>.5 || h.save_pose==5) return;
    Trajectory out;out.joint_names=h.names;out.points.resize(1);out.points[0].positions.resize(20);
    for(size_t i=0;i<20;++i) out.points[0].positions[i]=h.opened[i]+amount*(h.closed[i]-h.opened[i]);
    blend_resume(h,out.points[0].positions,false);
    std_msgs::msg::Float64MultiArray effort;effort.data.assign(20,h.open_current+amount*(h.closed_current-h.open_current));
    h.effort_pub->publish(effort);h.hand_pub->publish(out);
  }
  void trajectory(size_t index,const Trajectory &msg){
    const auto started=Clock::now();auto &h=hands_[index];const bool a3=profile_=="a3_sh5";const size_t size=a3?8:7;
    if(msg.joint_names.size()!=size || msg.points.size()!=1 || std::set<std::string>(msg.joint_names.begin(),msg.joint_names.end()).size()!=size) return;
    auto expected=h.arms;if(a3) expected.push_back("gripper_"+h.letter+"_joint1");
    for(const auto &name:expected) if(std::find(msg.joint_names.begin(),msg.joint_names.end(),name)==msg.joint_names.end()) return;
    const auto &p=msg.points[0];
    for(const auto *v:{&p.positions,&p.velocities,&p.accelerations,&p.effort}) if((v==&p.positions || !v->empty()) && (v->size()!=size || !finite(*v))) return;
    if(a3 && configured_){auto at=std::find(msg.joint_names.begin(),msg.joint_names.end(),expected.back())-msg.joint_names.begin();hand_command(h,normalize(p.positions[at],trigger_min_,trigger_max_));}
    // Preserve broadcaster IDLE hold, saved poses and slow-start arm targets.
    if(ready_ && !paused_ && !h.held){
      Trajectory out;out.header=msg.header;out.joint_names=h.arms;out.points.resize(1);auto &q=out.points[0];q.time_from_start=p.time_from_start;
      for(const auto &name:h.arms){auto at=std::find(msg.joint_names.begin(),msg.joint_names.end(),name)-msg.joint_names.begin();
        q.positions.push_back(p.positions[at]);if(!p.velocities.empty()) q.velocities.push_back(p.velocities[at]);
        if(!p.accelerations.empty()) q.accelerations.push_back(p.accelerations[at]);
        if(!p.effort.empty()) q.effort.push_back(p.effort[at]);
      }
      if(h.resume_active){
        if(seconds()-h.heartbeat>.5){h.held=true;h.resume_active=false;h.saw_disabled=false;return;}
        blend_resume(h,q.positions,true);
        q.velocities.clear();q.accelerations.clear();q.effort.clear();
      }
      h.arm_pub->publish(out);
    }
    const double us=std::chrono::duration<double,std::micro>(Clock::now()-started).count();++calls_;total_us_+=us;max_us_=std::max(max_us_,us);
  }
public:
  HandControl():Node("hand_control_bridge"){
    resume_duration_=declare_parameter<double>("resume_blend_duration",0.0);
    if(!std::isfinite(resume_duration_) || resume_duration_<0) throw std::runtime_error("Invalid resume duration");
    if(resume_duration_>0){
      auto callback=[this](State::ConstSharedPtr m){
        if(m->name.size()!=m->position.size() || !finite(m->position) ||
           std::set<std::string>(m->name.begin(),m->name.end()).size()!=m->name.size()) return;
        const double stamp=seconds();
        for(size_t i=0;i<m->name.size();++i) measured_[m->name[i]]={m->position[i],stamp};
      };
      follower_states_=create_subscription<State>("/joint_states",rclcpp::SensorDataQoS(),callback);
      arm_hand_states_=create_subscription<State>("/arm_hand/joint_states",rclcpp::SensorDataQoS(),callback);
    }
    profile_=declare_parameter<std::string>("control_profile","a3_sh5");
    if(profile_!="a3_sh5" && profile_!="lg2_mini_sh5_recording") throw std::runtime_error("Unsupported control profile");
    auto qos=rclcpp::QoS(1).reliable();
    for(size_t i=0;i<2;++i){auto &h=hands_[i];h.side=i==0?"left":"right";h.letter=i==0?"l":"r";
      for(size_t j=1;j<=7;++j) h.arms.push_back("arm_"+h.letter+"_joint"+std::to_string(j));
      const std::string base="/leader/joint_trajectory_command_broadcaster_"+h.side;
      h.arm_pub=create_publisher<Trajectory>(base+"/joint_trajectory",qos);h.hand_pub=create_publisher<Trajectory>(base+"_hand/joint_trajectory",qos);
      h.effort_pub=create_publisher<std_msgs::msg::Float64MultiArray>("/effort_"+h.letter+"_controller/commands",qos);
      auto input=declare_parameter<std::string>(h.side+"_trajectory_topic","/leader/a3/"+h.side+"/joint_trajectory");
      if(input==base+"/joint_trajectory") throw std::runtime_error("Input/output feedback loop");
      h.input=create_subscription<Trajectory>(input,qos,[this,i](Trajectory::ConstSharedPtr m){trajectory(i,*m);});
      h.teleop_sub=create_subscription<std_msgs::msg::UInt8>("/leader/"+h.side+"_teleop_state",qos,[this,i](std_msgs::msg::UInt8::ConstSharedPtr m){
        auto &hand=hands_[i];const bool enabled=m->data==1;
        if(hand.held && hand.resume_allowed && !enabled) hand.saw_disabled=true;
        if(hand.resume_active && !enabled){hand.held=true;hand.resume_active=false;hand.saw_disabled=true;}
        if(hand.held && hand.resume_allowed && hand.saw_disabled && enabled && !hand.enabled){
          if(begin_resume(hand)) hand.held=false;
          else RCLCPP_WARN(get_logger(), "Resume held: fresh measured arm/hand state required");
        }
        hand.enabled=enabled;hand.heartbeat=seconds();});
      h.save_sub=create_subscription<std_msgs::msg::UInt8>("/leader/"+h.side+"_save_pose_state",qos,[this,i](std_msgs::msg::UInt8::ConstSharedPtr m){hands_[i].save_pose=m->data;});
      h.hold_service=create_service<SetBool>("/leader/hand_control/"+h.side+"/pause",[this,i](SetBool::Request::SharedPtr q,SetBool::Response::SharedPtr r){
        hands_[i].resume_active=false;hands_[i].held=q->data;hands_[i].saw_disabled=false;hands_[i].resume_allowed=false;r->success=true;r->message="Side command ownership updated";});
      h.resume_service=create_service<SetBool>("/leader/hand_control/"+h.side+"/allow_resume",[this,i](SetBool::Request::SharedPtr q,SetBool::Response::SharedPtr r){
        hands_[i].resume_allowed=q->data;hands_[i].saw_disabled=false;r->success=true;});
    }
    pause_=create_service<SetBool>("/leader/hand_preset/pause",[this](SetBool::Request::SharedPtr q,SetBool::Response::SharedPtr r){paused_=q->data;r->success=true;});
    apply_=create_service<SetConfig>("/leader/hand_control/apply",[this](SetConfig::Request::SharedPtr q,SetConfig::Response::SharedPtr r){
      try{if(q->parameters.size()!=1 || q->parameters[0].name!="config" || q->parameters[0].value.type!=4) throw std::runtime_error("Expected one string config");
        configure(Json::parse(q->parameters[0].value.string_value));r->result.successful=true;
      }catch(const std::exception &e){r->result.successful=false;r->result.reason=e.what();}});
    description_=create_subscription<std_msgs::msg::String>("/robot_description",rclcpp::QoS(1).transient_local(),[this](std_msgs::msg::String::ConstSharedPtr m){have_model_=model_.initString(m->data);ready_=configured_ && limits_ok(hands_);});
    if(profile_=="lg2_mini_sh5_recording") raw_states_=create_subscription<State>("/leader/joint_states",qos,[this](State::ConstSharedPtr m){
      if(!configured_ || m->name.size()!=m->position.size() || !finite(m->position) || std::set<std::string>(m->name.begin(),m->name.end()).size()!=m->name.size()) return;
      for(auto &h:hands_){auto it=std::find(m->name.begin(),m->name.end(),"gripper_"+h.letter+"_joint1");if(it==m->name.end()) continue;
        double amount=normalize(m->position[it-m->name.begin()],h.raw_open,h.raw_closed);hand_command(h,amount<=deadband_?0:amount);}});
    virtual_pub_=create_publisher<State>("/topic_based_joint_states",qos);
    virtual_sub_=create_subscription<State>("/topic_based_joint_commands",qos,[this](State::ConstSharedPtr m){
      if(m->name.size()!=m->position.size() || !finite(m->position) || std::set<std::string>(m->name.begin(),m->name.end()).size()!=m->name.size()) return;
      State out;out.header.stamp=now();for(size_t i=0;i<m->name.size();++i) if(m->name[i]=="gripper_l_joint1" || m->name[i]=="gripper_r_joint1"){
        out.name.push_back(m->name[i]);out.position.push_back(std::clamp(m->position[i],std::min(trigger_min_,trigger_max_),std::max(trigger_min_,trigger_max_)));out.velocity.push_back(0);out.effort.push_back(0);}
      virtual_pub_->publish(out);});
    status_=create_publisher<std_msgs::msg::String>("/leader/hand_control/status",rclcpp::QoS(1).transient_local());
    timer_=create_wall_timer(std::chrono::milliseconds(250),[this]{
      Json j={{"control_profile",profile_},{"follower_ready",ready_},{"configured",configured_},{"paused",paused_}};
      for(const auto &h:hands_){j["trigger_values"][h.side]=h.trigger;j["teleop_enabled"][h.side]=h.enabled && seconds()-h.heartbeat<=.5;j["held"][h.side]=h.held;j["resume_blending"][h.side]=h.resume_active;}
      j["callback_timing_us"]={{"count",calls_},{"mean",calls_?total_us_/static_cast<double>(calls_):0},{"max",max_us_}};
      std_msgs::msg::String msg;msg.data=j.dump();status_->publish(msg);});
  }
};
int main(int argc,char **argv){rclcpp::init(argc,argv);try{rclcpp::spin(std::make_shared<HandControl>());}catch(const std::exception &e){fprintf(stderr,"%s\n",e.what());rclcpp::shutdown();return 1;}rclcpp::shutdown();return 0;}
