"""Measured, action-based SH5 bringdown and final-pose receiver."""
import fcntl
import json
import math
import os
from pathlib import Path
import subprocess
import threading
import time
import xml.etree.ElementTree as ET

from ament_index_python.packages import get_package_share_directory
from action_msgs.msg import GoalStatus
from builtin_interfaces.msg import Duration
from control_msgs.action import FollowJointTrajectory
from control_msgs.msg import JointTolerance
from controller_manager_msgs.srv import ListControllers, SwitchController
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy
from sensor_msgs.msg import JointState
from std_msgs.msg import Bool, Float64MultiArray, String
from std_srvs.srv import Trigger, SetBool
from trajectory_msgs.msg import JointTrajectoryPoint
from ffw_bringup.bringdown_plan import GROUPS, OutwardGesture, load_plan, load_task_final_pose, motion_duration, quintic_samples
from ffw_bringup.launch_shutdown import SHUTDOWN_EXIT_CODE
from ffw_bringup.follower_task_state import reverse_arm_plan


def duration_message(value):
    return Duration(sec=int(value), nanosec=int((value % 1)*1e9))


class SH5Bringdown(Node):
    def __init__(self, **kwargs):
        super().__init__('sh5_final_pose', **kwargs)
        base = Path(get_package_share_directory('ffw_bringup')) / 'config'
        def param(name, default):
            return self.declare_parameter(name, default).value
        self.receiver_lock = open(
            f'/tmp/sh5-receiver-{os.getuid()}-{os.environ.get("ROS_DOMAIN_ID", "0")}.lock', 'a+')
        try:
            fcntl.flock(self.receiver_lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            self.receiver_lock.close()
            raise RuntimeError('An SH5 final-pose/bringdown receiver is already running')
        self.exit_deadline = None
        self.leader_profile = ''
        self.leader_profile_received = 0.
        self.groups, self.phases = load_plan(param('config_dir', str(base/'ffw_sh5_rev1_follower')),
            param('endpose_file', str(base/'ffw_lg2_mini_leader/bgf_waypoint1_endpose.json')))
        self.require_init_profile = param('require_init_profile', False)
        self.init_profile_key = None
        self.init_profile_pending = None
        self.follower_task_name = ''
        self.bringdown_control_hands = param('bringdown_control_hands', False)
        if not self.bringdown_control_hands:
            # Do not command defective fingers and then merely ignore their errors.
            # Bringdown moves/verifies arms only; task final poses remain independent.
            self.phases = [(name, {g: values for g, values in targets.items()
                                  if g.startswith('arm_')}) for name, targets in self.phases]
        self.bringdown_groups = set().union(*(targets.keys() for _, targets in self.phases))
        self.task_name = param('task_name', '')
        tasks_dir = param('tasks_dir', str(base/'tasks'))
        try:
            self.final_targets, task_gesture = load_task_final_pose(
                self.task_name, tasks_dir, self.groups)
        except FileNotFoundError as error:
            # An unconfigured task disables task motion, never basic bringdown.
            # Missing files referenced by an existing task remain fatal.
            expected = (Path(tasks_dir).resolve() / (self.task_name + '.yaml'))
            if Path(error.filename) != expected:
                raise
            self.final_targets, task_gesture = None, None
            self.get_logger().error(
                f'Task final pose disabled: missing {expected}. Basic bringdown remains available.')
        self.tasks_dir = tasks_dir
        self.launch_task_name = self.task_name
        self.leader_task_received = 0.
        self.description_message = None
        self.hand_timeout = float(param('hand_confirm_timeout', 60.))
        self.arm_timeout = float(param('arm_confirm_timeout', 20.))
        self.speed = float(param('max_joint_speed', .25))
        self.effort = float(param('hand_effort_ma', 600.))
        if any(not math.isfinite(v) or v <= 0 for v in (self.hand_timeout, self.arm_timeout, self.speed)) or not 0 <= self.effort <= 910:
            raise ValueError('Invalid motion timeout, speed or current')
        self.gesture = OutwardGesture(param('left_axis_index', 1), param('right_axis_index', 4),
            param('left_axis_sign', 1.), param('right_axis_sign', 1.),
            param('gesture_threshold', .7), param('neutral_threshold', .2), param('gesture_hold_sec', .3))
        if task_gesture:
            self.gesture = OutwardGesture(task_gesture['left_axis_index'], task_gesture['right_axis_index'],
                task_gesture['left_axis_sign'], task_gesture['right_axis_sign'],
                task_gesture['gesture_threshold'], task_gesture['neutral_threshold'], task_gesture['gesture_hold_sec'])
        self.supervisor_services = list(param('shutdown_services', ['ai_worker_navigation', 'ai_worker_bringup', 'avatar_bringup']))
        self.shutdown_mode = param('shutdown_mode', 's6')
        if self.shutdown_mode == 'auto':
            self.shutdown_mode = 's6' if Path('/run/service/ai_worker_bringup').is_dir() else 'launch'
        if self.shutdown_mode not in ('s6', 'launch'):
            raise ValueError('shutdown_mode must be s6, launch or auto')
        self.leader_required = param('require_leader_manager', True)
        self.states, self.limits = {}, {}
        self.lock = threading.Lock()
        self.worker = None
        self.stop = threading.Event()
        self.handles = []
        self.motion_clients = {g: ActionClient(self, FollowJointTrajectory, p['topic']) for g,p in self.groups.items()}
        self.managers = {}
        for manager in ('/leader/controller_manager', '/controller_manager'):
            self.managers[manager] = (self.create_client(ListControllers, manager+'/list_controllers'),
                                      self.create_client(SwitchController, manager+'/switch_controller'))
        self.effort_pubs = {g: self.create_publisher(Float64MultiArray, f'/effort_{g[-1]}_controller/commands', 1)
                            for g in ('hand_l', 'hand_r')}
        self.preset_pause = self.create_client(SetBool, '/leader/hand_preset/pause')
        self.leader_shutdown = self.create_client(Trigger, '/leader/shutdown')
        self.side_pause = {s: self.create_client(SetBool, f'/leader/hand_control/{s}/pause')
                           for s in ('left', 'right')}
        self.side_resume = {s: self.create_client(SetBool, f'/leader/hand_control/{s}/allow_resume')
                            for s in ('left', 'right')}
        self.task_enabled = self.create_publisher(Bool, '/ffw/final_pose/enabled',
            QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL))
        self.create_timer(.5, lambda: self.task_enabled.publish(Bool(data=self.final_targets is not None)))
        self.status = self.create_publisher(String, '/ffw/bringdown/status',
            QoSProfile(depth=10, durability=DurabilityPolicy.TRANSIENT_LOCAL))
        self.create_subscription(JointState, '/joint_states', self.on_state, 10)
        self.create_subscription(JointState, '/arm_hand/joint_states', self.on_state, 10)
        self.create_subscription(String, '/robot_description', self.on_description,
            QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL))
        self.create_subscription(Float64MultiArray, '/leader/joystick_controller/final_pose_axes', self.on_joystick, 1)
        self.create_subscription(String, '/leader/hand_preset/status', self.on_leader_profile,
            QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL))
        self.create_service(Trigger, '/ffw/bringdown', self.on_bringdown)
        self.create_service(Trigger, '/ffw/final_pose', self.on_final_pose)
        self.create_subscription(String, '/ffw/init_profile', self.on_init_profile,
            QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL))
        self.create_timer(.2, self.apply_pending_init_profile)
        self.create_subscription(String, '/leader/task_name', self.on_task_selection, 1)
        self.create_timer(.5, self.expire_task_selection)
        self.report('ready', 'Waiting for measured follower state and requests')

    def report(self, state, detail):
        self.status.publish(String(data=json.dumps(dict(state=state, detail=detail))))
        self.get_logger().info(f'{state}: {detail}')

    def on_state(self, msg):
        if len(msg.name) != len(msg.position) or len(set(msg.name)) != len(msg.name):
            return
        now = time.monotonic()
        with self.lock:
            for name,value in zip(msg.name,msg.position):
                self.states[name] = (value,now)

    def on_description(self, msg):
        self.description_message = msg
        try:
            limits = {}
            for joint in ET.fromstring(msg.data).findall('joint'):
                limit = joint.find('limit')
                if limit is not None and 'lower' in limit.attrib:
                    limits[joint.get('name')] = (float(limit.get('lower')),float(limit.get('upper')))
            validation_phases = self.phases + ([('task_final_pose', self.final_targets)] if self.final_targets else [])
            for _, phase in validation_phases:
                for group, values in phase.items():
                    for name,value in zip(self.groups[group]['names'],values):
                        low,high = limits[name]
                        if not all(math.isfinite(v) for v in (low,high,value)) or not low <= value <= high:
                            raise ValueError(f'Waypoint exceeds joint limits: {name}')
            self.limits = limits
        except (ET.ParseError, KeyError, TypeError, ValueError) as error:
            self.limits = {}
            self.report('invalid_description', str(error))

    def snapshot(self, groups=None):
        if not self.limits:
            raise RuntimeError('Follower description/waypoint limits not validated')
        with self.lock:
            states = dict(self.states)
        result = {}
        now = time.monotonic()
        for group, info in self.groups.items():
            if groups is not None and group not in groups:
                continue
            result[group] = []
            for name in info['names']:
                value, stamp = states.get(name, (math.nan,0.))
                if not math.isfinite(value) or now-stamp > .5:
                    raise RuntimeError(f'Missing/stale measured joint: {name}')
                result[group].append(value)
        return result

    def on_init_profile(self, msg):
        try:
            message = json.loads(msg.data)
            key = (message['task_name'], message['profile_sha256'])
            if key == self.init_profile_key:
                return
            phases = reverse_arm_plan(message, self.groups)
            # Explicit hand-enabled legacy configurations retain their old path.
            if self.bringdown_control_hands:
                return
            self.init_profile_pending = (key, phases)
            self.apply_pending_init_profile()
        except (ValueError, KeyError, TypeError) as error:
            self.report('invalid_init_profile', str(error))

    def apply_pending_init_profile(self):
        if self.init_profile_pending is None or (self.worker and self.worker.is_alive()):
            return
        key, phases = self.init_profile_pending
        self.phases = phases
        self.bringdown_groups = {'arm_l', 'arm_r'}
        self.init_profile_key = key
        self.follower_task_name = key[0]
        self.init_profile_pending = None
        self.limits = {}
        if self.description_message is not None:
            self.on_description(self.description_message)
        self.report('init_profile_selected',
            f'Follower task={key[0] or "default"}; reverse path=' + ', '.join(name for name, _ in phases))

    def select_task(self, name):
        if self.worker is not None and self.worker.is_alive():
            return False
        try:
            targets, gesture = load_task_final_pose(name, self.tasks_dir, self.groups)
        except (OSError, ValueError, KeyError, TypeError) as error:
            self.report('task_rejected', str(error))
            return False
        self.final_targets = targets
        self.task_name = name
        self.gesture = OutwardGesture(**dict(zip(
            ('left_index', 'right_index', 'left_sign', 'right_sign', 'threshold', 'neutral', 'hold'),
            (gesture[k] for k in ('left_axis_index', 'right_axis_index', 'left_axis_sign',
             'right_axis_sign', 'gesture_threshold', 'neutral_threshold', 'gesture_hold_sec'))))) if gesture else OutwardGesture()
        self.limits = {}
        if self.description_message is not None:
            self.on_description(self.description_message)
        self.task_enabled.publish(Bool(data=targets is not None))
        self.report('task_selected', name or 'Task final pose disabled')
        return True

    def on_task_selection(self, msg):
        # A leader may select any task with a valid task YAML.
        if not msg.data or not msg.data.replace('_', '').isalnum():
            return
        self.leader_task_received = time.monotonic()
        if self.task_name != msg.data:
            self.select_task(msg.data)

    def expire_task_selection(self):
        if self.leader_task_received and time.monotonic()-self.leader_task_received > 1.5:
            # Never retain task gestures when a different/default leader takes over.
            restore = self.launch_task_name
            if restore and not (Path(self.tasks_dir) / (restore + '.yaml')).is_file():
                restore = ''
            if self.select_task(restore):
                self.leader_task_received = 0.

    def on_leader_profile(self, msg):
        try:
            self.leader_profile = json.loads(msg.data).get('control_profile', '')
            self.leader_profile_received = time.monotonic()
        except (ValueError, AttributeError):
            self.leader_profile = ''

    def on_joystick(self, msg):
        if (self.final_targets is None or self.leader_profile not in ('lg2_mini_sh5_recording', 'a3_sh5')
                or time.monotonic() - self.leader_profile_received > 1.5):
            return
        sides = self.gesture.update(msg.data, time.monotonic())
        if sides:
            ok, detail = self.start(False, sides)
            if not ok:
                self.report('rejected', detail)

    def on_bringdown(self, request, response):
        response.success, response.message = self.start(True)
        return response

    def on_final_pose(self, request, response):
        response.success, response.message = self.start(False)
        return response

    def start(self, shutdown, sides=('left', 'right')):
        if shutdown and self.require_init_profile and not self.bringdown_control_hands and self.init_profile_key is None:
            return False, 'Waiting for follower initialization profile on /ffw/init_profile'
        if not shutdown and self.final_targets is None:
            return False, 'Final pose is disabled; launch follower with task_name:=Task_000650 (or another configured task)'
        if self.worker is not None and self.worker.is_alive():
            return False, 'A pose operation is already running; return stick to neutral and retry'
        try:
            required_groups = self.bringdown_groups if shutdown else self.final_targets.keys()
            active_nodes = {name for name, _ in self.get_node_names_and_namespaces()}
            busy_groups = sorted(group for group in required_groups
                                 if f'{group}_joint_trajectory_executor' in active_nodes)
            if busy_groups:
                raise RuntimeError(f'Follower initialization is still running for {", ".join(busy_groups)}')
            self.snapshot(required_groups)
            if not all(self.motion_clients[g].server_is_ready() for g in required_groups):
                raise RuntimeError(f'Required action servers are not ready: {sorted(required_groups)}')
            # Shared across independently launched bringdown and final-pose nodes.
            handle = open(f'/tmp/sh5-pose-{os.getuid()}-{os.environ.get("ROS_DOMAIN_ID", "0")}.lock','a+')
            try:
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except Exception:
                handle.close()
                raise
        except Exception as error:
            return False, str(error)
        self.worker = threading.Thread(target=self.run_operation,args=(shutdown,handle,sides),daemon=True)
        self.worker.start()
        return True, 'Bringdown accepted' if shutdown else 'Final pose accepted'

    def wait(self, future, timeout):
        deadline = time.monotonic()+timeout
        while not future.done():
            if self.stop.wait(.02) or time.monotonic() >= deadline:
                raise RuntimeError('Operation stopped or controller request timed out')
        return future.result()

    def switch_off(self, manager, names=None, required=True):
        listing, switching = self.managers[manager]
        if not listing.wait_for_service(timeout_sec=3.):
            if required:
                raise RuntimeError(f'Manager unavailable: {manager}')
            return
        controllers = self.wait(listing.call_async(ListControllers.Request()),5.).controller
        selected = [c.name for c in controllers if c.state=='active' and (names is None or c.name in names)]
        if not selected:
            return
        if not switching.wait_for_service(timeout_sec=3.):
            raise RuntimeError('Controller switch unavailable')
        request = SwitchController.Request(deactivate_controllers=selected, strictness=2,
                                           timeout=Duration(sec=5))
        if not self.wait(switching.call_async(request),8.).ok:
            raise RuntimeError(f'Could not deactivate controllers: {selected}')

    def confirm(self, targets, timeout):
        deadline = time.monotonic()+timeout
        stable = None
        while time.monotonic() < deadline:
            current = self.snapshot(targets)
            errors = [(name,abs(a-b),self.groups[g]['tolerance'])
                for g,values in targets.items()
                for name,a,b in zip(self.groups[g]['names'],current[g],values)
                if abs(a-b)>self.groups[g]['tolerance']]
            if not errors:
                stable = time.monotonic() if stable is None else stable
                if time.monotonic()-stable >= .3:
                    return
            else:
                stable = None
            if self.stop.wait(.05):
                raise RuntimeError('Pose confirmation stopped')
        raise RuntimeError(f'Measured pose confirmation timed out: {errors[:4]}')

    def move_phase(self, name, targets):
        current = self.snapshot(targets)
        duration = max(motion_duration(current[g],v,self.speed) for g,v in targets.items())
        settling = max(self.hand_timeout if g.startswith('hand') else self.arm_timeout for g in targets)
        self.report('moving', f'{name}: {duration:.2f}s; groups={",".join(targets)}; settling allowance {settling:.0f}s')
        futures = []
        for group,values in targets.items():
            info = self.groups[group]
            goal = FollowJointTrajectory.Goal()
            goal.trajectory.joint_names = info['names']
            goal.goal_time_tolerance = duration_message(self.hand_timeout if group.startswith('hand') else self.arm_timeout)
            goal.goal_tolerance = [JointTolerance(name=n,position=info['tolerance']) for n in info['names']]
            goal.trajectory.points = [JointTrajectoryPoint(positions=v,time_from_start=duration_message(t))
                                     for t,v in quintic_samples(current[group],values,duration)]
            if group in self.effort_pubs:
                self.effort_pubs[group].publish(Float64MultiArray(data=[self.effort]*len(values)))
            pending = self.motion_clients[group].send_goal_async(goal)
            try:
                handle = self.wait(pending,5.)
            except Exception:
                def cancel_late(future):
                    accepted = future.result()
                    if accepted is not None and accepted.accepted:
                        accepted.cancel_goal_async()
                pending.add_done_callback(cancel_late)
                raise
            if not handle.accepted:
                raise RuntimeError(f'{group} rejected waypoint')
            self.handles.append(handle)
            futures.append((group,handle.get_result_async()))
        deadline = time.monotonic()+duration+settling+5.
        for group,future in futures:
            result = self.wait(future,max(0.,deadline-time.monotonic()))
            if result.status!=GoalStatus.STATUS_SUCCEEDED or result.result.error_code!=0:
                raise RuntimeError(f'{group} failed {name}: {result.result.error_string}')
        self.confirm(targets,settling)
        self.handles = []

    def stop_supervisors(self):
        for service in self.supervisor_services:
            path = Path('/run/service')/service
            if not path.is_dir():
                raise RuntimeError(f'Supervisor service unavailable: {path}')
        for service in self.supervisor_services:
            subprocess.run(['/command/s6-svc','-d',str(Path('/run/service')/service)],check=True,timeout=5.)
            subprocess.run(['/command/s6-svwait','-d','-t','15000',str(Path('/run/service')/service)],check=True,timeout=16.)

    def run_operation(self, shutdown, handle, sides=('left', 'right')):
        try:
            stop_leader_launch = False
            if shutdown and self.shutdown_mode == 's6':
                # Check the supervisor contract before moving or disabling anything.
                for service in self.supervisor_services:
                    if not (Path('/run/service')/service).is_dir():
                        raise RuntimeError(f'Missing shutdown service: {service}')
            elif shutdown:
                has_leader = self.managers['/leader/controller_manager'][0].wait_for_service(timeout_sec=.5)
                if has_leader or self.leader_required:
                    if not self.leader_shutdown.wait_for_service(timeout_sec=2.):
                        raise RuntimeError('Leader launch does not provide /leader/shutdown; restart it with the updated SH5 launch')
                    stop_leader_launch = True
            self.snapshot(self.bringdown_groups if shutdown else self.final_targets.keys())
            if shutdown:
                if self.preset_pause.wait_for_service(timeout_sec=.5):
                    if not self.wait(self.preset_pause.call_async(SetBool.Request(data=True)),3.).success:
                        raise RuntimeError('Preset bridge refused to pause')
                elif any(name == 'hand_preset_bridge' for name, namespace in self.get_node_names_and_namespaces()):
                    raise RuntimeError('Running preset bridge does not provide its pause service')
                self.switch_off('/leader/controller_manager',
                    ['joint_trajectory_command_broadcaster', 'joystick_controller'],self.leader_required)
            else:
                # Keep joystick and opposite-side teleop alive. C++ owns per-side
                # routing, so no competing streaming command can replace this goal.
                for side in sides:
                    for client in (self.side_pause[side], self.side_resume[side]):
                        if not client.wait_for_service(timeout_sec=2.):
                            raise RuntimeError('Task final pose requires the updated C++ hand control bridge')
                for side in sides:
                    if not self.wait(self.side_pause[side].call_async(SetBool.Request(data=True)),3.).success:
                        raise RuntimeError(f'Could not acquire {side} command ownership')
            phases = self.phases if shutdown else [
                ('final_pose', {g: values for g,values in self.final_targets.items()
                                if g[-1] in {side[0] for side in sides}})]
            for name,targets in phases:
                self.move_phase(name,targets)
            if shutdown:
                self.confirm(self.phases[-1][1],self.hand_timeout)
                self.switch_off('/leader/controller_manager',required=self.leader_required)
                self.switch_off('/controller_manager')
                if self.shutdown_mode == 's6':
                    self.stop_supervisors()
                elif stop_leader_launch:
                    result = self.wait(self.leader_shutdown.call_async(Trigger.Request()), 5.)
                    if not result.success:
                        raise RuntimeError(f'Leader shutdown failed: {result.message}')
            else:
                for side in sides:
                    if not self.wait(self.side_resume[side].call_async(SetBool.Request(data=True)),3.).success:
                        raise RuntimeError(f'Could not arm deliberate {side} teleop re-entry')
            self.report('succeeded', 'Bringdown complete; controllers deactivated; launch shutdown requested' if shutdown else
                        'Task final pose reached; selected side held. Disable and re-enable that side teleop to resume; opposite side remains available')
            if shutdown and self.shutdown_mode == 'launch':
                # The parent follower launch handles this distinct exit code.
                # Allow the completion status to reach the requesting client.
                self.exit_deadline = time.monotonic() + .5
        except Exception as error:
            for goal in self.handles:
                try:
                    self.wait(goal.cancel_goal_async(),3.)
                except Exception:
                    pass
            self.report('failed', str(error)+'; no further shutdown steps were run')
        finally:
            self.handles=[]
            handle.close()

    def destroy_node(self):
        self.task_enabled.publish(Bool(data=False))
        self.stop.set()
        if self.worker and self.worker.is_alive():
            self.worker.join(timeout=4.)
        self.receiver_lock.close()
        return super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SH5Bringdown()
    try:
        while rclpy.ok() and (node.exit_deadline is None or time.monotonic() < node.exit_deadline):
            rclpy.spin_once(node, timeout_sec=.1)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
    if node.exit_deadline is not None:
        raise SystemExit(SHUTDOWN_EXIT_CODE)
