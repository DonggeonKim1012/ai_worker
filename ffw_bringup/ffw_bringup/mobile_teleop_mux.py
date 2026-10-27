"""Opt-in mobile command arbitration: existing leader/navigation commands win."""
import math
import time

ZERO = (0.0, 0.0, 0.0)


class MobilePriority:
    """Use receipt-time deadlines, never replay UI motion after a takeover."""
    def __init__(self, timeout=0.5, release_delay=0.3):
        self.timeout, self.release_delay = timeout, release_delay
        self.primary = self.ui = ZERO
        self.primary_at = self.ui_at = self.last_primary_motion = -math.inf
        self.ui_blocked = False

    def primary_command(self, values, now):
        self.primary_at = now
        if not all(math.isfinite(v) for v in values):
            self.primary = ZERO
            self.last_primary_motion = now
            self.ui_blocked = True
            return
        self.primary = tuple(values)
        if any(abs(v) > 1e-6 for v in values):
            self.last_primary_motion = now
            self.ui_blocked = True

    def ui_command(self, values, now):
        self.ui_at = now
        if not all(math.isfinite(v) for v in values):
            self.ui = ZERO
            self.ui_blocked = True
            return
        self.ui = tuple(values)
        # Release the UI button AFTER the A3 has returned to neutral.
        if self.ui == ZERO and now - self.last_primary_motion >= self.release_delay:
            self.ui_blocked = False

    def output(self, now):
        if self.primary_at != -math.inf and now - self.primary_at > self.timeout:
            # An inactive ros2_control controller can keep its publisher alive.
            # Stop once on lost heartbeat; a held UI command must be released,
            # while an already neutral UI can accept the next deliberate press.
            self.ui_blocked = self.ui != ZERO
            self.primary = ZERO
            self.primary_at = -math.inf
            return ZERO
        if any(abs(v) > 1e-6 for v in self.primary):
            return self.primary
        if now - self.last_primary_motion < self.release_delay:
            return ZERO
        if now - self.ui_at > self.timeout:
            if self.ui != ZERO:
                self.ui_blocked = True
            return ZERO
        return ZERO if self.ui_blocked else self.ui


def main(args=None):
    import fcntl
    import os
    import rclpy
    from rclpy.node import Node
    from rclpy.executors import ExternalShutdownException
    from rclpy._rclpy_pybind11 import RCLError
    from geometry_msgs.msg import Twist

    # A controller-only reload can outlive the follower launch. Keep one mux
    # publisher when the follower is launched again.
    lock = open(f'/tmp/ffw_mobile_teleop_mux_{os.environ.get("ROS_DOMAIN_ID", "0")}.lock', 'a')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        lock.close()
        print('Mobile teleop mux is already running in this domain; reusing it.', flush=True)
        return
    rclpy.init(args=args)
    node = Node('mobile_teleop_mux')
    policy = MobilePriority()
    primary_topic = node.declare_parameter('primary_topic', '/cmd_vel').value
    ui_topic = node.declare_parameter('ui_topic', '/cyclo/mobile_teleop/cmd_vel').value
    output_topic = node.declare_parameter('output_topic', '/ffw/mobile/cmd_vel').value
    if len({primary_topic, ui_topic, output_topic}) != 3:
        raise ValueError('Mobile input/output topics must be distinct')
    publisher = node.create_publisher(Twist, output_topic, 1)
    def values(msg):
        return msg.linear.x, msg.linear.y, msg.angular.z
    node.create_subscription(Twist, primary_topic,
        lambda m: policy.primary_command(values(m), time.monotonic()), 1)
    node.create_subscription(Twist, ui_topic,
        lambda m: policy.ui_command(values(m), time.monotonic()), 1)
    def publish():
        msg = Twist()
        msg.linear.x, msg.linear.y, msg.angular.z = policy.output(time.monotonic())
        publisher.publish(msg)
    node.create_timer(0.02, publish)
    node.get_logger().info('Mobile priority: leader/navigation > UI; UI timeout 0.5s; release UI after takeover')
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        if rclpy.ok():
            publisher.publish(Twist())
        node.destroy_node()
        try:
            rclpy.try_shutdown()
        except RCLError as error:
            # Jazzy SIGINT may shut down the context between ok() and shutdown().
            if 'rcl_shutdown already called' not in str(error):
                raise
        lock.close()
