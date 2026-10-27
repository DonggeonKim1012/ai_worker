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

from pathlib import Path
import yaml
import tempfile
import atexit
import subprocess
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, OpaqueFunction
from launch.conditions import IfCondition
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch_ros.actions import Node, PushRosNamespace
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue
from ffw_bringup.launch_shutdown import leader_shutdown_actions


def generate_launch_description():
    declared_arguments = [
        DeclareLaunchArgument('task_name', default_value='',
                              description='Optional task override; empty reads /ffw/task_name from the running follower.'),
        DeclareLaunchArgument('robot_type', default_value='default',
                              choices=['default', 'sh5', 'ffw_sh5_rev1'],
                              description='Explicit SH5 follower selection enables 8 -> 7+20 command conversion.'),
        DeclareLaunchArgument('port_name',
                              default_value='/dev/serial/by-id/usb-ROBOTIS_Avatar_Controller_315738613434-if00',
                              description='Serial port of the single A3 controller board.'),
        DeclareLaunchArgument('hand_trigger_open', default_value='-0.1',
                              description='Open endpoint of the calibrated A3 gripper command.'),
        DeclareLaunchArgument('hand_trigger_closed', default_value='1.1',
                              description='Closed endpoint of the calibrated A3 gripper command.'),
        DeclareLaunchArgument(
            'description_file',
            default_value='ffw_a3.urdf.xacro',
            description='URDF/XACRO file for the robot model.',
        ),
        DeclareLaunchArgument(
            'use_mock_hardware',
            default_value='false',
            description='Use mock hardware mirroring command.',
        ),
        DeclareLaunchArgument(
            'launch_foot_switch',
            default_value='true',
            description='Whether to launch the foot switch node.',
        ),
    ]

    description_file = LaunchConfiguration('description_file')
    use_mock_hardware = LaunchConfiguration('use_mock_hardware')
    launch_foot_switch = LaunchConfiguration('launch_foot_switch')
    sh5 = PythonExpression(["'", LaunchConfiguration('robot_type'), "' in ('sh5', 'ffw_sh5_rev1')"])

    # Robot controllers config file path
    robot_controllers = PathJoinSubstitution(
        [
            FindPackageShare('ffw_bringup'),
            'config',
            'ffw_a3',
            'ffw_a3_ai_hardware_controller.yaml',
        ]
    )

    def resolve_task_name(context):
        explicit = LaunchConfiguration('task_name').perform(context).strip()
        if explicit:
            return explicit
        if LaunchConfiguration('robot_type').perform(context) not in ('sh5', 'ffw_sh5_rev1'):
            return ''
        try:
            result = subprocess.run(
                ['ros2', 'topic', 'echo', '/ffw/task_name', 'std_msgs/msg/String',
                 '--once', '--field', 'data'],
                check=True, capture_output=True, text=True, timeout=4.0)
            return result.stdout.strip().splitlines()[0]
        except (subprocess.SubprocessError, IndexError):
            return ''

    def load_task_config(task_name):
        if not task_name or not task_name.replace('_', '').isalnum():
            return None
        path = Path(get_package_share_directory('ffw_bringup')) / 'config/tasks' / f'{task_name}.yaml'
        if not path.is_file():
            return None
        document = yaml.safe_load(path.read_text()) or {}
        return document if isinstance(document, dict) else None

    # ros2_control Node
    def make_control_node(context):
        parameters = [robot_controllers]
        task_name = resolve_task_name(context)
        task = load_task_config(task_name)
        if LaunchConfiguration('robot_type').perform(context) in ('sh5', 'ffw_sh5_rev1'):
            parameters.append(PathJoinSubstitution([FindPackageShare('ffw_bringup'),
                'config', 'common', 'sh5_task_joystick.yaml']))
        task_configured = (LaunchConfiguration('robot_type').perform(context) in ('sh5', 'ffw_sh5_rev1')
                           and task is not None and isinstance(task.get('a3_joystick'), dict))
        if task_configured:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as config:
                yaml.safe_dump({'/**': {'joystick_controller': {
                    'ros__parameters': task['a3_joystick']},
                    'joint_trajectory_command_broadcaster': {'ros__parameters': {
                        'leader_blend_duration': task.get('teleop_resume', {}).get('duration', 0.0)}}}}, config)
                parameters.append(config.name)
            atexit.register(lambda: Path(config.name).unlink(missing_ok=True))
        nodes = [Node(package='controller_manager', executable='ros2_control_node',
                      parameters=parameters, output='both')]
        if task_configured:
            nodes.append(Node(package='ffw_bringup', executable='task_selection',
                parameters=[{'task_name': task_name}], output='screen'))
        return nodes
    control_node = OpaqueFunction(function=make_control_node)

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name='xacro')]),
            ' ',
            PathJoinSubstitution(
                [FindPackageShare('ffw_description'), 'urdf', 'ffw_a3', description_file]
            ),
            ' ',
            'use_mock_hardware:=', use_mock_hardware,
            ' ', 'port_name:=', LaunchConfiguration('port_name'),
        ]
    )
    robot_description = {'robot_description': ParameterValue(robot_description_content, value_type=str)}

    def spawn_controllers(context):
        arguments = [
            'joint_trajectory_command_broadcaster',
            'spring_actuator_controller',
            'joystick_controller',
            'joint_state_broadcaster',
        ]
        if LaunchConfiguration('robot_type').perform(context) in ('sh5', 'ffw_sh5_rev1'):
            for side in ('left', 'right'):
                arguments += ['--controller-ros-args',
                    f'-r /leader/joint_trajectory_command_broadcaster_{side}/joint_trajectory:='
                    f'/leader/a3/{side}/joint_trajectory']
        return [Node(package='controller_manager', executable='spawner',
                     arguments=arguments, parameters=[robot_description])]

    robot_controller_spawner = OpaqueFunction(function=spawn_controllers)

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

    gripper_trigger_node = Node(
        package='ffw_joint_trajectory_command_broadcaster',
        executable='gripper_trigger',
        name='gripper_trigger',
        output='both',
        parameters=[{'gripper_threshold': -0.5}],
    )

    # Wrap everything in a namespace 'leader'
    leader_with_namespace = GroupAction(
        actions=[
            PushRosNamespace('leader'),
            control_node,
            robot_controller_spawner,
            robot_state_publisher_node,
            gripper_trigger_node,
        ]
    )

    hand_bridge = Node(
        package='ffw_teleop', executable='hand_preset_catalog',
        namespace='leader', name='hand_preset_bridge', output='screen',
        condition=IfCondition(sh5), parameters=[{
            'control_profile': 'a3_sh5',
            'config_file': PathJoinSubstitution([FindPackageShare('ffw_bringup'),
                'config', 'ffw_lg2_mini_leader', 'hand_preset_interpolator.yaml']),
            'trigger_min': ParameterValue(LaunchConfiguration('hand_trigger_open'), value_type=float),
            'trigger_max': ParameterValue(LaunchConfiguration('hand_trigger_closed'), value_type=float),
        }])

    def make_hand_control(context):
        task = load_task_config(resolve_task_name(context))
        resume_duration = (task or {}).get('teleop_resume', {}).get('duration', 0.0)
        return [Node(package='ffw_hand_control', executable='hand_control_bridge',
            namespace='leader', condition=IfCondition(sh5), output='screen',
            parameters=[{'control_profile': 'a3_sh5',
                'resume_blend_duration': float(resume_duration)}])]

    hand_control = OpaqueFunction(function=make_hand_control)
    return LaunchDescription(declared_arguments + [leader_with_namespace, foot_switch_node,
        hand_bridge, hand_control] + leader_shutdown_actions(IfCondition(sh5)))
