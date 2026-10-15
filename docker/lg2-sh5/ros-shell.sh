#!/usr/bin/env bash
set -eo pipefail
source /full/ros_ws/install/setup.bash
export LD_LIBRARY_PATH="/usr/lib/aarch64-linux-gnu/nvidia:/usr/local/cuda/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export ROS_DOMAIN_ID=174 RMW_IMPLEMENTATION=rmw_zenoh_cpp
export ZENOH_CONFIG_OVERRIDE='transport/shared_memory/enabled=false;scouting/multicast/enabled=false;connect/endpoints=["tcp/127.0.0.1:7447"]'
export ROS_LOG_DIR=/workspace/ros-log
mkdir -p "$ROS_LOG_DIR"
case "${1:-}" in
  router)
    unset ZENOH_CONFIG_OVERRIDE
    exec flock -n /workspace/router.lock ros2 run rmw_zenoh_cpp rmw_zenohd
    ;;
  follower)
    test -c /dev/follower
    echo 'SH5 init_position=true: clear the workspace and keep emergency stop ready.'
    exec flock -n /workspace/follower.lock ros2 launch ffw_bringup ffw_sh5_follower_ai.launch.py \
      init_position:=true launch_cameras:=true head_camera_type:=zed \
      auto_assign_cameras:=false launch_lidar:=false
    ;;
  leader)
    test -c /dev/left_leader && test -c /dev/right_leader
    exec flock -n /workspace/leader.lock ros2 launch ffw_bringup ffw_lg2_mini_leader_recording.launch.py \
      launch_final_pose:=false
    ;;
  shell) exec bash --noprofile --norc ;;
  *) echo 'Usage: bash lg2-sh5-ros router|follower|leader|shell' >&2; exit 2 ;;
esac
