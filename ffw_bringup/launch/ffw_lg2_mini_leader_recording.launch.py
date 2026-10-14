"""LG2 mini leader with task-specific short/long joystick gestures."""

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    leader_launch = PathJoinSubstitution([
        FindPackageShare('ffw_bringup'), 'launch', 'ffw_lg2_mini_leader_ai.launch.py'])
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(leader_launch),
            launch_arguments={
                'task_controller_config': 'lg2_recording_controls.yaml',
            }.items(),
        ),
    ])
