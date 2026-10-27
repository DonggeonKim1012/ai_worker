"""SH5 UI jog routing without competing with the leader's idle hold stream."""
import math
import time

LEADER_JOYSTICK_TOPIC = '/leader/joystick_controller/sensorxel_joy_values'


def leader_input_stale(last_activity, now, publisher_count):
    # A stopped leader cannot keep a later UI session locked out forever.
    return last_activity != -math.inf and now-last_activity > .5 and publisher_count > 0


def jog_step_within_limit(group, name, target, measured):
    # UI head steps reach 0.1 rad; allow its 0.015 rad feedback tolerance plus rounding.
    max_step = .051 if group == 'lift' else (.301 if name == 'head_joint2' else .116)
    return abs(target-measured) <= max_step


def jog_target_within_limits(group, target, measured, lower, upper):
    if lower <= target <= upper:
        return True
    if group != 'head':
        return False
    # A leader can leave the head outside the UI's narrower range. Permit a
    # short inward recovery step or a hold on that joint, never an outward jog.
    return ((measured > upper and upper <= target <= measured + .015)
            or (measured < lower and measured - .015 <= target <= lower))


class JointPriority:
    def __init__(self):
        self.previous = None
        self.changed_at = self.active_at = -math.inf
        self.last_primary_at = -math.inf
        self.ui_owned = False

    def activity(self, active, now):
        if active:
            self.active_at = now

    def primary(self, positions, now):
        # A mission may resend the same pose after an intervening UI jog.
        # Treat the first command after a quiet primary stream as new input;
        # keep ignoring an uninterrupted leader idle-hold stream while UI owns.
        resumed = now - self.last_primary_at > 0.5
        self.last_primary_at = now
        changed = resumed or self.previous is None or any(
            abs(a-b) > 1e-6 for a, b in zip(positions, self.previous))
        self.previous = tuple(positions)
        if changed:
            self.changed_at = now
        if changed or now - self.active_at < 0.3:
            self.ui_owned = False
        return not self.ui_owned

    def request_ui(self, now):
        if now - max(self.changed_at, self.active_at) < 0.3:
            return False
        self.ui_owned = True
        return True


def main(args=None):
    import copy
    import fcntl
    import os
    import rclpy
    from rclpy.node import Node
    from rclpy.executors import ExternalShutdownException
    from rclpy._rclpy_pybind11 import RCLError
    from sensor_msgs.msg import JointState
    from nav_msgs.msg import Odometry
    from std_msgs.msg import Float64MultiArray
    from trajectory_msgs.msg import JointTrajectory

    # A controller-only reload may start this outside the follower launch.
    # Reuse that instance on a later launch, never create competing publishers.
    lock = open(f'/tmp/ffw_upper_body_mux_{os.environ.get("ROS_DOMAIN_ID", "0")}.lock', 'a')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        lock.close()
        print('Upper body mux is already running in this domain; reusing it.', flush=True)
        return
    rclpy.init(args=args)
    node = Node('upper_body_teleop_mux')
    groups = {'head': ('head_joint1', 'head_joint2'), 'lift': ('lift_joint',)}
    limits = {'head_joint1': (-.2267, .6901), 'head_joint2': (-.3, .3), 'lift_joint': (-.5, 0.)}
    policy = {g: JointPriority() for g in groups}
    states = {}
    base = {'at': -math.inf, 'stopped': False}
    activity_at = [-math.inf]
    primary_at = {g: -math.inf for g in groups}
    publishers = {g: node.create_publisher(JointTrajectory, f'/ffw/ui_priority/{g}/joint_trajectory', 1)
                  for g in groups}

    def joint_state(msg):
        now = time.monotonic()
        for name, value in zip(msg.name, msg.position):
            if name in limits and math.isfinite(value):
                states[name] = (value, now)

    def odom(msg):
        v = msg.twist.twist
        base['at'] = time.monotonic()
        base['stopped'] = (all(math.isfinite(x) for x in (v.linear.x, v.linear.y, v.angular.z))
                           and math.hypot(v.linear.x, v.linear.y) <= .015 and abs(v.angular.z) <= .03)

    def activity(msg):
        if len(msg.data) != 6 or not all(math.isfinite(v) for v in msg.data):
            return
        now = time.monotonic()
        activity_at[0] = now
        policy['head'].activity(any(abs(v) > 1e-6 for v in msg.data[:2]), now)
        policy['lift'].activity(any(abs(v) > 1e-6 for v in msg.data[3:5]), now)

    def positions(group, msg):
        if tuple(msg.joint_names) != groups[group] or len(msg.points) != 1:
            raise ValueError('Unexpected joints or waypoint count')
        values = msg.points[0].positions
        if len(values) != len(groups[group]) or not all(math.isfinite(v) for v in values):
            raise ValueError('Invalid joint positions')
        return values

    def primary(group, msg):
        if msg.header.frame_id == 'ffw_recording_hold':
            return
        try:
            values = positions(group, msg)
        except ValueError:
            # Invalid primary input must never allow UI to take over silently.
            policy[group].activity(True, time.monotonic())
            return
        now = time.monotonic()
        primary_at[group] = now
        if policy[group].primary(values, now):
            publishers[group].publish(msg)

    def ui(group, msg):
        now = time.monotonic()
        try:
            values = positions(group, msg)
            if now-base['at'] > .5 or not base['stopped']:
                raise ValueError('Base must have fresh, stationary odometry')
            # Task-specific leaders may publish bounded targets only while jogging.
            # Use the joystick heartbeat, not an idle trajectory, for liveness.
            # Startup executors also publish on the legacy leader trajectory
            # topics. A trajectory alone does not prove that a leader exists.
            # A live leader with missing heartbeat is unsafe. A disconnected
            # leader has no input to compete with UI jogging.
            if leader_input_stale(activity_at[0], now, node.count_publishers(LEADER_JOYSTICK_TOPIC)):
                raise ValueError('Leader input is stale')
            for name, value in zip(groups[group], values):
                low, high = limits[name]
                if name not in states or now-states[name][1] > .5:
                    raise ValueError('Joint feedback is stale')
                measured = states[name][0]
                if not jog_target_within_limits(group, value, measured, low, high):
                    raise ValueError(f'Target outside SH5 jog limits: {name} target={value:.3f}, measured={measured:.3f}')
                if not jog_step_within_limit(group, name, value, measured):
                    raise ValueError(f'Jog step too large: {name} target={value:.3f}, measured={measured:.3f}')
            point = msg.points[0]
            seconds = point.time_from_start.sec + point.time_from_start.nanosec / 1e9
            if not .2 <= seconds <= 2 or any((point.velocities, point.accelerations, point.effort)):
                raise ValueError('Expected a short position-only UI jog')
            if not policy[group].request_ui(now):
                raise ValueError('A3 input has priority; return leader to neutral and retry')
            command = copy.deepcopy(msg)
            command.header.stamp.sec = command.header.stamp.nanosec = 0
            speed = .05 if group == 'lift' else .2
            seconds = max(seconds, max(abs(v-states[n][0])/speed for n,v in zip(groups[group],values)))
            command.points[0].time_from_start.sec = int(seconds)
            command.points[0].time_from_start.nanosec = int((seconds-int(seconds))*1e9)
            publishers[group].publish(command)
            node.get_logger().info(f'UI {group} jog accepted; A3 retains priority')
        except ValueError as error:
            node.get_logger().warning(f'UI {group} jog rejected: {error}')

    node.create_subscription(JointState, '/joint_states', joint_state, 10)
    node.create_subscription(Odometry, '/odom', odom, 1)
    node.create_subscription(Float64MultiArray, LEADER_JOYSTICK_TOPIC, activity, 1)
    for group, side in (('head', 'left'), ('lift', 'right')):
        node.create_subscription(JointTrajectory, f'/leader/joystick_controller_{side}/joint_trajectory',
                                 lambda m, g=group: primary(g,m), 1)
        node.create_subscription(JointTrajectory, f'/cyclo/upper_body/{group}/joint_trajectory',
                                 lambda m, g=group: ui(g,m), 1)
    node.get_logger().info('Upper body UI jog ready: A3 activity/changed targets have priority over UI')
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        try:
            rclpy.try_shutdown()
        except RCLError as error:
            if 'rcl_shutdown already called' not in str(error):
                raise
