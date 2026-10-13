# 1109 SH5 navigation tuning — 2026-09-23

The active launch is `ffw_navigation/navigation.launch.py` with `navigation.yaml`, not the optional `navigation_mppi.yaml` preset. Changes were loaded into the running Nav2 stack on map `bgf_0923_3`. No physical movement goal was sent for validation.

## Findings and changes

| Area | Observed before | Applied |
| --- | --- | --- |
| Controller | `RegulatedPurePursuitController`, `use_rotate_to_heading: true` | Direct MPPI `Omni` under the same `FollowPath` controller ID; no rotate-to-path, PathAngle or PreferForward critic |
| Command pipeline | Velocity smoother clamped lateral velocity to zero | Symmetric X/Y limits of ±0.35 m/s, yaw ±0.7 rad/s, matching acceleration limits |
| Final corrections | Smoother discarded commands below 0.03 m/s or rad/s | Smoother deadband zero; base controller's existing small deadband remains |
| AMCL model | Differential, updates after 0.35 m / 0.3 rad | Omni, updates after 0.02 m / 0.02 rad |
| AMCL sampling | 400–1,200 particles, 40 laser beams | 800–2,000 adaptive particles, 80 beams, resample every update; sigma_hit 0.2 |
| Inflation | Radius 0.70 m, decay factor 3 | Radius 0.55 m, decay factor 5; physical 17-point footprint and 0.02 m padding retained |
| Local costmap | 0.05 m cells, 5 Hz update | 0.025 m cells, 10 Hz update; global map remains at its native 0.05 m resolution |
| Near obstacles | 0.35 m minimum marking range in default config | 0.05 m, matching the merged scan minimum so nearby real obstacles are not discarded |
| BT acknowledgement | 20 ms action acknowledgement timeout | 1,000 ms |
| Progress | 0.05 m / 0.05 rad required within 15 s | 0.02 m / 0.02 rad within 20 s; controller failure tolerance 1 s |
| Arrival requirement | 0.025 m / 0.02 rad in Nav2, 0.03 m in UI | Retained; success must still pass the UI pose check |

The observed abort log contains repeated `detected collision ahead`, `Controller patience exceeded`, and `Failed to make progress`, ending with a timeout acknowledging `compute_path_to_pose`. An aborted action can return `error_code: 0` when no specific BT error was populated. The supervisor API now labels this explicitly and includes nonempty `error_msg` text. A zero code does not override the ABORTED action status.

The optional `navigation_mppi.yaml` received matching localization, inflation, progress and smoother settings. Its existing explicit Omni/Curve controller selection is preserved; the currently active default is the direct Omni `FollowPath` above.

## Validation

- Live ROS parameter readback confirmed MPPI Omni, all velocity axes, AMCL settings, inflation and local resolution.
- Diagnostic regression tests: 7 passed.
- Installed controller and velocity smoother were tested in ROS domain 130 with Fast DDS and dedicated `/sh5_validation/*` command topics. The real robot uses domain 30 with Zenoh. A simulated base integrated only the isolated smoothed commands.

| Isolated test | Final XY error | Final yaw error | Result |
| --- | ---: | ---: | --- |
| 0.4 m lateral move, keep heading | 1.82 cm | 0.16° | SUCCEEDED; positive Y command, no pre-turn |
| 0.4 m reverse move, keep heading | 1.86 cm | 0.09° | SUCCEEDED; negative X command, no pre-turn |
| Small position adjustment plus final yaw | 0.56 cm | 0.81° | SUCCEEDED |

These tests use ideal odometry and an obstacle-free scan. They do not establish physical tracking accuracy or obstacle avoidance in the actual room. Two transient loop-rate warnings occurred during the isolated test; all three cases converged successfully.

After restoring the stationary robot's measured pose and processing scans, AMCL reported 801 particles and XY standard deviations of approximately 5.7 cm and 7.1 cm (yaw 4.4°). These are filter estimates, not ground-truth measurements. Physical accuracy within 3 cm still needs a measured real run; increasing particles alone does not establish it. The real odometry twist remained zero during the final readback.

## RViz

Run from the host:

```bash
/home/robotis/ai_worker/ffw_navigation/scripts/open_sh5_navigation_rviz.sh
```

The window opens on the existing noVNC desktop, accessible on the same host as the 7080 UI at port **8090**, path `/vnc.html`.

The saved view is `rviz/sh5_navigation_debug.rviz`. It includes map, merged laser, local/global costmap and footprint, global path, AMCL particles and pose uncertainty, wheel odometry, swerve markers, and the full robot model. Global costmap, wheel odometry and the heavy full robot model can be toggled on in Displays; the default view prioritizes live 2D navigation rendering.

RViz runs inside `novnc-server` because its Xvfb display uses a private IPC namespace. Running software OpenGL across the robot-container boundary produced a black viewport. The launcher ensures the Zenoh middleware and Nav2 RViz plugins are present and copies the robot/camera description resources, including aliases for absolute file paths in the published URDF. This also makes the setup repeatable after desktop-container recreation.

## References

- [Nav2 AMCL configuration](https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/others/configuring_amcl/)
- [Nav2 controller tuning guide](https://docs.nav2.org/rolling/configuration_and_development/tuning_guide/)
- [Nav2 BT Navigator configuration](https://docs.nav2.org/rolling/configuration_and_development/configuration_guide/core_servers/configuring_bt_navigator/)
