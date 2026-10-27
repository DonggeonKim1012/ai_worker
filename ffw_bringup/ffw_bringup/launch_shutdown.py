"""Explicit completion signal between a ROS service node and its own launch."""
from launch.actions import EmitEvent, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.events import Shutdown
from launch_ros.actions import Node

SHUTDOWN_EXIT_CODE = 42


def shutdown_when_requested(node):
    return RegisterEventHandler(OnProcessExit(
        target_action=node,
        on_exit=lambda event, context: [EmitEvent(event=Shutdown(
            reason='SH5 bringdown completed'))]
        if event.returncode == SHUTDOWN_EXIT_CODE else []))


def leader_shutdown_actions(condition):
    node = Node(package='ffw_bringup', executable='launch_stop_receiver',
                name='leader_launch_stop', condition=condition,
                parameters=[{'service_name': '/leader/shutdown'}], output='screen')
    return [node, shutdown_when_requested(node)]
