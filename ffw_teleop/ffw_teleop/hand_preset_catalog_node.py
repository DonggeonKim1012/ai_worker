"""Studio-only catalog services; high-rate commands are owned by ffw_hand_control."""
import copy
import json
from pathlib import Path
import time

import rclpy
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import ExternalShutdownException
from rclpy._rclpy_pybind11 import RCLError
from rclpy.qos import QoSProfile, DurabilityPolicy
from rcl_interfaces.msg import Parameter, ParameterValue, SetParametersResult
from rcl_interfaces.srv import SetParametersAtomically
from std_msgs.msg import String
from ffw_teleop.hand_preset_model import PresetCatalog


class HandPresetCatalog(Node):
    def __init__(self):
        super().__init__('hand_preset_bridge')  # Preserve the Studio discovery contract.
        self.catalog = PresetCatalog(self.declare_parameter(
            'preset_file', str(Path.home()/'.ros/sh5_hand_presets.json')).value,
            self.declare_parameter('config_file', '').value or None)
        self.profile = self.declare_parameter('control_profile', 'a3_sh5').value
        self.trigger_min = self.declare_parameter('trigger_min', -.1).value
        self.trigger_max = self.declare_parameter('trigger_max', 1.1).value
        self.runtime, self.runtime_received = {}, 0.
        self.synced = False
        self.busy = False
        self.last_error = ''
        self.io_group = ReentrantCallbackGroup()
        self.client = self.create_client(SetParametersAtomically, '/leader/hand_control/apply',
                                         callback_group=self.io_group)
        latched = QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL)
        self.create_subscription(String, '/leader/hand_control/status', self.on_runtime, latched)
        self.status_pub = self.create_publisher(String, '/leader/hand_preset/status', latched)
        for action in ('set', 'custom/save', 'manage/update', 'manage/delete', 'manage/restore'):
            # An async callback allows the executor to receive the C++ response.
            async def callback(request, response, selected=action):
                return await self.on_service(selected, request, response)
            self.create_service(SetParametersAtomically, '/leader/hand_preset/'+action, callback)
        self.create_timer(.5, self.tick)

    def on_runtime(self, msg):
        try:
            value = json.loads(msg.data)
            if value.get('control_profile') != self.profile:
                return
            self.runtime, self.runtime_received = value, time.monotonic()
            if not value.get('configured'):
                self.synced = False
        except (ValueError, AttributeError):
            pass

    def config_request(self):
        c = self.catalog.config
        document = dict(schema=1, profile=self.profile, trigger_min=self.trigger_min,
            trigger_max=self.trigger_max, deadband=c['trigger_open_deadband_alpha'],
            change_limit=c['preset_change_max_trigger_alpha'])
        for side, number in self.catalog.active.items():
            profile = self.catalog.presets[number]['pose']
            opened_current = c[f'{side}_default_effort_command_ma']
            document[side] = dict(names=c[f'{side}_joint_names'],
                open=self.catalog.positions(side, number, 0.),
                closed=self.catalog.positions(side, number, 1.),
                open_current=opened_current,
                closed_current=c.get(f'{side}_preset_{profile}_effort_command_ma', opened_current),
                raw_open=c[f'{side}_trigger_open'], raw_closed=c[f'{side}_trigger_closed'])
        return SetParametersAtomically.Request(parameters=[Parameter(name='config',
            value=ParameterValue(type=4, string_value=json.dumps(document, allow_nan=False)))])

    async def sync(self):
        if not self.client.service_is_ready():
            raise RuntimeError('C++ hand controller is unavailable')
        future = self.client.call_async(self.config_request())
        timer = self.create_timer(3., lambda: future.cancel() if not future.done() else None,
                                  callback_group=self.io_group)
        try:
            result = await future
            if result is None:
                raise RuntimeError('C++ hand controller acknowledgement timed out')
            if not result.result.successful:
                raise RuntimeError(result.result.reason)
            self.synced = True
        finally:
            self.destroy_timer(timer)

    async def tick(self):
        if not self.synced and not self.busy and self.client.service_is_ready():
            self.busy = True
            try:
                await self.sync()
                self.last_error = ''
            except Exception as error:
                self.last_error = str(error)
            finally:
                self.busy = False
        payload = self.catalog.status()
        fresh = time.monotonic()-self.runtime_received < 1.5
        payload.update(control_profile=self.profile,
            follower_ready=fresh and self.synced and self.runtime.get('follower_ready', False),
            trigger_values=self.runtime.get('trigger_values', {'left': 0., 'right': 0.}),
            teleop_enabled=self.runtime.get('teleop_enabled', {}) if fresh else {'left': False, 'right': False},
            control_backend='cpp', control_error=self.last_error)
        self.status_pub.publish(String(data=json.dumps(payload, allow_nan=False)))

    async def on_service(self, action, request, response):
        if self.busy:
            response.result = SetParametersResult(successful=False, reason='Catalog update already running; retry')
            return response
        self.busy = True
        previous = copy.deepcopy((self.catalog.presets, self.catalog.active, self.catalog.deleted))
        try:
            expected = {'set': {'side': 4, 'preset_id': 2},
                'custom/save': {'name': 4, 'description': 4, 'curls': 8},
                'manage/update': {'preset_id': 2, 'name': 4, 'description': 4, 'note': 4},
                'manage/delete': {'preset_id': 2}, 'manage/restore': {'preset_id': 2}}[action]
            values = {}
            for parameter in request.parameters:
                key, value = parameter.name, parameter.value
                if key in values or key not in expected or value.type != expected[key]:
                    raise ValueError(f'Unexpected or incorrectly typed parameter: {key}')
                values[key] = {2: value.integer_value, 4: value.string_value,
                              8: list(value.double_array_value)}[value.type]
            # C++ also checks fresh release state atomically before changing targets.
            self.catalog.apply(action, values)
            await self.sync()
            self.last_error = ''
            response.result = SetParametersResult(successful=True, reason='Catalog saved and C++ controller acknowledged')
        except Exception as error:
            self.catalog.presets, self.catalog.active, self.catalog.deleted = previous
            self.last_error = str(error)
            try:
                if action != 'set':
                    self.catalog.persist()
            except OSError as storage_error:
                self.last_error += f'; rollback persistence failed: {storage_error}'
            # A lost acknowledgement leaves acceptance uncertain: do not report ready.
            self.synced = False
            response.result = SetParametersResult(successful=False, reason=self.last_error)
        finally:
            self.busy = False
        return response


def main(args=None):
    rclpy.init(args=args)
    node = HandPresetCatalog()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        try:
            rclpy.try_shutdown()
        except RCLError as error:
            # Jazzy's signal handler can shut the context down between the
            # internal ok() check and shutdown(). Do not mask other failures.
            if 'rcl_shutdown already called' not in str(error):
                raise
