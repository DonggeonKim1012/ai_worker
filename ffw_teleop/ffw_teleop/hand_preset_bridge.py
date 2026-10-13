"""Physical SH5 leader preset catalog and trigger interpolation bridge."""
from functools import partial
import json
import math
from pathlib import Path
import time
import xml.etree.ElementTree as ET

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy
from rcl_interfaces.msg import SetParametersResult
from rcl_interfaces.srv import SetParametersAtomically
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray, String, UInt8
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_srvs.srv import SetBool

from ffw_teleop.hand_preset_model import PresetCatalog, normalize_trigger


class HandPresetBridge(Node):
    def __init__(self, **kwargs):
        super().__init__('hand_preset_bridge', **kwargs)
        config_file = self.declare_parameter('config_file', '').value or None
        self.catalog = PresetCatalog(self.declare_parameter(
            'preset_file', str(Path.home() / '.ros' / 'sh5_hand_presets.json')).value, config_file)
        # This bridge receives calibrated [-0.1, 1.1] broadcaster output,
        # not the raw physical trigger angles in the imported YAML.
        self.trigger_min = float(self.declare_parameter('trigger_min', -0.1).value)
        self.trigger_max = float(self.declare_parameter('trigger_max', 1.1).value)
        normalize_trigger(0.0, self.trigger_min, self.trigger_max)
        self.require_teleop_heartbeat = self.declare_parameter(
            'require_teleop_heartbeat', True).value
        self.paused = False
        self.create_service(SetBool, '/leader/hand_preset/pause', self.on_pause)
        self.ready = False
        self.teleop = {'left': (False, 0.0), 'right': (False, 0.0)}
        self.trigger = {'left': 0.0, 'right': 0.0}
        self.endpose = {}
        endpose_file = self.declare_parameter('endpose_file', '').value
        if endpose_file:
            document = json.loads(Path(endpose_file).read_text())
            if document.get('robot_type') != 'ffw_sh5_rev1':
                raise ValueError('End pose must belong to ffw_sh5_rev1')
            for side, letter in (('left', 'l'), ('right', 'r')):
                names = self.catalog.config[f'{side}_joint_names']
                values = [document['joints'][name] for name in names]
                if not all(type(v) in (int, float) and math.isfinite(v) for v in values):
                    raise ValueError('End pose contains invalid hand positions')
                self.endpose[side] = values
        self.measured = {}
        self.save_state = {side: (0, 0.0) for side in ('left', 'right')}
        self.save_motion = {}
        self.save_blocked = set()
        self.create_subscription(JointState, '/joint_states', self.on_measured, 10)
        self.create_subscription(JointState, '/arm_hand/joint_states', self.on_measured, 10)
        self.create_timer(0.02, self.publish_endpose)
        self.pubs = {}
        self.effort_pubs = {}
        self.endpose_effort_ma = {}
        self.teleop_effort_ma = {}
        self.names = {hand: self.catalog.config[f'{hand}_joint_names']
                      for hand in ('left', 'right')}
        for hand in self.names:
            self.create_subscription(UInt8, f'/leader/{hand}_save_pose_state',
                partial(self.on_save_pose, hand), 1)
            self.pubs[hand] = self.create_publisher(JointTrajectory,
                self.catalog.config[f'{hand}_command_topic'], 1)
            effort = float(self.catalog.config[f'{hand}_endpose_effort_command_ma'])
            effort_max = float(self.catalog.config['effort_command_max_ma'])
            if not math.isfinite(effort) or not 0.0 <= effort <= effort_max:
                raise ValueError(f'{hand} end-pose effort must be between 0 and {effort_max} mA')
            self.endpose_effort_ma[hand] = effort
            opened = float(self.catalog.config[f'{hand}_default_effort_command_ma'])
            closed = {str(number): float(self.catalog.config.get(
                f'{hand}_preset_{number}_effort_command_ma', opened))
                for number in self.catalog.config['preset_ids']}
            if any(not math.isfinite(value) or not 0.0 <= value <= effort_max
                   for value in [opened, *closed.values()]):
                raise ValueError(f'{hand} teleop current limits must be between 0 and {effort_max} mA')
            self.teleop_effort_ma[hand] = (opened, closed)
            self.effort_pubs[hand] = self.create_publisher(
                Float64MultiArray, self.catalog.config[f'{hand}_effort_command_topic'], 1)
            self.create_subscription(UInt8, f'/leader/{hand}_teleop_state',
                partial(self.on_teleop, hand), 1)
            self.create_subscription(JointTrajectory,
                f'/leader/joint_trajectory_command_broadcaster_{hand}/joint_trajectory',
                partial(self.on_trajectory, hand), 1)
        self.feedback = self.create_publisher(JointState, '/topic_based_joint_states', 1)
        self.create_subscription(JointState, '/topic_based_joint_commands', self.on_virtual_command, 1)
        latched = QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL)
        self.create_subscription(String, '/robot_description', self.on_description, latched)
        self.status_pub = self.create_publisher(String, '/leader/hand_preset/status', latched)
        for action in ('set', 'custom/save', 'manage/update', 'manage/delete', 'manage/restore'):
            self.create_service(SetParametersAtomically, '/leader/hand_preset/' + action,
                                partial(self.on_service, action))
        self.create_timer(0.5, self.publish_status)
        self.publish_status()

    def on_pause(self, request, response):
        self.paused = request.data
        if self.paused:
            self.save_motion.clear()
        response.success = True
        response.message = 'Preset output paused' if self.paused else 'Preset output resumed'
        return response

    def on_description(self, message):
        try:
            robot = ET.fromstring(message.data)
            limits = {joint.get('name'): joint.find('limit') for joint in robot.findall('joint')}
            for hand, names in self.names.items():
                for index, (name, opened) in enumerate(zip(names, self.catalog.config[f'{hand}_open_pose'])):
                    limit = limits.get(name)
                    if limit is None:
                        raise ValueError(f'Missing SH5 joint limit: {name}')
                    lower, upper = float(limit.get('lower')), float(limit.get('upper'))
                    if not all(math.isfinite(v) for v in (lower, upper)) or not (
                            lower <= opened <= upper and all(
                                lower <= self.catalog.positions(hand, number, amount)[index] <= upper
                                for number in self.catalog.presets for amount in (0.0, 1.0))
                            and (hand not in self.endpose or
                                 lower <= self.endpose[hand][index] <= upper)):
                        raise ValueError(f'Preset exceeds follower limits: {name}')
            self.ready = True
        except (ET.ParseError, ValueError, TypeError) as error:
            self.ready = False
            self.get_logger().error(str(error))

    def on_measured(self, message):
        if len(message.name) != len(message.position) or len(set(message.name)) != len(message.name):
            return
        now = time.monotonic()
        # Keep freshness per joint: unrelated partial snapshots cannot refresh fingers.
        for name, value in zip(message.name, message.position):
            self.measured[name] = (value, now)

    def on_save_pose(self, hand, message):
        now = time.monotonic()
        previous, _ = self.save_state[hand]
        self.save_state[hand] = (message.data, now)
        if message.data != 5:
            self.save_motion.pop(hand, None)
            self.save_blocked.discard(hand)
            return
        if previous == 5 or hand in self.save_blocked:
            return
        if not self.ready or hand not in self.endpose:
            self.save_blocked.add(hand)
            return
        start = []
        for name in self.names[hand]:
            value, received = self.measured.get(name, (math.nan, 0.0))
            if not math.isfinite(value) or now - received > 0.5:
                self.save_blocked.add(hand)
                self.get_logger().error(f'{hand} end pose blocked: missing/stale joint {name}')
                return
            start.append(value)
        target = self.endpose[hand]
        duration = max(2.0, max(1.5 * abs(a-b) / 0.25 for a, b in zip(start, target)))
        self.save_motion[hand] = (now, duration, start)

    def publish_endpose(self):
        if self.paused:
            return
        now = time.monotonic()
        for hand, (started, duration, start) in list(self.save_motion.items()):
            pose_id, received = self.save_state[hand]
            if not self.ready or pose_id != 5 or now - received > 0.5:
                self.save_motion.pop(hand, None)
                self.save_blocked.add(hand)
                continue
            amount = min(1.0, max(0.0, (now-started) / duration))
            blend = amount * amount * (3.0 - 2.0 * amount)
            values = [a + blend * (b-a) for a, b in zip(start, self.endpose[hand])]
            self.pubs[hand].publish(JointTrajectory(joint_names=self.names[hand],
                points=[JointTrajectoryPoint(positions=values)]))
            # The saved finger target needs its own current limit. The normal
            # trigger interpolator is bypassed in save-pose mode, so relying on
            # its last current command can let a grasp back-drive and loosen.
            self.effort_pubs[hand].publish(Float64MultiArray(
                data=[self.endpose_effort_ma[hand]] * len(self.names[hand])))

    def on_teleop(self, hand, message):
        self.teleop[hand] = (message.data == 1, time.monotonic())

    def on_trajectory(self, hand, message):
        enabled, received = self.teleop[hand]
        if (self.paused or not self.ready or (self.require_teleop_heartbeat and
                (not enabled or time.monotonic() - received > 0.5))
                or self.save_state[hand][0] == 5):
            return
        gripper = f"gripper_{'l' if hand == 'left' else 'r'}_joint1"
        if len(set(message.joint_names)) != len(message.joint_names) or gripper not in message.joint_names:
            return
        if not message.points:
            return
        values = message.points[-1].positions
        if len(values) != len(message.joint_names) or not all(math.isfinite(v) for v in values):
            return
        amount = normalize_trigger(values[message.joint_names.index(gripper)], self.trigger_min, self.trigger_max)
        self.trigger[hand] = amount
        output = JointTrajectory(joint_names=self.names[hand])
        point = JointTrajectoryPoint(positions=self.catalog.positions(hand, self.catalog.active[hand], amount))
        # Stream the current target directly. Replacing a 100 ms trajectory at
        # 100 Hz repeatedly interpolates from measured position and adds lag.
        # The follower's existing motor profile still governs physical motion.
        point.time_from_start.nanosec = 0
        output.points = [point]
        # Each control mode must own its current command. Otherwise the
        # saved-pose limit remains latched when normal trigger control resumes.
        preset = self.catalog.presets[self.catalog.active[hand]]
        profile = str(preset.get('pose', self.catalog.template))
        opened, closed = self.teleop_effort_ma[hand]
        effort = opened + amount * (closed[profile] - opened)
        self.effort_pubs[hand].publish(Float64MultiArray(
            data=[effort] * len(self.names[hand])))
        self.pubs[hand].publish(output)

    def on_virtual_command(self, message):
        # Echo the virtual input in its own units. Re-normalizing here creates a feedback drift.
        if len(message.name) != len(message.position) or len(set(message.name)) != len(message.name):
            return
        pairs = [(name, value) for name, value in zip(message.name, message.position)
                 if name in ('gripper_l_joint1', 'gripper_r_joint1')]
        if not pairs or not all(math.isfinite(value) for _, value in pairs):
            return
        output = JointState()
        output.header.stamp = self.get_clock().now().to_msg()
        output.name = [name for name, _ in pairs]
        output.position = [min(self.trigger_max, max(self.trigger_min, value)) for _, value in pairs]
        output.velocity = [0.0] * len(pairs)
        output.effort = [0.0] * len(pairs)
        self.feedback.publish(output)

    def on_service(self, action, request, response):
        try:
            expected = {
                'set': {'side': 4, 'preset_id': 2},
                'custom/save': {'name': 4, 'description': 4, 'curls': 8},
                'manage/update': {'preset_id': 2, 'name': 4, 'description': 4, 'note': 4},
                'manage/delete': {'preset_id': 2}, 'manage/restore': {'preset_id': 2},
            }[action]
            values = {}
            for parameter in request.parameters:
                key, value = parameter.name, parameter.value
                if key in values or key not in expected or value.type != expected[key]:
                    raise ValueError(f'Unexpected or incorrectly typed parameter: {key}')
                values[key] = {2: value.integer_value, 4: value.string_value,
                               8: list(value.double_array_value)}[value.type]
            if action == 'set' and self.catalog.config['require_trigger_release_on_change']:
                side = values.get('side')
                hands = ('left', 'right') if side == 'both' else (side,)
                if any(self.trigger.get(hand, 0.0) >
                       self.catalog.config['preset_change_max_trigger_alpha'] for hand in hands):
                    raise ValueError('Release the trigger before changing presets')
            self.catalog.apply(action, values)
            response.result = SetParametersResult(successful=True, reason='Preset saved/selected')
            self.publish_status()
        except (KeyError, ValueError, TypeError, OSError) as error:
            response.result = SetParametersResult(successful=False, reason=str(error))
        return response

    def publish_status(self):
        payload = self.catalog.status()
        payload['follower_ready'] = self.ready
        payload['trigger_values'] = self.trigger
        payload['teleop_enabled'] = {hand: enabled and time.monotonic() - received <= 0.5
                                    for hand, (enabled, received) in self.teleop.items()}
        self.status_pub.publish(String(data=json.dumps(payload, allow_nan=False)))


def main(args=None):
    rclpy.init(args=args)
    node = HandPresetBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
