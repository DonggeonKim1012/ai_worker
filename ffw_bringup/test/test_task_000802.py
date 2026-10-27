"""Task configuration tests; no ROS graph or hardware required."""
from pathlib import Path
import yaml
from ffw_bringup.bringdown_plan import load_plan, load_task_final_pose, OutwardGesture

BASE = Path(__file__).resolve().parents[1] / 'config'


def test_capture_and_existing_task_compatibility():
    groups, _ = load_plan(str(BASE / 'ffw_sh5_rev1_follower'),
                         str(BASE / 'ffw_lg2_mini_leader/bgf_waypoint1_endpose.json'))
    targets, _ = load_task_final_pose('Task_000802', str(BASE / 'tasks'), groups)
    assert {key: len(value) for key, value in targets.items()} == {
        'arm_l': 7, 'arm_r': 7, 'hand_l': 20, 'hand_r': 20}
    assert load_task_final_pose('', str(BASE / 'tasks'), groups) == (None, None)
    assert load_task_final_pose('Task_000650', str(BASE / 'tasks'), groups)[0]
    config = yaml.safe_load((BASE / 'tasks/Task_000802.yaml').read_text())
    for group, values in targets.items():
        assert values == [config['final_pose']['joints'][n] for n in groups[group]['names']]
    assert config['a3_joystick'] == {
        'allow_task_final_pose': True, 'final_pose_gesture_enabled': True,
        'task_vertical_motion': False, 'enable_randomization': False}


def test_each_outward_gesture_requires_neutral_and_fires_once():
    cfg = yaml.safe_load((BASE / 'tasks/Task_000802.yaml').read_text())['gesture']
    assert cfg['gesture_hold_sec'] == 2.0
    for side in ('left', 'right'):
        gesture = OutwardGesture(left_sign=cfg['left_axis_sign'],
                                 right_sign=cfg['right_axis_sign'], hold=cfg['gesture_hold_sec'])
        values = [0.] * 6
        index = cfg[side + '_axis_index']
        values[index] = cfg[side + '_axis_sign']
        assert gesture.update(values, 0.) == []  # held at startup is ignored
        assert gesture.update([0.] * 6, .1) == []
        assert gesture.update(values, .2) == []
        for tick in range(3, 22):
            assert gesture.update(values, tick / 10) == []
        assert gesture.update(values, 2.21) == [side]
        assert gesture.update(values, 2.3) == []
        assert gesture.update([0.] * 6, 2.4) == []
        values[index] *= -1
        for tick in range(25, 50):
            assert gesture.update(values, tick / 10) == []


def test_interrupted_or_stale_hold_does_not_fire():
    gesture = OutwardGesture(hold=2.0)
    outward = [0., 1., 0., 0., 0., 0.]
    gesture.update([0.] * 6, 0.)
    for tick in range(1, 20):
        assert gesture.update(outward, tick / 10) == []
    assert gesture.update([0.] * 6, 2.) == []
    for tick in range(21, 40):
        assert gesture.update(outward, tick / 10) == []
    # A gap in samples cannot count as continued physical input.
    assert gesture.update(outward, 5.) == []
    for tick in range(51, 80):
        assert gesture.update(outward, tick / 10) == []
