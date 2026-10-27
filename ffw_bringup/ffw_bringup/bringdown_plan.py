"""Separate SH5 lowering path and explicitly selected task final poses."""
import json
import math
from pathlib import Path
import yaml

PROFILE = 'ffw_sh5_follower_initial_positions_Task_000650.yaml'
GROUPS = ('arm_l', 'arm_r', 'hand_l', 'hand_r')


def load_plan(config_dir, endpose_file):
    document = yaml.safe_load((Path(config_dir) / PROFILE).read_text())['/**']
    endpose = json.loads(Path(endpose_file).read_text())
    if endpose['robot_type'] != 'ffw_sh5_rev1':
        raise ValueError('End pose must belong to ffw_sh5_rev1')
    groups = {}
    for group in GROUPS:
        params = document[group + '_joint_trajectory_executor']['ros__parameters']
        names = params['joint_names']
        steps = params['step_names']
        if not names or len(set(names)) != len(names):
            raise ValueError('Invalid joint names')
        for step in steps:
            if len(params[step]) != len(names) or not all(math.isfinite(v) for v in params[step]):
                raise ValueError('Invalid startup waypoint')
        final = [endpose['joints'][name] for name in names]
        if not all(type(v) in (int, float) and math.isfinite(v) for v in final):
            raise ValueError('Invalid final pose')
        groups[group] = dict(names=names, topic=params['action_topic'],
            tolerance=float(params['position_tolerance']), final=final,
            reverse=[list(params[step]) for step in reversed(steps)], steps=list(reversed(steps)))
    if groups['arm_l']['steps'] != groups['arm_r']['steps']:
        raise ValueError('Arm approach steps must match')
    # Preserve BOTH original retraction/clearance waypoints in reverse approach
    # order. Do not deduplicate step1 even if it is close to task_start in YAML.
    # Only the separate raised task final pose is excluded from bringdown.
    phases = [('task_start', {g: groups[g]['reverse'][0] for g in GROUPS})]
    for step in ('step1', 'step0'):
        waypoint = {}
        for g in GROUPS:
            if g.startswith('arm'):
                if step not in groups[g]['steps']:
                    raise ValueError(f'Bringdown requires the {step} waypoint')
                waypoint[g] = groups[g]['reverse'][groups[g]['steps'].index(step)]
            else:
                waypoint[g] = groups[g]['reverse'][0]
        phases.append((step, waypoint))
    phases.append(('arms_down', {g: [0.0]*7 if g.startswith('arm')
                               else groups[g]['reverse'][0] for g in GROUPS}))
    return groups, phases


def load_task_final_pose(task_name, tasks_dir, groups):
    if not task_name:
        return None, None
    # Explicit allow-list through config files; no arbitrary path traversal.
    if not task_name.replace('_', '').isalnum():
        raise ValueError('Invalid task_name')
    root = Path(tasks_dir).resolve()
    document = yaml.safe_load((root / (task_name + '.yaml')).read_text())
    if document.get('robot_type') != 'ffw_sh5_rev1':
        raise ValueError('Task final pose must target SH5')
    if document.get('final_pose_enabled', True) is False:
        return None, None
    if 'final_pose' in document:
        pose = document['final_pose']
    else:
        source = (root / document['final_pose_file']).resolve()
        if not source.is_relative_to(root.parent):
            raise ValueError('Task pose file must be inside the bringup config directory')
        pose = json.loads(source.read_text())
    if pose.get('robot_type') != 'ffw_sh5_rev1':
        raise ValueError('Invalid final-pose robot type')
    targets = {g: [pose['joints'][n] for n in groups[g]['names']] for g in GROUPS}
    if any(type(v) not in (int, float) or not math.isfinite(v) for values in targets.values() for v in values):
        raise ValueError('Invalid task final-pose values')
    return targets, document['gesture']


def motion_duration(start, end, speed=.25):
    if not math.isfinite(speed) or speed <= 0:
        raise ValueError('Joint speed must be positive and finite')
    return max(4.0, 1.875 * max(abs(a-b) for a,b in zip(start,end)) / speed)


def quintic_samples(start, end, duration, count=51):
    for index in range(count):
        u = index / (count-1)
        blend = 10*u**3 - 15*u**4 + 6*u**5
        yield duration*u, [a + (b-a)*blend for a,b in zip(start,end)]


class OutwardGesture:
    """Independent per-hand edge detection; require neutral before each gesture."""
    def __init__(self, left_index=1, right_index=4, left_sign=1., right_sign=1.,
                 threshold=.7, neutral=.2, hold=.3):
        self.indices = (left_index, right_index)
        self.signs = (left_sign, right_sign)
        self.threshold, self.neutral, self.hold = threshold, neutral, hold
        self.armed = {'left': False, 'right': False}
        self.since = {'left': None, 'right': None}
        self.last = None

    def update(self, values, now):
        fired = []
        invalid = len(values) <= max(self.indices) or any(not math.isfinite(v) for v in values)
        stale = self.last is not None and now-self.last > .5
        if invalid or stale:
            self.armed = dict.fromkeys(self.armed, False)
            self.since = dict.fromkeys(self.since, None)
        self.last = now
        if invalid:
            return fired
        for hand,index,sign in zip(('left', 'right'), self.indices, self.signs):
            value = values[index]*sign
            if abs(value) < self.neutral:
                self.armed[hand] = True
                self.since[hand] = None
            elif self.armed[hand] and value >= self.threshold:
                self.since[hand] = now if self.since[hand] is None else self.since[hand]
                if now-self.since[hand] >= self.hold:
                    self.armed[hand] = False
                    self.since[hand] = None
                    fired.append(hand)
            else:
                self.since[hand] = None
        return fired
