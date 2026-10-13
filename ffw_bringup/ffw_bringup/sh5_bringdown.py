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
from std_msgs.msg import Float64MultiArray, String
from std_srvs.srv import Trigger, SetBool
from trajectory_msgs.msg import JointTrajectoryPoint
from ffw_bringup.bringdown_plan import GROUPS, OutwardGesture, load_plan, motion_duration, quintic_samples


def duration_message(value):
    return Duration(sec=int(value), nanosec=int((value % 1)*1e9))


class SH5Bringdown(Node):
    def __init__(self, **kwargs):
        super().__init__('sh5_final_pose', **kwargs)
        base = Path(get_package_share_directory('ffw_bringup')) / 'config'
        def param(name, default):
            return self.declare_parameter(name, default).value
        self.groups, self.phases = load_plan(param('config_dir', str(base/'ffw_sh5_rev1_follower')),
            param('endpose_file', str(base/'ffw_lg2_mini_leader/bgf_waypoint1_endpose.json')))
        self.hand_timeout = float(param('hand_confirm_timeout', 60.))
        self.arm_timeout = float(param('arm_confirm_timeout', 20.))
        self.speed = float(param('max_joint_speed', .25))
        self.effort = float(param('hand_effort_ma', 600.))
        if any(not math.isfinite(v) or v <= 0 for v in (self.hand_timeout, self.arm_timeout, self.speed)) or not 0 <= self.effort <= 910:
            raise ValueError('Invalid motion timeout, speed or current')
        self.gesture = OutwardGesture(param('left_axis_index', 1), param('right_axis_index', 4),
            param('left_axis_sign', 1.), param('right_axis_sign', 1.),
            param('gesture_threshold', .7), param('neutral_threshold', .2), param('gesture_hold_sec', .3))
        self.supervisor_services = list(param('shutdown_services', ['ai_worker_navigation', 'ai_worker_bringup', 'avatar_bringup']))
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
        self.status = self.create_publisher(String, '/ffw/bringdown/status',
            QoSProfile(depth=10, durability=DurabilityPolicy.TRANSIENT_LOCAL))
        self.create_subscription(JointState, '/joint_states', self.on_state, 10)
        self.create_subscription(JointState, '/arm_hand/joint_states', self.on_state, 10)
        self.create_subscription(String, '/robot_description', self.on_description,
            QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL))
        self.create_subscription(Float64MultiArray, '/leader/joystick_controller/sensorxel_joy_values', self.on_joystick, 10)
        self.create_service(Trigger, '/ffw/bringdown', self.on_bringdown)
        self.create_service(Trigger, '/ffw/final_pose', self.on_final_pose)
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
        try:
            limits = {}
            for joint in ET.fromstring(msg.data).findall('joint'):
                limit = joint.find('limit')
                if limit is not None and 'lower' in limit.attrib:
                    limits[joint.get('name')] = (float(limit.get('lower')),float(limit.get('upper')))
            for _, phase in self.phases:
                for group, values in phase.items():
                    for name,value in zip(self.groups[group]['names'],values):
                        low,high = limits[name]
                        if not all(math.isfinite(v) for v in (low,high,value)) or not low <= value <= high:
                            raise ValueError(f'Waypoint exceeds joint limits: {name}')
            self.limits = limits
        except (ET.ParseError, KeyError, TypeError, ValueError) as error:
            self.limits = {}
            self.report('invalid_description', str(error))

    def snapshot(self):
        if not self.limits:
            raise RuntimeError('Follower description/waypoint limits not validated')
        with self.lock:
            states = dict(self.states)
        result = {}
        now = time.monotonic()
        for group, info in self.groups.items():
            result[group] = []
            for name in info['names']:
                value, stamp = states.get(name, (math.nan,0.))
                if not math.isfinite(value) or now-stamp > .5:
                    raise RuntimeError(f'Missing/stale measured joint: {name}')
                result[group].append(value)
        return result

    def on_joystick(self, msg):
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
        if self.worker is not None and self.worker.is_alive():
            return False, 'A pose operation is already running; return stick to neutral and retry'
        try:
            self.snapshot()
            if not all(c.server_is_ready() for c in self.motion_clients.values()):
                raise RuntimeError('Arm/hand action servers are not ready')
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
            current = self.snapshot()
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
        current = self.snapshot()
        duration = max(motion_duration(current[g],v,self.speed) for g,v in targets.items())
        self.report('moving', f'{name}: {duration:.2f}s; finger settling allowance {self.hand_timeout:.0f}s')
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
        deadline = time.monotonic()+duration+max(self.hand_timeout,self.arm_timeout)+5.
        for group,future in futures:
            result = self.wait(future,max(0.,deadline-time.monotonic()))
            if result.status!=GoalStatus.STATUS_SUCCEEDED or result.result.error_code!=0:
                raise RuntimeError(f'{group} failed {name}: {result.result.error_string}')
        self.confirm(targets,self.hand_timeout)
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
            if shutdown:
                # Check the supervisor contract before moving or disabling anything.
                for service in self.supervisor_services:
                    if not (Path('/run/service')/service).is_dir():
                        raise RuntimeError(f'Missing shutdown service: {service}')
            self.snapshot()
            if self.preset_pause.wait_for_service(timeout_sec=.5):
                if not self.wait(self.preset_pause.call_async(SetBool.Request(data=True)),3.).success:
                    raise RuntimeError('Preset bridge refused to pause')
            elif any(name == 'hand_preset_bridge' for name, namespace in self.get_node_names_and_namespaces()):
                raise RuntimeError('Running preset bridge does not provide its pause service')
            self.switch_off('/leader/controller_manager',
                ['joint_trajectory_command_broadcaster'],self.leader_required)
            phases = self.phases if shutdown else [
                ('final_pose', {g: values for g,values in self.phases[0][1].items()
                                if g[-1] in {side[0] for side in sides}})]
            for name,targets in phases:
                self.move_phase(name,targets)
            if shutdown:
                self.confirm(self.phases[-1][1],self.hand_timeout)
                self.switch_off('/leader/controller_manager',required=self.leader_required)
                self.switch_off('/controller_manager')
                self.stop_supervisors()
            self.report('succeeded', 'Controllers and follower stopped' if shutdown else
                        'Final pose reached; leader arm broadcaster remains paused')
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
        self.stop.set()
        if self.worker and self.worker.is_alive():
            self.worker.join(timeout=4.)
        return super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SH5Bringdown()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()
