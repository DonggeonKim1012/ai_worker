"""Independent receiver: keep outside the follower/leader supervisor trees."""
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    config = PathJoinSubstitution([FindPackageShare('ffw_bringup'), 'config',
                                  'ffw_lg2_mini_leader', 'bgf_endpose.yaml'])
    pose = PathJoinSubstitution([FindPackageShare('ffw_bringup'), 'config',
                                'ffw_lg2_mini_leader', 'bgf_waypoint1_endpose.json'])
    return LaunchDescription([
        DeclareLaunchArgument('endpose_file', default_value=pose),
        Node(package='ffw_bringup', executable='sh5_final_pose', name='sh5_final_pose',
             parameters=[config, {'endpose_file': LaunchConfiguration('endpose_file')}],output='screen')])
