"""ROS message-level tests; no hardware nodes or physical commands are started."""
from pathlib import Path
import tempfile
import subprocess
from ament_index_python.packages import get_package_share_directory
import time
import unittest
from unittest.mock import Mock

import rclpy
from rclpy.parameter import Parameter
from rcl_interfaces.msg import Parameter as ParameterMessage, ParameterValue
from rcl_interfaces.srv import SetParametersAtomically
from sensor_msgs.msg import JointState
from std_msgs.msg import String, UInt8
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from ffw_teleop.hand_preset_bridge import HandPresetBridge
from ffw_teleop.hand_preset_model import load_config
CONFIG_FILE = Path(__file__).resolve().parents[2] / 'ffw_bringup/config/ffw_lg2_mini_leader/hand_preset_interpolator.yaml'
CONFIG = load_config(CONFIG_FILE)
POSES = {str(n): {s: CONFIG[f'{s}_preset_{n}'] for s in ('left', 'right')}
         for n in CONFIG['preset_ids']}


class BridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rclpy.init()
        source = Path(get_package_share_directory('ffw_description')) / 'urdf/ffw_sh5_rev1_follower/ffw_sh5_follower.urdf.xacro'
        cls.description = subprocess.check_output(['xacro', str(source)], text=True)

    @classmethod
    def tearDownClass(cls):
        rclpy.shutdown()

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.node = HandPresetBridge(parameter_overrides=[Parameter(
            'preset_file', value=str(Path(self.directory.name) / 'presets.json')),
            Parameter('config_file', value=str(CONFIG_FILE))])
        self.addCleanup(self.node.destroy_node)
        self.node.pubs = {'left': Mock(), 'right': Mock()}
        self.node.effort_pubs = {'left': Mock(), 'right': Mock()}
        self.node.feedback = Mock()
        self.node.on_description(String(data=self.description))
        self.assertTrue(self.node.ready, 'Existing SH5 preset poses must fit actual URDF limits')
        self.msg = JointTrajectory(joint_names=['gripper_l_joint1'],
            points=[JointTrajectoryPoint(positions=[1.1])])

    def test_requires_arm_enabled_and_fresh_heartbeat(self):
        self.node.on_trajectory('left', self.msg)
        self.node.pubs['left'].publish.assert_not_called()
        self.node.on_teleop('left', UInt8(data=1))
        self.node.on_trajectory('left', self.msg)
        actual = self.node.pubs['left'].publish.call_args[0][0].points[0].positions
        for value, target in zip(actual, POSES['5']['left']):
            self.assertAlmostEqual(value, target)
        self.node.teleop['left'] = (True, time.monotonic() - 1.0)
        self.node.on_trajectory('left', self.msg)
        self.assertEqual(self.node.pubs['left'].publish.call_count, 1)
        self.node.on_teleop('left', UInt8(data=0))
        self.node.on_trajectory('left', self.msg)
        self.assertEqual(self.node.pubs['left'].publish.call_count, 1)

    def test_main_trajectory_gating_without_recovery_heartbeat(self):
        self.node.require_teleop_heartbeat = False
        self.node.on_trajectory('left', self.msg)
        self.node.pubs['left'].publish.assert_called_once()
        self.node.ready = False
        self.node.on_trajectory('left', self.msg)
        self.assertEqual(self.node.pubs['left'].publish.call_count, 1)

    def test_selection_requires_released_trigger(self):
        self.node.trigger['left'] = 1.0
        request = SetParametersAtomically.Request(parameters=[
            ParameterMessage(name='side', value=ParameterValue(type=4, string_value='left')),
            ParameterMessage(name='preset_id', value=ParameterValue(type=2, integer_value=2))])
        response = self.node.on_service('set', request, SetParametersAtomically.Response())
        self.assertFalse(response.result.successful)
        self.assertEqual(self.node.catalog.active['left'], 5)

    def test_partial_or_nan_message_never_commands_hand(self):
        self.node.on_teleop('left', UInt8(data=1))
        for values in ([], [float('nan')], [0.0, 1.0]):
            self.msg.points[0].positions = values
            self.node.on_trajectory('left', self.msg)
        self.node.pubs['left'].publish.assert_not_called()

    def test_selecting_preset_does_not_move_hand(self):
        self.node.on_teleop('left', UInt8(data=1))
        request = SetParametersAtomically.Request(parameters=[
            ParameterMessage(name='side', value=ParameterValue(type=4, string_value='both')),
            ParameterMessage(name='preset_id', value=ParameterValue(type=2, integer_value=2))])
        response = self.node.on_service('set', request, SetParametersAtomically.Response())
        self.assertTrue(response.result.successful, response.result.reason)
        self.assertEqual(self.node.catalog.active, {'left': 2, 'right': 2})
        self.node.pubs['left'].publish.assert_not_called()
        self.node.pubs['right'].publish.assert_not_called()

    def test_preset_five_publishes_its_own_pose(self):
        self.node.catalog.apply('set', {'side': 'left', 'preset_id': 5})
        self.node.on_teleop('left', UInt8(data=1))
        self.node.on_trajectory('left', self.msg)
        actual = self.node.pubs['left'].publish.call_args[0][0].points[0].positions
        for value, target in zip(actual, POSES['5']['left']):
            self.assertAlmostEqual(value, target)

    def test_continuous_hand_targets_do_not_add_a_future_interpolation_window(self):
        self.node.catalog.apply('set', {'side': 'left', 'preset_id': 5})
        self.node.on_teleop('left', UInt8(data=1))
        for raw in (-0.1, 0.5, 1.1, 1.1):
            self.msg.points[0].positions = [raw]
            self.node.on_trajectory('left', self.msg)
            point = self.node.pubs['left'].publish.call_args[0][0].points[0]
            self.assertEqual(point.time_from_start.sec, 0)
            self.assertEqual(point.time_from_start.nanosec, 0)
        for value, target in zip(point.positions, POSES['5']['left']):
            self.assertAlmostEqual(value, target)

    def test_virtual_feedback_preserves_units(self):
        self.node.on_virtual_command(JointState(name=['gripper_l_joint1', 'gripper_r_joint1'],
                                                position=[-0.1, 1.1]))
        output = self.node.feedback.publish.call_args[0][0]
        self.assertEqual(list(output.position), [-0.1, 1.1])
        self.node.on_virtual_command(JointState(name=['gripper_l_joint1'], position=[float('nan')]))
        self.assertEqual(self.node.feedback.publish.call_count, 1)

    def test_trigger_restores_configured_current_independently(self):
        self.node.on_teleop('left', UInt8(data=1))
        for raw, expected in [(-0.1, 300.0), (0.5, 450.0), (1.1, 600.0)]:
            self.msg.points[0].positions = [raw]
            self.node.on_trajectory('left', self.msg)
            self.assertEqual(list(self.node.effort_pubs['left'].publish.call_args[0][0].data),
                             [expected] * 20)
        self.node.effort_pubs['right'].publish.assert_not_called()
        self.node.on_teleop('left', UInt8(data=0))
        self.node.on_trajectory('left', self.msg)
        self.assertEqual(self.node.effort_pubs['left'].publish.call_count, 3)

    def test_invalid_description_blocks_motion(self):
        self.node.on_description(String(data='<robot name="other"><link name="base"/></robot>'))
        self.node.on_teleop('left', UInt8(data=1))
        self.node.on_trajectory('left', self.msg)
        self.node.pubs['left'].publish.assert_not_called()


if __name__ == '__main__':
    unittest.main()
