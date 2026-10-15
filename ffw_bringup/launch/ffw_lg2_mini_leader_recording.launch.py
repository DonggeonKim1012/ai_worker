"""Opt-in LG2 mini + SH5 profile; other leader/follower launches are unchanged."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    leader_launch = PathJoinSubstitution([
        FindPackageShare('ffw_bringup'), 'launch', 'ffw_lg2_mini_leader_ai.launch.py'])
    return LaunchDescription([
        DeclareLaunchArgument('launch_final_pose', default_value='false'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(leader_launch),
            launch_arguments={
                'enable_sh5_recording_controls': 'true',
                'follower_type': 'ffw_sh5_rev1',
                'launch_final_pose': LaunchConfiguration('launch_final_pose'),
                'task_controller_config': 'lg2_recording_controls.yaml',
            }.items(),
        ),
    ])
