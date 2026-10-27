"""Task initialization and reverse bringdown paths; no hardware required."""
import copy
import json
from pathlib import Path
import tempfile
import yaml
from ffw_bringup.bringdown_plan import load_plan
from ffw_bringup.follower_task_state import (
    read_initial_pose, task_initial_pose, profile_message, reverse_arm_plan)

BASE = Path(__file__).resolve().parents[1] / 'config'
PROFILE = BASE / 'ffw_sh5_rev1_follower'


def test_802_matches_penultimate_and_final_elbows_and_head():
    base = read_initial_pose(PROFILE / 'ffw_sh5_follower_initial_positions_Task_000650.yaml')
    result = task_initial_pose(BASE, 'Task_000802')
    expected = copy.deepcopy(base)
    for side in ('l', 'r'):
        node = f'arm_{side}_joint_trajectory_executor'
        values = expected['/**'][node]['ros__parameters']['task_start']
        values[3] = round(values[3] - .2, 6)
        expected['/**'][node]['ros__parameters']['step1'] = list(values)
    expected['/**']['head_joint_trajectory_executor']['ros__parameters']['task_start'] = [.83, 0.]
    assert result == expected
    assert result['/**']['arm_l_joint_trajectory_executor']['ros__parameters']['step0'][3] == -2.8


def test_reverse_exact_actual_steps_then_arms_down():
    groups, _ = load_plan(PROFILE, PROFILE.parent / 'ffw_lg2_mini_leader/bgf_waypoint1_endpose.json')
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / 'initial.yaml'
        path.write_text(yaml.safe_dump(task_initial_pose(BASE, 'Task_000802')))
        msg = profile_message(path, 'Task_000802')
        phases = reverse_arm_plan(msg, groups)
        assert [name for name, _ in phases] == ['task_start', 'step1', 'step0', 'arms_down']
        for name, targets in phases[:-1]:
            assert set(targets) == {'arm_l', 'arm_r'}
            for group, values in targets.items():
                step = next(s for s in msg['groups'][group]['steps'] if s['name'] == name)
                assert values == step['positions']
        assert phases[-1][1] == {'arm_l': [0.] * 7, 'arm_r': [0.] * 7}
        changed = copy.deepcopy(msg)
        changed['groups']['arm_r']['steps'][0]['positions'][0] = float('nan')
        try:
            reverse_arm_plan(changed, groups)
        except ValueError:
            pass
        else:
            raise AssertionError('Non-finite target accepted')


def test_default_repeated_ros_namespaces_and_explicit_profiles():
    groups, _ = load_plan(PROFILE, PROFILE.parent / 'ffw_lg2_mini_leader/bgf_waypoint1_endpose.json')
    path = PROFILE / 'ffw_sh5_follower_initial_positions.yaml'
    doc = read_initial_pose(path)
    assert len(doc['/**']) == 7
    msg = profile_message(path, '')
    phases = reverse_arm_plan(msg, groups)
    assert [name for name, _ in phases] == ['step1', 'step0', 'arms_down']
    # Active follower path is independent of a leader/end-pose task selection.
    assert msg['task_name'] == ''
    assert all(set(targets) == {'arm_l', 'arm_r'} for _, targets in phases)
