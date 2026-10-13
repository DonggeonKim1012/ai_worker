# SH5 hand presets

The recovered catalog supplies presets 0–6, separate left/right selection,
per-preset open poses, trigger interpolation, and current limits. Preset 5 is
the default. The missing model has been implemented in `hand_preset_model.py`.

After building and sourcing the workspace:

```bash
ros2 launch ffw_bringup hand_preset.launch.py
ros2 service call /leader/hand_preset/set rcl_interfaces/srv/SetParametersAtomically \
  '{parameters: [{name: side, value: {type: 4, string_value: both}}, {name: preset_id, value: {type: 2, integer_value: 1}}]}'
```

Release the trigger before changing presets. Selection alone publishes no hand
motion. `/leader/hand_preset/status` publishes a transient-local JSON catalog.
Services `custom/save`, `manage/update`, `manage/delete`, and `manage/restore`
use the same parameter service type. Custom save accepts `name`, `description`,
and five `curls` (double array, range 0–1). IDs start at 100. Custom presets and
metadata persist atomically in `/workspace/hand_presets/sh5_hand_presets.json`.
Built-in or selected presets cannot be deleted; deletion can be undone for 10 seconds.

The bridge receives `/leader/joint_trajectory_command_broadcaster_left/joint_trajectory`
and its right counterpart. Outputs match main's SH5 hand-controller remappings.
A valid follower `/robot_description` with all finger limits is required before
any motion. The default also requires fresh UInt8 value 1 on
`/leader/left_teleop_state` and `/leader/right_teleop_state`, as in the recovered
leader controller. Current main does not publish these heartbeats. For main's
broadcaster, which publishes trajectories only while enabled, explicitly launch
with `require_teleop_heartbeat:=false` and set `trigger_min`/`trigger_max` to the
actual broadcaster output endpoints (including its offsets). The defaults
−0.1 and 1.1 belong to the recovered calibrated broadcaster, not raw angles.
This launch starts only the bridge; it does not start or reconfigure controllers.

An optional `endpose_file` can supply a validated `ffw_sh5_rev1` joint JSON.
Save-state value 5 then ramps from fresh measured fingers, stops on stale
save-state input, and holds the configured current limit. Site-specific BGF
poses and leader hardware changes are not required by the preset catalog.
