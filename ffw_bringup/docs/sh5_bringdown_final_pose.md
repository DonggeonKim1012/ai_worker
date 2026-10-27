# SH5 bringdown and opt-in task final pose

The follower launch starts one bringdown receiver by default. Do not start a
second receiver from the leader. `launch_bringdown:=false` explicitly disables it.

```bash
ros2 launch ffw_bringup ffw_sh5_follower_ai.launch.py init_position:=true launch_cameras:=true
ros2 service call /ffw/bringdown std_srvs/srv/Trigger '{}'
```

Bringdown always follows **measured current state → task_start → step1 → step0
→ arms_down**. Both original retraction/folding steps are preserved exactly from
`config/ffw_sh5_rev1_follower/ffw_sh5_follower_initial_positions_Task_000650.yaml`.
Only the separate raised final pose is excluded. Do not remove step1 because it
is numerically close to task_start. By default, bringdown commands and verifies
**arms only** (`bringdown_control_hands:=false`). It sends no finger trajectory
or finger-current command and does not wait for finger feedback/action servers.
Existing hand-controller holding targets and head/lift targets are not changed.
This does not repair a faulty finger or make a grasped object safe to lower:
check hand/object clearance before requesting the arm sequence.

For a healthy hand, `bringdown_control_hands:=true` explicitly restores the old
released-hand targets and their checks. Neither setting changes task final pose.
Action results AND fresh measured arm settling remain required before advancing;
failure cancels accepted goals and does not continue shutdown. New settings take
effect after restarting the receiver/follower, not in an already running process.

Bringdown globally pauses the hand bridge and disables competing leader command
controllers. After the final downward pose is confirmed it disables controllers
and stops services (s6 deployment) or its own parent launch (standalone deployment).
It is not emergency stop, and it cannot operate through disconnected/failed motors.
Do not use it while initialization is still actively controlling the joints.

## Final pose is a separate, disabled-by-default feature

```bash
ros2 launch ffw_bringup ffw_sh5_follower_ai.launch.py task_name:=Task_000650
# Single-board A3, explicitly paired with SH5:
ros2 launch ffw_bringup ffw_a3_ai.launch.py robot_type:=sh5 port_name:=/dev/left_leader
# Or the opt-in two-board LG2 profile:
ros2 launch ffw_bringup ffw_lg2_mini_leader_recording.launch.py launch_final_pose:=false
```

Without `task_name`, final-pose services reject requests and joystick axes retain
normal behavior. With an approved task, neutral first, then left stick outward
left / right stick outward right for 0.3 seconds selects that side's arm and hand.
`config/tasks/Task_000650.yaml` references the operator-approved existing
`bgf_waypoint1_endpose.json`. New tasks add their own YAML; unknown task names fail.
The JSON targets are not newly measured eye-height coordinates. Verify physical
axis signs and clearance after changing leader boards before testing motion.

The selected side is held by the C++ bridge while the opposite side stays available.
After success, deliberately disable and re-enable that side's teleop to resume.
No controller shutdown or bringdown sequence occurs. A failed move leaves that
side held. Both gestures in one sample select both sides; a new request while a
move is busy is rejected, requiring neutral and retry.

Task selection does not change initialization. `init_position_file` remains the
separate explicit startup-trajectory option. Neither new pose path was physically
executed during the 2026-10-15 timing/mapping checks; those used init_position=false
with teleop inactive. Software checks are not swept-volume collision validation.
