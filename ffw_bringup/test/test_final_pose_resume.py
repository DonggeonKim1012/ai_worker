"""Exercise final-pose completion without a ROS graph or motion commands."""
from types import SimpleNamespace
from unittest.mock import Mock
import pytest
from ffw_bringup import sh5_bringdown as module


@pytest.mark.parametrize('side', ['left', 'right'])
def test_stop_waits_for_fresh_selected_side_ack(monkeypatch, side):
    clock = [10.0]
    monkeypatch.setattr(module.time, 'monotonic', lambda: clock[0])
    node = SimpleNamespace(side_commands={'left': Mock(), 'right': Mock()},
                           side_teleop_states={side: (0, 9.0)}, stop=Mock())
    def wait(delay):
        clock[0] += delay
        node.side_teleop_states[side] = (0, clock[0])
        return False
    node.stop.wait.side_effect = wait
    module.SH5Bringdown.stop_side_teleop(node, side)
    node.stop.wait.assert_called_once()
    assert node.side_commands[side].publish.call_args.args[0].data == 0
    node.side_commands['right' if side == 'left' else 'left'].publish.assert_not_called()


def test_no_ack_keeps_side_held(monkeypatch):
    clock = [10.0]
    monkeypatch.setattr(module.time, 'monotonic', lambda: clock[0])
    node = SimpleNamespace(side_commands={'left': Mock()},
                           side_teleop_states={'left': (1, 10.0)}, stop=Mock())
    def wait(delay):
        clock[0] += delay
        return False
    node.stop.wait.side_effect = wait
    with pytest.raises(RuntimeError, match='side remains held'):
        module.SH5Bringdown.stop_side_teleop(node, 'left')


@pytest.mark.parametrize('side', ['left', 'right'])
def test_completion_stops_selected_side_before_arming_resume(side):
    events = []
    node = SimpleNamespace(
        final_targets={'arm_l': [0.]*7, 'arm_r': [0.]*7},
        side_pause={'left': Mock(), 'right': Mock()},
        side_resume={'left': Mock(), 'right': Mock()},
        snapshot=Mock(), handles=[], report=Mock(),
        wait=lambda future, timeout: SimpleNamespace(success=True),
        move_phase=lambda name, targets: events.append(('move', set(targets))),
        stop_side_teleop=lambda selected: events.append(('stop', selected)))
    node.side_resume[side].call_async.side_effect = lambda req: events.append(('resume', side))
    handle = Mock()
    module.SH5Bringdown.run_operation(node, False, handle, (side,))
    assert events == [('move', {'arm_' + side[0]}), ('stop', side), ('resume', side)]
    node.side_resume['right' if side == 'left' else 'left'].call_async.assert_not_called()
    assert node.report.call_args.args[0] == 'succeeded'
    handle.close.assert_called_once()
