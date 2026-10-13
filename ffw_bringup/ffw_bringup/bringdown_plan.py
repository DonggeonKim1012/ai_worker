"""Task 650 reverse approach and shared raised final pose."""
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
    phases = [('final_pose', {g: groups[g]['final'] for g in GROUPS})]
    for index, step in enumerate(groups['arm_l']['steps']):
        phases.append((step, {g: groups[g]['reverse'][index] if g.startswith('arm')
                             else groups[g]['reverse'][0] for g in GROUPS}))
    phases.append(('arms_down', {g: [0.0]*7 if g.startswith('arm')
                               else groups[g]['reverse'][0] for g in GROUPS}))
    return groups, phases


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
