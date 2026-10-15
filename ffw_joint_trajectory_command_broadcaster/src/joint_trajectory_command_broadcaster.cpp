// Copyright 2021 ros2_control development team
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "joint_trajectory_command_broadcaster/joint_trajectory_command_broadcaster.hpp"

#include <cstddef>
#include <limits>
#include <memory>
#include <string>
#include <unordered_map>
#include <vector>
#include <functional>
#include <cmath>
#include <algorithm>
#include <iterator>

#include "hardware_interface/types/hardware_interface_type_values.hpp"
#include "rclcpp/qos.hpp"
#include "rclcpp/time.hpp"
#include "std_msgs/msg/header.hpp"
#include "std_msgs/msg/u_int8.hpp"
#include "trajectory_msgs/msg/joint_trajectory.hpp"
#include "sensor_msgs/msg/joint_state.hpp"
#include "urdf/model.h"

namespace rclcpp_lifecycle
{
class State;
}  // namespace rclcpp_lifecycle

namespace joint_trajectory_command_broadcaster
{
const auto kUninitializedValue = std::numeric_limits<double>::quiet_NaN();
using hardware_interface::HW_IF_POSITION;

JointTrajectoryCommandBroadcaster::JointTrajectoryCommandBroadcaster() {}

controller_interface::CallbackReturn JointTrajectoryCommandBroadcaster::on_init()
{
  try {
    param_listener_ = std::make_shared<ParamListener>(get_node());
    params_ = param_listener_->get_params();
  } catch (const std::exception & e) {
    fprintf(stderr, "Exception thrown during init stage with message: %s \n", e.what());
    return CallbackReturn::ERROR;
  }

  return CallbackReturn::SUCCESS;
}

controller_interface::InterfaceConfiguration
JointTrajectoryCommandBroadcaster::command_interface_configuration() const
{
  return controller_interface::InterfaceConfiguration{
    controller_interface::interface_configuration_type::NONE};
}

controller_interface::InterfaceConfiguration JointTrajectoryCommandBroadcaster::
state_interface_configuration()
const
{
  controller_interface::InterfaceConfiguration state_interfaces_config;

  state_interfaces_config.type = controller_interface::interface_configuration_type::INDIVIDUAL;
  for (const auto & joint : params_.left_joints) {
    state_interfaces_config.names.push_back(joint + "/" + HW_IF_POSITION);
  }
  for (const auto & joint : params_.right_joints) {
    state_interfaces_config.names.push_back(joint + "/" + HW_IF_POSITION);
  }
  if (params_.use_joystick_arm_toggles && !params_.joystick_short_press_events) {
    state_interfaces_config.names.push_back("sensorxel_l_joy/JOYSTICK TACT SWITCH");
    state_interfaces_config.names.push_back("sensorxel_r_joy/JOYSTICK TACT SWITCH");
  }
  return state_interfaces_config;
}

controller_interface::CallbackReturn JointTrajectoryCommandBroadcaster::on_configure(
  const rclcpp_lifecycle::State & /*previous_state*/)
{
  if (!param_listener_) {
    RCLCPP_ERROR(get_node()->get_logger(), "Error encountered during init");
    return controller_interface::CallbackReturn::ERROR;
  }
  params_ = param_listener_->get_params();
  if (params_.joystick_slow_start_duration < 0.0 ||
    !std::isfinite(params_.joystick_slow_start_duration))
  {
    RCLCPP_ERROR(get_node()->get_logger(), "joystick_slow_start_duration must be finite and nonnegative");
    return controller_interface::CallbackReturn::ERROR;
  }

  // Map interface if needed
  map_interface_to_joint_state_.clear();
  map_interface_to_joint_state_[HW_IF_POSITION] = params_.map_interface_to_joint_state.position;

  try {
    // Create publishers for left and right groups
    std::vector<std::string> groups = {"left", "right"};

    for (const auto & group_name : groups) {
      // Get joints for this group
      std::vector<std::string> group_joints;
      if (group_name == "left" && !params_.left_joints.empty()) {
        group_joints = params_.left_joints;
      } else if (group_name == "right" && !params_.right_joints.empty()) {
        group_joints = params_.right_joints;
      }

      if (group_joints.empty()) {
        continue;  // Skip empty groups
      }

      group_joint_names_[group_name] = group_joints;

      // Get offsets for this group
      if (group_name == "left" && !params_.left_offsets.empty()) {
        group_joint_offsets_[group_name] = params_.left_offsets;
      } else if (group_name == "right" && !params_.right_offsets.empty()) {
        group_joint_offsets_[group_name] = params_.right_offsets;
      } else {
        // Initialize empty offsets if not provided
        group_joint_offsets_[group_name] = std::vector<double>();
      }

      // Get reverse joints for this group
      if (group_name == "left" && !params_.left_reverse_joints.empty()) {
        group_reverse_joints_[group_name] = params_.left_reverse_joints;
      } else if (group_name == "right" && !params_.right_reverse_joints.empty()) {
        group_reverse_joints_[group_name] = params_.right_reverse_joints;
      } else {
        // Initialize empty reverse joints if not provided
        group_reverse_joints_[group_name] = std::vector<std::string>();
      }

      // Create topic name with group-specific namespace
      std::string topic_name;
      topic_name = "joint_trajectory_command_broadcaster_" + group_name + "/joint_trajectory";
      group_topic_names_[group_name] = topic_name;

      // Create publisher for this group
      joint_trajectory_publishers_[group_name] =
        get_node()->create_publisher<trajectory_msgs::msg::JointTrajectory>(
        topic_name, rclcpp::SystemDefaultsQoS());

      realtime_joint_trajectory_publishers_[group_name] =
        std::make_shared<realtime_tools::RealtimePublisher<trajectory_msgs::msg::JointTrajectory>>(
        joint_trajectory_publishers_[group_name]);

      RCLCPP_INFO(
        get_node()->get_logger(),
        "Created joint trajectory publisher for group '%s' on topic: %s with %zu joints",
        group_name.c_str(), topic_name.c_str(), group_joints.size());

      if (params_.use_joystick_arm_toggles) {
        teleop_state_publishers_[group_name] =
          get_node()->create_publisher<std_msgs::msg::UInt8>(
          group_name + "_teleop_state", rclcpp::SystemDefaultsQoS());
      }
    }

    // Store the groups for later use
    trajectory_groups_ = groups;

    // Create subscriber for follower joint states
    joint_states_subscriber_ = get_node()->create_subscription<sensor_msgs::msg::JointState>(
      params_.follower_joint_states_topic, rclcpp::SystemDefaultsQoS(),
      std::bind(&JointTrajectoryCommandBroadcaster::joint_states_callback, this,
        std::placeholders::_1));

    if (params_.use_joystick_arm_toggles && params_.joystick_short_press_events) {
      joystick_short_press_subscriber_ = get_node()->create_subscription<std_msgs::msg::String>(
        params_.joystick_short_press_topic, rclcpp::SystemDefaultsQoS(),
        [this](const std_msgs::msg::String::SharedPtr msg) {
          if (msg->data == "left") {
            left_short_press_events_.fetch_add(1, std::memory_order_relaxed);
          } else if (msg->data == "right") {
            right_short_press_events_.fetch_add(1, std::memory_order_relaxed);
          }
        });
    }

    RCLCPP_INFO(
      get_node()->get_logger(),
      "Subscribed to follower joint states topic: %s",
      params_.follower_joint_states_topic.c_str());
  } catch (const std::exception & e) {
    // get_node() may throw, logging raw here
    fprintf(stderr, "Exception thrown during init stage with message: %s \n", e.what());
    return CallbackReturn::ERROR;
  }

  const std::string & urdf = get_robot_description();
  is_model_loaded_ = !urdf.empty() && model_.initString(urdf);
  if (!is_model_loaded_) {
    RCLCPP_ERROR(
      get_node()->get_logger(),
      "Failed to parse robot description. Will proceed without URDF-based filtering.");
  }

  return CallbackReturn::SUCCESS;
}

controller_interface::CallbackReturn JointTrajectoryCommandBroadcaster::on_activate(
  const rclcpp_lifecycle::State & /*previous_state*/)
{
  if (!init_joint_data()) {
    RCLCPP_ERROR(
      get_node()->get_logger(), "None of requested interfaces exist. Controller will not run.");
    return CallbackReturn::ERROR;
  }

  // Check offsets for each group
  for (const auto & group_name : trajectory_groups_) {
    const auto & group_joints = group_joint_names_[group_name];
    const size_t num_joints = group_joints.size();

    if (group_joint_offsets_[group_name].empty()) {
      // If no offsets provided, use zeros
      group_joint_offsets_[group_name].assign(num_joints, 0.0);
    } else if (group_joint_offsets_[group_name].size() != num_joints) {
      RCLCPP_ERROR(
        get_node()->get_logger(),
        "The number of provided offsets (%zu) for group '%s' does not match the number of "
        "joints (%zu).",
        group_joint_offsets_[group_name].size(), group_name.c_str(), num_joints);
      return CallbackReturn::ERROR;
    }

    RCLCPP_INFO(
      get_node()->get_logger(),
      "Group '%s' configured with %zu joints and %zu offsets",
      group_name.c_str(), num_joints, group_joint_offsets_[group_name].size());
  }

  // No need to init JointState or DynamicJointState messages, only JointTrajectory
  // will be published. We'll construct it on-the-fly in update()

  return CallbackReturn::SUCCESS;
}


controller_interface::CallbackReturn JointTrajectoryCommandBroadcaster::on_deactivate(
  const rclcpp_lifecycle::State & /*previous_state*/)
{
  joint_names_.clear();
  name_if_value_mapping_.clear();
  group_joint_names_.clear();
  group_joint_offsets_.clear();
  group_topic_names_.clear();
  group_reverse_joints_.clear();
  group_slow_start_time_.clear();
  group_slow_start_positions_.clear();
  left_short_press_events_.store(0, std::memory_order_relaxed);
  right_short_press_events_.store(0, std::memory_order_relaxed);

  return CallbackReturn::SUCCESS;
}

template<typename T>
bool has_any_key(
  const std::unordered_map<std::string, T> & map, const std::vector<std::string> & keys)
{
  for (const auto & key_item : map) {
    const auto & key = key_item.first;
    if (std::find(keys.cbegin(), keys.cend(), key) != keys.cend()) {
      return true;
    }
  }
  return false;
}

bool JointTrajectoryCommandBroadcaster::init_joint_data()
{
  joint_names_.clear();
  if (state_interfaces_.empty()) {
    return false;
  }

  // Initialize mapping
  for (auto si = state_interfaces_.crbegin(); si != state_interfaces_.crend(); si++) {
    if (name_if_value_mapping_.count(si->get_prefix_name()) == 0) {
      name_if_value_mapping_[si->get_prefix_name()] = {};
    }
    std::string interface_name = si->get_interface_name();
    if (map_interface_to_joint_state_.count(interface_name) > 0) {
      interface_name = map_interface_to_joint_state_[interface_name];
    }
    name_if_value_mapping_[si->get_prefix_name()][interface_name] = kUninitializedValue;
  }

  // Filter out joints without position interface (since we want positions)
  for (const auto & name_ifv : name_if_value_mapping_) {
    const auto & interfaces_and_values = name_ifv.second;
    if (has_any_key(interfaces_and_values, {HW_IF_POSITION})) {
      if (
        !params_.use_urdf_to_filter || !is_model_loaded_ ||
        model_.getJoint(name_ifv.first))
      {
        joint_names_.push_back(name_ifv.first);
      }
    }
  }

  return true;
}

double get_value(
  const std::unordered_map<std::string, std::unordered_map<std::string, double>> & map,
  const std::string & name, const std::string & interface_name)
{
  const auto & interfaces_and_values = map.at(name);
  const auto interface_and_value = interfaces_and_values.find(interface_name);
  if (interface_and_value != interfaces_and_values.cend()) {
    return interface_and_value->second;
  } else {
    return kUninitializedValue;
  }
}

void JointTrajectoryCommandBroadcaster::joint_states_callback(
  const sensor_msgs::msg::JointState::SharedPtr msg)
{
  // Update follower joint positions
  for (size_t i = 0; i < msg->name.size(); ++i) {
    if (i < msg->position.size()) {
      follower_joint_positions_[msg->name[i]] = msg->position[i];
    }
  }

  // Debug logging (only log occasionally to avoid spam)
  static int callback_count = 0;
  if (++callback_count % 100 == 0) {
    RCLCPP_DEBUG(get_node()->get_logger(),
      "Received follower joint states for %zu joints", msg->name.size());
  }
}

double JointTrajectoryCommandBroadcaster::calculate_mean_error() const
{
  // Check if we have received any follower joint states
  if (follower_joint_positions_.empty()) {
    return std::numeric_limits<double>::max();  // Return max error if no follower data
  }

  double total_error = 0.0;
  int valid_joints = 0;

  // Calculate mean error across all joints in all groups
  for (const auto & group_pair : group_joint_names_) {
    const auto & group_name = group_pair.first;
    const auto & group_joints = group_pair.second;
    // Safely get group offsets and reverse joints
    std::vector<double> group_offsets;
    std::vector<std::string> group_reverse_joints;

    auto offsets_it = group_joint_offsets_.find(group_name);
    if (offsets_it != group_joint_offsets_.end()) {
      group_offsets = offsets_it->second;
    }

    auto reverse_it = group_reverse_joints_.find(group_name);
    if (reverse_it != group_reverse_joints_.end()) {
      group_reverse_joints = reverse_it->second;
    }

    for (size_t i = 0; i < group_joints.size(); ++i) {
      const auto & joint_name = group_joints[i];
      auto follower_it = follower_joint_positions_.find(joint_name);
      if (follower_it == follower_joint_positions_.end()) {
        continue;  // Skip joints not available in follower
      }

      double leader_pos = get_value(name_if_value_mapping_, joint_name, HW_IF_POSITION);
      if (std::isnan(leader_pos)) {
        continue;  // Skip joints without valid leader position
      }

      // Apply reverse and offset to leader position for comparison
      if (std::find(group_reverse_joints.begin(), group_reverse_joints.end(), joint_name) !=
        group_reverse_joints.end())
      {
        leader_pos = -leader_pos;
      }

      // Apply group offset
      if (i < group_offsets.size()) {
        leader_pos += group_offsets[i];
      }

      total_error += std::abs(leader_pos - follower_it->second);
      valid_joints++;
    }
  }

  return valid_joints > 0 ? total_error / valid_joints : std::numeric_limits<double>::max();
}

bool JointTrajectoryCommandBroadcaster::check_trigger_active() const
{
  // Check if gripper trigger joints are above threshold
  double gripper_r_pos = get_value(name_if_value_mapping_, "gripper_r_joint1", HW_IF_POSITION);
  double gripper_l_pos = get_value(name_if_value_mapping_, "gripper_l_joint1", HW_IF_POSITION);

  // Return true if both grippers are above threshold
  return (!std::isnan(gripper_r_pos) &&
         gripper_r_pos * params_.trigger_sign >=
         params_.trigger_threshold * params_.trigger_sign) &&
         (!std::isnan(gripper_l_pos) &&
         gripper_l_pos * params_.trigger_sign >= params_.trigger_threshold * params_.trigger_sign);
}

void JointTrajectoryCommandBroadcaster::update_trigger_state(const rclcpp::Time & current_time)
{
  bool current_trigger_active = check_trigger_active();

  if (current_trigger_active && !trigger_counting_) {
    // Start trigger counting (only if mode hasn't changed in this trigger session)
    if (!mode_changed_in_this_trigger_) {
      trigger_counting_ = true;
      trigger_start_time_ = current_time;
      RCLCPP_INFO(get_node()->get_logger(), "Trigger activated - counting started");
    }
  } else if (!current_trigger_active) {
    // Trigger released - reset all states
    if (trigger_counting_) {
      trigger_counting_ = false;
      RCLCPP_INFO(get_node()->get_logger(), "Trigger released - counting stopped");
    }
    // Reset for next trigger session when trigger is completely released
    mode_changed_in_this_trigger_ = false;
  }

  // Check if trigger has been held for specified duration and mode hasn't changed in this session
  if (trigger_counting_ && !mode_changed_in_this_trigger_ &&
    (current_time - trigger_start_time_) >=
    rclcpp::Duration::from_seconds(params_.trigger_duration))
  {
    // Toggle auto mode state
    if (auto_mode_ == AutoMode::STOPPED) {
      auto_mode_ = AutoMode::ACTIVE;
      // Reset sync state when starting auto mode
      joints_synced_ = false;
      first_publish_ = true;
      RCLCPP_INFO(get_node()->get_logger(),
          "Auto mode ACTIVATED - follower will slowly follow leader");
    } else {
      auto_mode_ = AutoMode::STOPPED;
      RCLCPP_INFO(get_node()->get_logger(), "Auto mode STOPPED - follower paused");
    }

    // Mark that mode has changed in this trigger session
    mode_changed_in_this_trigger_ = true;
    trigger_counting_ = false;  // Stop counting
  }
}

void JointTrajectoryCommandBroadcaster::update_joystick_arm_modes(
  const rclcpp::Time & current_time)
{
  const std::pair<const char *, const char *> bindings[] = {
    {"left", "sensorxel_l_joy"},
    {"right", "sensorxel_r_joy"},
  };

  for (const auto & [group_name, sensor_name] : bindings) {
    bool toggle = false;
    if (params_.joystick_short_press_events) {
      auto & events = group_name[0] == 'l' ? left_short_press_events_ : right_short_press_events_;
      toggle = (events.exchange(0, std::memory_order_relaxed) % 2) != 0;
    } else {
      const double value =
        get_value(name_if_value_mapping_, sensor_name, "JOYSTICK TACT SWITCH");
      const bool pressed = !std::isnan(value) && value > 0.5;
      bool & was_pressed = joystick_button_pressed_[group_name];
      toggle = pressed && !was_pressed;
      was_pressed = pressed;
    }

    if (toggle) {
      bool & active = group_teleoperation_active_[group_name];
      active = !active;
      if (active) {
        joints_synced_ = false;
        first_publish_ = true;
        group_slow_start_time_[group_name] = current_time;
        group_slow_start_positions_.erase(group_name);
      } else {
        group_slow_start_time_.erase(group_name);
        group_slow_start_positions_.erase(group_name);
      }
      RCLCPP_INFO(
        get_node()->get_logger(), "%s arm teleoperation %s",
        group_name, active ? "ACTIVATED" : "STOPPED");
    }
  }
}

bool JointTrajectoryCommandBroadcaster::check_joints_synced() const
{
  double mean_error = calculate_mean_error();
  return mean_error <= params_.sync_threshold;
}

controller_interface::return_type JointTrajectoryCommandBroadcaster::update(
  const rclcpp::Time & time, const rclcpp::Duration & /*period*/)
{
  // Update stored values
  for (const auto & state_interface : state_interfaces_) {
    std::string interface_name = state_interface.get_interface_name();
    if (map_interface_to_joint_state_.count(interface_name) > 0) {
      interface_name = map_interface_to_joint_state_[interface_name];
    }
    auto value = state_interface.get_optional();
    if (value) {
      name_if_value_mapping_[state_interface.get_prefix_name()][interface_name] = *value;
    }
  }

  if (params_.use_joystick_arm_toggles) {
    update_joystick_arm_modes(time);
    for (const auto & group_name : trajectory_groups_) {
      std_msgs::msg::UInt8 state;
      state.data = group_teleoperation_active_[group_name] ? 1 : 0;
      teleop_state_publishers_[group_name]->publish(state);
    }
    if (!group_teleoperation_active_["left"] && !group_teleoperation_active_["right"]) {
      return controller_interface::return_type::OK;
    }
  } else {
    update_trigger_state(time);
    if (auto_mode_ == AutoMode::STOPPED) {
      return controller_interface::return_type::OK;
    }
  }

  // Calculate mean error and check if joints are synced
  double mean_error = calculate_mean_error();
  bool current_synced = check_joints_synced();

  // Update sync status and handle first publish
  if (first_publish_) {
    joints_synced_ = false;
    first_publish_ = false;
    RCLCPP_INFO(get_node()->get_logger(),
        "First publish - using adaptive time_from_start based on error");
  } else {
    // Once synced, stay synced permanently
    if (!joints_synced_ && current_synced) {
      joints_synced_ = true;
      RCLCPP_INFO(get_node()->get_logger(),
          "Joints synced for the first time - switching to immediate time_from_start permanently");
    }
  }

  // Publish JointTrajectory messages for each group with current positions
  for (const auto & group_name : trajectory_groups_) {
    if (params_.use_joystick_arm_toggles && !group_teleoperation_active_[group_name]) {
      continue;
    }
    const auto & group_joints = group_joint_names_[group_name];
    // Safely get group offsets and reverse joints
    std::vector<double> group_offsets;
    std::vector<std::string> group_reverse_joints;

    auto offsets_it = group_joint_offsets_.find(group_name);
    if (offsets_it != group_joint_offsets_.end()) {
      group_offsets = offsets_it->second;
    }

    auto reverse_it = group_reverse_joints_.find(group_name);
    if (reverse_it != group_reverse_joints_.end()) {
      group_reverse_joints = reverse_it->second;
    }

    if (group_joints.empty()) {
      continue;  // Skip empty groups
    }

    auto & realtime_publisher = realtime_joint_trajectory_publishers_[group_name];
    if (realtime_publisher) {
      trajectory_msgs::msg::JointTrajectory traj_msg;
      traj_msg.header.stamp = rclcpp::Time(0, 0);
      traj_msg.joint_names = group_joints;

      const size_t num_joints = group_joints.size();
      traj_msg.points.clear();
      traj_msg.points.resize(1);
      traj_msg.points[0].positions.resize(num_joints, kUninitializedValue);

      for (size_t i = 0; i < num_joints; ++i) {
        double pos_value =
          get_value(name_if_value_mapping_, group_joints[i], HW_IF_POSITION);

        // Check if the current joint is in the reverse_joints parameter
        if (
          std::find(
            group_reverse_joints.begin(),
            group_reverse_joints.end(),
            group_joints[i]) != group_reverse_joints.end())
        {
          pos_value = -pos_value;
        }

        // Apply offset
        if (i < group_offsets.size()) {
          pos_value += group_offsets[i];
        }

        traj_msg.points[0].positions[i] = pos_value;
      }

      if (params_.use_joystick_arm_toggles && params_.joystick_slow_start_duration > 0.0) {
        auto start_time = group_slow_start_time_.find(group_name);
        if (start_time != group_slow_start_time_.end()) {
          auto start_positions = group_slow_start_positions_.find(group_name);
          if (start_positions == group_slow_start_positions_.end()) {
            std::vector<double> measured;
            measured.reserve(num_joints);
            bool complete = true;
            for (const auto & joint : group_joints) {
              auto follower = follower_joint_positions_.find(joint);
              if (follower == follower_joint_positions_.end() || !std::isfinite(follower->second)) {
                complete = false;
                break;
              }
              measured.push_back(follower->second);
            }
            if (!complete) {
              continue;  // Never ramp from an unknown follower pose.
            }
            start_positions = group_slow_start_positions_.emplace(group_name, std::move(measured)).first;
            start_time->second = time;
          }
          const double elapsed = (time - start_time->second).seconds();
          const double amount = std::clamp(elapsed / params_.joystick_slow_start_duration, 0.0, 1.0);
          for (size_t i = 0; i < num_joints; ++i) {
            traj_msg.points[0].positions[i] = start_positions->second[i] + amount *
              (traj_msg.points[0].positions[i] - start_positions->second[i]);
          }
          if (amount >= 1.0) {
            group_slow_start_time_.erase(start_time);
            group_slow_start_positions_.erase(start_positions);
          } else {
            traj_msg.points[0].time_from_start = rclcpp::Duration::from_seconds(0.02);
            realtime_publisher->try_publish(traj_msg);
            continue;
          }
        }
        bool close_to_follower = true;
        for (size_t i = 0; i < num_joints; ++i) {
          auto follower = follower_joint_positions_.find(group_joints[i]);
          if (follower == follower_joint_positions_.end() ||
            !std::isfinite(follower->second) ||
            std::abs(traj_msg.points[0].positions[i] - follower->second) > 0.15)
          {
            close_to_follower = false;
            break;
          }
        }
        if (close_to_follower) {
          traj_msg.points[0].time_from_start = rclcpp::Duration::from_seconds(0.02);
          realtime_publisher->try_publish(traj_msg);
          continue;
        }
      }

      // Set time_from_start based on sync status and mean error
      if (joints_synced_) {
        traj_msg.points[0].time_from_start = rclcpp::Duration(0, 0);  // immediate when synced
      } else {
        // Adaptive timing based on mean error using parameters
        if(mean_error < params_.min_error) {
          mean_error = 0;
        }

        double error_ratio = std::min(mean_error / params_.max_error, 1.0);
        // Corrected logic: small error -> small delay, large error -> large delay
        double adaptive_delay = params_.min_delay + (params_.max_delay - params_.min_delay) *
          error_ratio;


        // Convert to nanoseconds
        int32_t delay_ns = static_cast<int32_t>(adaptive_delay * 1e9);
        traj_msg.points[0].time_from_start = rclcpp::Duration(0, delay_ns);
      }

      realtime_publisher->try_publish(traj_msg);
    }
  }

  return controller_interface::return_type::OK;
}

}  // namespace joint_trajectory_command_broadcaster

#include "pluginlib/class_list_macros.hpp"

PLUGINLIB_EXPORT_CLASS(
  joint_trajectory_command_broadcaster::JointTrajectoryCommandBroadcaster,
  controller_interface::ControllerInterface)
