"""Standalone hand preset bridge for the SH5 follower."""
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    config = PathJoinSubstitution([FindPackageShare('ffw_bringup'), 'config',
                                  'ffw_lg2_mini_leader', 'hand_preset_interpolator.yaml'])
    return LaunchDescription([
        DeclareLaunchArgument('config_file', default_value=config),
        DeclareLaunchArgument('preset_file', default_value='/workspace/hand_presets/sh5_hand_presets.json'),
        DeclareLaunchArgument('endpose_file', default_value=''),
        DeclareLaunchArgument('require_teleop_heartbeat', default_value='true'),
        DeclareLaunchArgument('trigger_min', default_value='-0.1'),
        DeclareLaunchArgument('trigger_max', default_value='1.1'),
        Node(package='ffw_teleop', executable='hand_preset_bridge', name='hand_preset_bridge',
             parameters=[{'require_teleop_heartbeat': ParameterValue(
                 LaunchConfiguration('require_teleop_heartbeat'), value_type=bool)}, {name: LaunchConfiguration(name) for name in
                          ('config_file', 'preset_file', 'endpose_file')},
                         {name: ParameterValue(LaunchConfiguration(name), value_type=float)
                          for name in ('trigger_min', 'trigger_max')}],
             output='screen'),
    ])
