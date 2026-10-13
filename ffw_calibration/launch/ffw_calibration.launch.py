#!/usr/bin/env python3
#
# Copyright 2026 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, ExecuteProcess, LogInfo, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def _launch_ui(context):
    if LaunchConfiguration('launch_ui').perform(context).lower() != 'true':
        return []
    ui_dist = os.path.join(get_package_share_directory('ffw_calibration'), 'ui', 'dist')
    if not os.path.isfile(os.path.join(ui_dist, 'index.html')):
        return [LogInfo(msg='Calibration UI was not built; run npm ci && npm run build before colcon build.')]
    return [ExecuteProcess(
        cmd=['python3', '-m', 'http.server', '5173', '--bind', '0.0.0.0',
             '--directory', ui_dist],
        output='screen',
    )]


def generate_launch_description():
    config_dir = os.path.join(get_package_share_directory('ffw_calibration'), 'config')
    calibration_service = Node(
        package='ffw_calibration',
        executable='calibration_service',
        name='ffw_calibration_service',
        output='screen',
        parameters=[{
            'calibration_pose_path': os.path.join(config_dir, 'common', 'calibration_pose.yaml'),
            'homing_offsets_path': LaunchConfiguration('homing_offsets_path'),
            'robot_poses_path': os.path.join(config_dir, 'common', 'robot_poses.yaml'),
            'joint_states_topic': '/joint_states',
            'stale_timeout_sec': 1.0,
            'default_zero_pose_duration_sec': 10.0,
            'default_effort_duration_sec': 1.0,
            'effort_hz': 50.0,
        }],
    )

    rosbridge_websocket = Node(
        package='rosbridge_server',
        executable='rosbridge_websocket',
        name='rosbridge_websocket',
        output='screen',
        parameters=[{
            'port': 9090,
            'fragment_timeout': 600,
            'max_message_size': 100000000,
            'unregister_timeout': 10.0,
            'call_service_timeout': 60.0,
        }],
    )

    return LaunchDescription([
        DeclareLaunchArgument('launch_ui', default_value='true', choices=['true', 'false']),
        DeclareLaunchArgument(
            'homing_offsets_path',
            default_value=os.path.join(
                config_dir, 'ffw_bg2_rev4_follower', 'homing_offsets.yaml'),
            description='Writable homing offsets YAML path; set this to a persistent location if needed.'),
        calibration_service,
        rosbridge_websocket,
        OpaqueFunction(function=_launch_ui),
    ])
