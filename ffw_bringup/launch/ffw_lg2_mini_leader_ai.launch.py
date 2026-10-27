#!/usr/bin/env python3
#
# Copyright 2025 ROBOTIS CO., LTD.
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
#
# Authors: Sungho Woo, Woojin Wie, Wonho Yun

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, GroupAction, RegisterEventHandler, LogInfo, OpaqueFunction
from launch.conditions import IfCondition
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch_ros.actions import Node, PushRosNamespace
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue
from ffw_bringup.launch_shutdown import leader_shutdown_actions


def generate_launch_description():
    declared_arguments = [
        DeclareLaunchArgument('launch_final_pose', default_value='false'),
        DeclareLaunchArgument('enable_sh5_recording_controls', default_value='false',
                              choices=['true', 'false'],
                              description='Opt in to LG2 mini + SH5 recording and hand controls.'),
        DeclareLaunchArgument('follower_type', default_value='',
                              description='Set ffw_sh5_rev1 for the SH5 recording profile.'),
        DeclareLaunchArgument(
            'description_file',
            default_value='ffw_lg2_mini_leader.urdf.xacro',
            description='URDF/XACRO file for the robot model.',
        ),
        DeclareLaunchArgument(
            'launch_foot_switch',
            default_value='false',
            description='Whether to launch the foot switch node.',
        ),
        DeclareLaunchArgument(
            'controller_config',
            default_value='ffw_lg2_mini_leader_ai_hardware_controller.yaml',
            description='Controller config filename; use the _extended.yaml profile for recovered task controls.',
        ),
        DeclareLaunchArgument(
            'task_controller_config', default_value='',
            description='Optional task-only controller parameter overlay.',
        ),
    ]

    description_file = LaunchConfiguration('description_file')
    launch_foot_switch = LaunchConfiguration('launch_foot_switch')

    # Robot controllers config file path
    robot_controllers = PathJoinSubstitution(
        [
            FindPackageShare('ffw_bringup'),
            'config',
            'ffw_lg2_mini_leader',
            LaunchConfiguration('controller_config'),
        ]
    )

    endpose_config = PathJoinSubstitution([
        FindPackageShare('ffw_bringup'), 'config', 'ffw_lg2_mini_leader', 'bgf_endpose.yaml'])

    # The standard profile is unchanged unless a task overlay is explicitly selected.
    def make_control_node(context):
        enabled = LaunchConfiguration('enable_sh5_recording_controls').perform(context) == 'true'
        follower = LaunchConfiguration('follower_type').perform(context)
        task_config = LaunchConfiguration('task_controller_config').perform(context)
        if enabled and (follower != 'ffw_sh5_rev1' or
                        description_file.perform(context) != 'ffw_lg2_mini_leader.urdf.xacro'):
            raise RuntimeError('SH5 recording controls require LG2 mini leader and follower_type:=ffw_sh5_rev1')
        if task_config == 'lg2_recording_controls.yaml' and not enabled:
            raise RuntimeError('Use ffw_lg2_mini_leader_recording.launch.py for the SH5 recording profile')
        if LaunchConfiguration('launch_final_pose').perform(context) == 'true' and not enabled:
            raise RuntimeError('SH5 final pose requires enable_sh5_recording_controls:=true')
        if enabled:
            if task_config not in ('', 'lg2_recording_controls.yaml'):
                raise RuntimeError('SH5 recording controls require lg2_recording_controls.yaml')
            task_config = 'lg2_recording_controls.yaml'
        parameters = [robot_controllers]
        if enabled:
            parameters.append(endpose_config)
        if task_config:
            parameters.append(PathJoinSubstitution([
                FindPackageShare('ffw_bringup'), 'config', 'ffw_lg2_mini_leader', task_config]))
        return [Node(package='controller_manager', executable='ros2_control_node',
                     parameters=parameters, output='both')]

    control_node = OpaqueFunction(function=make_control_node)

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name='xacro')]),
            ' ',
            PathJoinSubstitution(
                [FindPackageShare('ffw_description'), 'urdf', 'ffw_lg2_mini_leader', description_file]
            ),
        ]
    )
    robot_description = {'robot_description': ParameterValue(robot_description_content, value_type=str)}

    robot_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            # Only the opt-in SH5 profile disconnects joystick base commands.
            '--controller-ros-args',
            ['-r joystick_controller:/cmd_vel:=', PythonExpression([
                "'/leader/joystick_controller/disabled_cmd_vel' if '",
                LaunchConfiguration('enable_sh5_recording_controls'),
                "' == 'true' else '/cmd_vel'"])],
            '--controller-ros-args',
            ['-r /leader/joint_trajectory_command_broadcaster_left/joint_trajectory:=', PythonExpression([
                "'/leader/sh5_raw/left/joint_trajectory' if '", LaunchConfiguration('enable_sh5_recording_controls'),
                "' == 'true' else '/leader/joint_trajectory_command_broadcaster_left/joint_trajectory'"])],
            '--controller-ros-args',
            ['-r /leader/joint_trajectory_command_broadcaster_right/joint_trajectory:=', PythonExpression([
                "'/leader/sh5_raw/right/joint_trajectory' if '", LaunchConfiguration('enable_sh5_recording_controls'),
                "' == 'true' else '/leader/joint_trajectory_command_broadcaster_right/joint_trajectory'"])],
            # '--controller-ros-args',
            # '-r /leader/joint_trajectory_command_broadcaster_left/joint_trajectory:='
            # '/leader/joint_trajectory_command_broadcaster_left/raw_joint_trajectory',
            # '--controller-ros-args',
            # '-r /leader/joint_trajectory_command_broadcaster_right/joint_trajectory:='
            # '/leader/joint_trajectory_command_broadcaster_right/raw_joint_trajectory',
            'joint_state_broadcaster',
            'trigger_position_controller',
            'joystick_controller',
            'joint_trajectory_command_broadcaster',
        ],
        parameters=[robot_description],
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='both',
        parameters=[robot_description, {'frame_prefix': 'leader_'}],
    )

    foot_switch_node = Node(
        package='ffw_bringup',
        executable='foot_switch_node',
        name='foot_switch_node',
        output='both',
        parameters=[{'controller_config_path': robot_controllers}],
        condition=IfCondition(launch_foot_switch),
    )

    # leader_feedback_node = Node(
    #     package='ffw_joint_trajectory_command_broadcaster',
    #     executable='leader_feedback',
    #     name='leader_feedback',
    #     output='both',
    # )

    hand_preset_node = Node(
        package='ffw_teleop',
        executable='hand_preset_catalog',
        name='hand_preset_bridge',
        output='both',
        condition=IfCondition(LaunchConfiguration('enable_sh5_recording_controls')),
        parameters=[{'config_file': PathJoinSubstitution([
            FindPackageShare('ffw_bringup'), 'config', 'ffw_lg2_mini_leader',
            'hand_preset_interpolator.yaml',
        ]),
            'control_profile': 'lg2_mini_sh5_recording'}],
    )

    # Execute process to publish position command
    position_command_process = ExecuteProcess(
        name='trigger_position_command',
        cmd=[
            'ros2', 'topic', 'pub',
            '-r', '50',
            '-t', '50',
            '-p', '50',
            '/leader/trigger_position_controller/commands',
            'std_msgs/msg/Float64MultiArray',
            'data: [0.0, 0.0]',
        ],
    )

    # Note: leader_position_controller commands are now continuously published by
    # joint_trajectory_command_broadcaster (mirrors follower poses every cycle).
    # No initial-kick process needed.

    delay_position_command_after_controllers = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=robot_controller_spawner,
            on_exit=lambda event, context: [position_command_process] if event.returncode == 0
            else [LogInfo(msg='Leader controller startup failed; trigger homing skipped.')],
        )
    )

    # Wrap everything in a namespace 'leader'
    leader_with_namespace = GroupAction(
        actions=[
            PushRosNamespace('leader'),
            control_node,
            robot_controller_spawner,
            robot_state_publisher_node,
            delay_position_command_after_controllers,
            # leader_feedback_node,
            hand_preset_node,
            Node(package='ffw_hand_control', executable='hand_control_bridge',
                 condition=IfCondition(LaunchConfiguration('enable_sh5_recording_controls')),
                 parameters=[{'control_profile': 'lg2_mini_sh5_recording',
                     'left_trajectory_topic': '/leader/sh5_raw/left/joint_trajectory',
                     'right_trajectory_topic': '/leader/sh5_raw/right/joint_trajectory'}], output='screen'),
        ]
    )

    final_pose_node = Node(
        package='ffw_bringup', executable='sh5_final_pose', name='sh5_final_pose',
        parameters=[endpose_config],
        condition=IfCondition(PythonExpression([
            "'", LaunchConfiguration('enable_sh5_recording_controls'), "' == 'true' and '",
            LaunchConfiguration('launch_final_pose'), "' == 'true'"])), output='screen')

    return LaunchDescription(declared_arguments + [
        leader_with_namespace, foot_switch_node, final_pose_node] +
        leader_shutdown_actions(IfCondition(LaunchConfiguration('enable_sh5_recording_controls'))))
