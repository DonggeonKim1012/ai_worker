# SH5 bringdown and mini-leader final pose

`ros2 launch ffw_bringup ffw_lg2_mini_leader_ai.launch.py` starts the recovered
physical mini-leader model, controllers, and the final-pose/bringdown receiver.
Its joystick configuration reserves the axes for pose gestures instead of
head/lift/base jogging. Alternatively, use an existing leader and run
`ros2 launch ffw_bringup sh5_final_pose.launch.py` independently. Use only one
receiver; `launch_final_pose:=false` disables the receiver in the mini launch.

After each stick has been neutral, push the **left stick left** for 0.3 seconds
to move only the left arm and fingers; push the **right stick right** to move
only the right arm and fingers. Held sticks fire once. Both sides can be
selected in the same gesture sample. While an operation is running, another
request is rejected with status; return to neutral and retry after completion.
The recovered left-Y reversal maps physical left to positive normalized Y;
both outward gesture signs are therefore +1. Axis indices/signs and thresholds are configurable in `bgf_endpose.yaml`.

The reconstructed `bgf_waypoint1_endpose.json` uses Task 650's released finger
positions (small recorded offsets outside URDF limits bounded to the joint limits;
original values are recorded in the JSON) and arm targets `[-0.9, 0, 0, -1.8, 0, 0.9, 0]` rad on both sides.
Compared with Task 650's first reverse waypoint, shoulder flexion raises the
elbow and folded forearm brings the hands in front of the head. URDF forward
kinematics places the wrist about 0.492 m forward and 0.077 m above the arm
base (±0.228 m laterally); the fingers extend above the wrist. These are newly
constructed targets, not recovered recorded poses. Joint limits and interpolation
were checked; the physical eye alignment and swept collision path have not
been tested on hardware. Adjust the JSON targets after reviewing the pose.

To request bringdown:

```bash
ros2 service call /ffw/bringdown std_srvs/srv/Trigger '{}'
```

Order: measured current pose → raised final pose → Task 650 `task_start` →
`step1` → `step0` → `arms_down` (all seven arm joints zero, straight downward).
Hands retain Task 650's released finger target after the first phase. Head and
lift retain their measured controller targets. Each phase uses quintic position
samples at a configured maximum 0.25 rad/s, FollowJointTrajectory actions,
and fresh per-joint measurements; no phase advances without measured settling.
Hand goal settling and each waypoint's measured confirmation allow **60 seconds**;
arm goal settling allows 20 seconds. Tolerances are not widened. Missing/stale
feedback, goal rejection, or timeout cancels accepted goals and prevents later
shutdown steps.

Before movement the receiver pauses the preset bridge (if present) and
deactivates the leader arm trajectory broadcaster, preventing competing hand
or arm commands. After final pose, these producers remain paused so returning
the stick to neutral cannot jump the arms back to the leader pose. Re-enable
teleoperation explicitly when ready. Current limits of 600 mA are sent for each
selected hand before its action goal; this is a current limit, not forced current.

Only after the final downward pose is confirmed does bringdown deactivate all
active leader/follower controllers. It then stops the s6 navigation service,
the follower service (which terminates its controller manager and launch
process), and finally the avatar service. Service names are configurable with
`shutdown_services`; default names match the current container. Missing required
supervisor services are rejected before movement. This does not stop the Docker
container or Cyclo manager. Launching the receiver independently keeps it alive
to report final status; if it is inside the avatar supervisor, stopping avatar
also stops the receiver as the last shutdown step.

The reconstructed Task 650 startup file is installed and can be selected with
`init_position_file:=ffw_sh5_follower_initial_positions_Task_000650.yaml` on the
existing follower launch. Bringdown always uses this explicit profile.
