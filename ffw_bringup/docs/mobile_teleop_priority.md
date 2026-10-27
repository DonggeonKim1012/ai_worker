# Optional Cyclo mobile teleop with leader priority

The A3 leader is unchanged. Its `/cmd_vel` stream has priority over the
separate Cyclo UI stream `/cyclo/mobile_teleop/cmd_vel`. Do not put both
publishers on `/cmd_vel`: idle leader zeros overwrite the UI command.

Enable `mobile_teleop_mux:=true` on `ffw_sh5_follower_ai.launch.py` and set
Cyclo's `window.__CYCLO_CONFIG__.mobileTeleopTopic` to
`/cyclo/mobile_teleop/cmd_vel`. Both sides must be enabled together.
The follower then subscribes to `/ffw/mobile/cmd_vel`, produced by the mux.
The launch default remains false, and Cyclo's default remains `/cmd_vel`.

- Nonzero leader/navigation commands take priority immediately.
- Idle primary zeros do not suppress UI commands.
- After primary intervention, allow 0.3 seconds of neutral, release the UI
  control, then press it again. Holding the old UI button cannot resume motion.
- UI messages expire after 0.5 seconds. If an established primary source
  disappears for 0.5 seconds, stop and require UI release/repress after recovery.
- The output is published at 50 Hz. The existing base controller's timeout
  stops motion if the mux itself disappears. This is not an emergency stop.

No runtime or primary-leader restart is performed by installing these files.
Apply the paired configuration only while the robot is safely stopped.
Validate real motion with the emergency stop ready. Policy and isolated ROS
transport tests do not establish physical braking or obstacle safety.

## Head and lift UI jog

Enable `upper_body_teleop_mux:=true` with Cyclo's runtime setting
`upperBodyTeleopPriority: true`. UI trajectories then use
`/cyclo/upper_body/{head,lift}/joint_trajectory`, and the corresponding
controllers subscribe to `/ffw/ui_priority/{head,lift}/joint_trajectory`.
Both settings default off for existing deployments.

A per-ROS-domain lock prevents duplicate mux publishers. A mux started for a
controller-only hot reload is reused by a subsequent follower launch; it lives
until stopped or the container exits. Restart that instance after code updates.

The A3 source topics are unchanged. Until a UI jog is accepted, leader commands
pass through unchanged. While the UI owns a target, repeated identical leader
hold values are suppressed. A changed leader target or active leader joystick
immediately restores leader priority; a UI command is never queued for later.

UI requests require fresh measured joints and stationary odometry, valid SH5
joint limits and a bounded jog step/duration. Head jogs run no faster than
0.2 rad/s and lift jogs no faster than 0.05 m/s. These are bounded position
commands, not continuous velocity commands or an emergency-stop mechanism.
The existing recorded raw leader topics do not include these separate UI jogs.

## A3 vertical controls for Task_000911

Start the A3 leader with both `robot_type:=sh5 task_name:=Task_000911`.
Only this exact combination loads `config/ffw_a3/Task_000911_joystick.yaml`.
An empty or different task name retains the legacy A3 behavior; the follower's
task name alone does not select this leader mapping.

- Physical vertical sticks use sensor X, not sensor Y, on the existing A3 board.
  Left vertical uses the existing reversed-X calibration: forward is negative X.
  Right vertical retains the existing lift sign: positive X raises the lift.
- Full deflection requests at most 0.10 m/s base speed or a 0.03 m/s lift target
  increment; actual motion depends on the follower controller. Lift targets
  accumulate at that rate, with outstanding travel limited to 5 mm from fresh
  measured position (no windup). Release/reversal resets to measured position.
  Targets are clamped to [-0.5, 0.0] m. Confirm directions after changing boards.
- Also launch the SH5 follower with `task_name:=Task_000911` to load the matching
  base-controller override (`Task_000911_base_controller.yaml`): linear command
  deadband 0.01 m/s instead of the legacy 0.10 m/s. Without it, nearly all of the
  task's capped 0.10 m/s stick range is discarded. Maximum speed is unchanged.
- No lateral base, yaw, or head trajectory is sent by this task mapping.
  Horizontal axes remain available to an independently configured final-pose
  receiver; joystick button/recording events are unchanged.
- Neutral is required at startup and after stale joint feedback (>0.5 s).
  Recording-finish randomization is disabled for this task.
- Idle lift targets are not repeatedly published, so UI jogging can retain its
  target. The upper-body mux uses the joystick stream as its leader heartbeat.

This task-specific joystick configuration does not create or alter a task's
initial pose or final pose. Keep the emergency stop ready for physical tests.
