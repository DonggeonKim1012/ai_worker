"""Publish the explicit leader task; does not issue motion commands."""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


def main(args=None):
    rclpy.init(args=args)
    node = Node('task_selection')
    task = node.declare_parameter('task_name', '').value
    if not task or not task.replace('_', '').isalnum():
        raise ValueError('task_name must be a valid task identifier')
    publisher = node.create_publisher(String, '/leader/task_name', 1)
    node.create_timer(.25, lambda: publisher.publish(String(data=task)))
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
