"""Stop this launch only after an explicit shutdown request."""
import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

from ffw_bringup.launch_shutdown import SHUTDOWN_EXIT_CODE


def main(args=None):
    rclpy.init(args=args)
    node = Node('leader_launch_stop')
    requested = False

    def request_stop(request, response):
        nonlocal requested
        requested = True
        response.success = True
        response.message = 'Leader launch shutdown accepted'
        return response

    name = node.declare_parameter('service_name', '/leader/shutdown').value
    node.create_service(Trigger, name, request_stop)
    try:
        while rclpy.ok() and not requested:
            rclpy.spin_once(node, timeout_sec=.1)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
    if requested:
        raise SystemExit(SHUTDOWN_EXIT_CODE)
