# 1109 BGF navigation 파라미터 위치와 공식 값

BGF 커밋 `5745b7a5f15f236e51cd9d9a0cd3c3f776ea129c`로 복원한 설정을 기준으로 한다. 공식 비교 커밋은 `9bc7f7b93ee118f4f3f47016d2f2314c0d0895e4`이다. 줄번호는 2026년 10월 6일 기준이다. 이후 편집으로 줄번호가 바뀌면 전체 파라미터 경로 또는 마지막 키를 검색한다.

“파일에 명시 없음”은 플러그인 기본값이나 코드 동작을 따르는 경우이며 0 또는 비활성을 뜻하지 않는다. ROS 파일의 반복 `/**` 블록을 각각 처리했다. 명시된 값과 실제 사용 여부를 구분한다.

**ffw_navigation/config/navigation_mppi_1109.yaml — Run 기본**

| 파라미터 경로 | 현재 파일 위치 | BGF 값 | 공식 파일 명시값 | 차이와 주의사항 |
|---|---|---|---|---|
| `amcl.ros__parameters.alpha1` | [439](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:439) | `0.4` | `0.4` | 공식과 동일 |
| `amcl.ros__parameters.alpha2` | [440](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:440) | `0.4` | `0.4` | 공식과 동일 |
| `amcl.ros__parameters.alpha3` | [441](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:441) | `0.4` | `0.4` | 공식과 동일 |
| `amcl.ros__parameters.alpha4` | [442](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:442) | `0.4` | `0.4` | 공식과 동일 |
| `amcl.ros__parameters.alpha5` | [443](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:443) | `0.4` | `0.4` | 공식과 동일 |
| `amcl.ros__parameters.always_reset_initial_pose` | [478](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:478) | `false` | `false` | 공식과 동일 |
| `amcl.ros__parameters.base_frame_id` | [444](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:444) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `amcl.ros__parameters.beam_skip_distance` | [445](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:445) | `0.5` | `0.5` | 공식과 동일 |
| `amcl.ros__parameters.beam_skip_error_threshold` | [446](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:446) | `0.9` | `0.9` | 공식과 동일 |
| `amcl.ros__parameters.beam_skip_threshold` | [447](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:447) | `0.3` | `0.3` | 공식과 동일 |
| `amcl.ros__parameters.do_beamskip` | [448](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:448) | `false` | `false` | 공식과 동일 |
| `amcl.ros__parameters.first_map_only` | [479](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:479) | `false` | `false` | 공식과 동일 |
| `amcl.ros__parameters.global_frame_id` | [449](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:449) | `"map"` | `"map"` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.x` | [481](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:481) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.y` | [482](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:482) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.yaw` | [484](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:484) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.z` | [483](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:483) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.lambda_short` | [450](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:450) | `0.1` | `0.1` | 공식과 동일 |
| `amcl.ros__parameters.laser_likelihood_max_dist` | [451](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:451) | `2.0` | `2.0` | 공식과 동일 |
| `amcl.ros__parameters.laser_max_range` | [452](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:452) | `100.0` | `100.0` | 공식과 동일 |
| `amcl.ros__parameters.laser_min_range` | [453](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:453) | `-1.0` | `-1.0` | 공식과 동일 |
| `amcl.ros__parameters.laser_model_type` | [454](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:454) | `"likelihood_field"` | `"likelihood_field"` | 공식과 동일 |
| `amcl.ros__parameters.map_topic` | [476](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:476) | `"map"` | `"map"` | 공식과 동일 |
| `amcl.ros__parameters.max_beams` | [455](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:455) | `80` | `60` | 변경 |
| `amcl.ros__parameters.max_particles` | [456](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:456) | `2000` | `2000` | 공식과 동일 |
| `amcl.ros__parameters.min_particles` | [457](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:457) | `800` | `500` | 변경 |
| `amcl.ros__parameters.odom_frame_id` | [458](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:458) | `"odom"` | `"odom"` | 공식과 동일 |
| `amcl.ros__parameters.pf_err` | [459](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:459) | `0.05` | `0.05` | 공식과 동일 |
| `amcl.ros__parameters.pf_z` | [460](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:460) | `0.99` | `0.99` | 공식과 동일 |
| `amcl.ros__parameters.recovery_alpha_fast` | [461](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:461) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.recovery_alpha_slow` | [462](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:462) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.resample_interval` | [463](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:463) | `1` | `1` | 공식과 동일 |
| `amcl.ros__parameters.robot_model_type` | [464](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:464) | `"nav2_amcl::OmniMotionModel"` | `"nav2_amcl::OmniMotionModel"` | 공식과 동일 |
| `amcl.ros__parameters.save_pose_rate` | [465](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:465) | `0.5` | `0.5` | 공식과 동일 |
| `amcl.ros__parameters.scan_topic` | [475](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:475) | `"/scan"` | `"/scan"` | 공식과 동일 |
| `amcl.ros__parameters.set_initial_pose` | [477](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:477) | `true` | `true` | 공식과 동일 |
| `amcl.ros__parameters.sigma_hit` | [466](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:466) | `0.2` | `0.2` | 공식과 동일 |
| `amcl.ros__parameters.tf_broadcast` | [467](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:467) | `true` | `true` | 공식과 동일 |
| `amcl.ros__parameters.transform_tolerance` | [468](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:468) | `1.0` | `1.0` | 공식과 동일 |
| `amcl.ros__parameters.update_min_a` | [469](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:469) | `0.02` | `0.01` | 변경 |
| `amcl.ros__parameters.update_min_d` | [470](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:470) | `0.02` | `0.25` | 변경 |
| `amcl.ros__parameters.z_hit` | [471](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:471) | `0.5` | `0.5` | 공식과 동일 |
| `amcl.ros__parameters.z_max` | [472](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:472) | `0.05` | `0.05` | 공식과 동일 |
| `amcl.ros__parameters.z_rand` | [473](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:473) | `0.5` | `0.5` | 공식과 동일 |
| `amcl.ros__parameters.z_short` | [474](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:474) | `0.05` | `0.05` | 공식과 동일 |
| `behavior_server.ros__parameters.assisted_teleop.plugin` | [341](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:341) | `"nav2_behaviors::AssistedTeleop"` | `"nav2_behaviors::AssistedTeleop"` | 공식과 동일 |
| `behavior_server.ros__parameters.backup.plugin` | [335](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:335) | `"nav2_behaviors::BackUp"` | `"nav2_behaviors::BackUp"` | 공식과 동일 |
| `behavior_server.ros__parameters.behavior_plugins` | [331](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:331) | `["spin", "backup", "drive_on_heading", "assisted_teleop", "wait"]` | `["spin", "backup", "drive_on_heading", "assisted_teleop", "wait"]` | 공식과 동일 |
| `behavior_server.ros__parameters.cycle_frequency` | [330](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:330) | `10.0` | `10.0` | 공식과 동일 |
| `behavior_server.ros__parameters.drive_on_heading.plugin` | [337](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:337) | `"nav2_behaviors::DriveOnHeading"` | `"nav2_behaviors::DriveOnHeading"` | 공식과 동일 |
| `behavior_server.ros__parameters.global_costmap_topic` | [327](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:327) | `"global_costmap/costmap_raw"` | `"global_costmap/costmap_raw"` | 공식과 동일 |
| `behavior_server.ros__parameters.global_footprint_topic` | [329](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:329) | `"global_costmap/published_footprint"` | `"global_costmap/published_footprint"` | 공식과 동일 |
| `behavior_server.ros__parameters.global_frame` | [343](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:343) | `"map"` | `"map"` | 공식과 동일 |
| `behavior_server.ros__parameters.local_costmap_topic` | [326](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:326) | `"local_costmap/costmap_raw"` | `"local_costmap/costmap_raw"` | 공식과 동일 |
| `behavior_server.ros__parameters.local_footprint_topic` | [328](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:328) | `"local_costmap/published_footprint"` | `"local_costmap/published_footprint"` | 공식과 동일 |
| `behavior_server.ros__parameters.local_frame` | [342](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:342) | `"odom"` | `"odom"` | 공식과 동일 |
| `behavior_server.ros__parameters.max_rotational_vel` | [347](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:347) | `1.0` | `1.0` | 공식과 동일 |
| `behavior_server.ros__parameters.min_rotational_vel` | [348](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:348) | `0.4` | `0.4` | 공식과 동일 |
| `behavior_server.ros__parameters.robot_base_frame` | [344](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:344) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `behavior_server.ros__parameters.rotational_acc_lim` | [349](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:349) | `3.2` | `3.2` | 공식과 동일 |
| `behavior_server.ros__parameters.simulate_ahead_time` | [346](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:346) | `2.0` | `2.0` | 공식과 동일 |
| `behavior_server.ros__parameters.spin.plugin` | [333](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:333) | `"nav2_behaviors::Spin"` | `"nav2_behaviors::Spin"` | 공식과 동일 |
| `behavior_server.ros__parameters.transform_tolerance` | [345](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:345) | `0.3` | `0.3` | 공식과 동일 |
| `behavior_server.ros__parameters.wait.plugin` | [339](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:339) | `"nav2_behaviors::Wait"` | `"nav2_behaviors::Wait"` | 공식과 동일 |
| `bt_navigator.ros__parameters.action_server_result_timeout` | [9](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:9) | `900.0` | `900.0` | 공식과 동일 |
| `bt_navigator.ros__parameters.bt_loop_duration` | [6](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:6) | `10` | `10` | 공식과 동일 |
| `bt_navigator.ros__parameters.default_nav_through_poses_bt_xml` | [16](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:16) | `"$(find-pkg-share ffw_navigation)/config/bt/nav_modes_1109.xml"` | `"$(find-pkg-share ffw_navigation)/config/bt/nav_modes.xml"` | 변경 |
| `bt_navigator.ros__parameters.default_nav_to_pose_bt_xml` | [15](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:15) | `"$(find-pkg-share ffw_navigation)/config/bt/nav_modes_1109.xml"` | `"$(find-pkg-share ffw_navigation)/config/bt/nav_modes.xml"` | 변경 |
| `bt_navigator.ros__parameters.default_server_timeout` | [7](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:7) | `1000` | `20` | 변경 |
| `bt_navigator.ros__parameters.error_code_names` | [20](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:20) | `["compute_path_error_code", "follow_path_error_code"]` | `["compute_path_error_code", "follow_path_error_code"]` | 공식과 동일 |
| `bt_navigator.ros__parameters.global_frame` | [3](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:3) | `"map"` | `"map"` | 공식과 동일 |
| `bt_navigator.ros__parameters.navigate_through_poses.plugin` | [14](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:14) | `"nav2_bt_navigator::NavigateThroughPosesNavigator"` | `"nav2_bt_navigator::NavigateThroughPosesNavigator"` | 공식과 동일 |
| `bt_navigator.ros__parameters.navigate_to_pose.plugin` | [12](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:12) | `"nav2_bt_navigator::NavigateToPoseNavigator"` | `"nav2_bt_navigator::NavigateToPoseNavigator"` | 공식과 동일 |
| `bt_navigator.ros__parameters.navigators` | [10](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:10) | `["navigate_to_pose", "navigate_through_poses"]` | `["navigate_to_pose", "navigate_through_poses"]` | 공식과 동일 |
| `bt_navigator.ros__parameters.odom_topic` | [5](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:5) | `"/odom"` | `"/odom"` | 공식과 동일 |
| `bt_navigator.ros__parameters.plugin_lib_names` | [18](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:18) | `["is_path_length_under_plugin"]` | `["is_path_length_under_plugin", "nav2_behavior_tree"]` | 변경 |
| `bt_navigator.ros__parameters.robot_base_frame` | [4](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:4) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `bt_navigator.ros__parameters.wait_for_service_timeout` | [8](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:8) | `1000` | `1000` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.action_type` | [392](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:392) | `"approach"` | `"approach"` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.enabled` | [398](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:398) | `false` | `false` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.footprint_topic` | [393](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:393) | `"/local_costmap/published_footprint"` | `"/local_costmap/published_footprint"` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.min_points` | [396](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:396) | `6` | `6` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.simulation_time_step` | [395](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:395) | `0.1` | `0.1` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.time_before_collision` | [394](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:394) | `1.0` | `1.0` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.type` | [391](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:391) | `"polygon"` | `"polygon"` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.visualize` | [397](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:397) | `false` | `false` | 공식과 동일 |
| `collision_monitor.ros__parameters.base_frame_id` | [380](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:380) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `collision_monitor.ros__parameters.base_shift_correction` | [387](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:387) | `true` | `true` | 공식과 동일 |
| `collision_monitor.ros__parameters.cmd_vel_in_topic` | [382](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:382) | `"cmd_vel_smoothed"` | `"cmd_vel_smoothed"` | 공식과 동일 |
| `collision_monitor.ros__parameters.cmd_vel_out_topic` | [383](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:383) | `"cmd_vel"` | `"cmd_vel"` | 공식과 동일 |
| `collision_monitor.ros__parameters.observation_sources` | [399](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:399) | `["scan"]` | `["scan"]` | 공식과 동일 |
| `collision_monitor.ros__parameters.odom_frame_id` | [381](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:381) | `"odom"` | `"odom"` | 공식과 동일 |
| `collision_monitor.ros__parameters.polygons` | [389](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:389) | `["FootprintApproach"]` | `["FootprintApproach"]` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.enabled` | [405](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:405) | `true` | `true` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.max_height` | [404](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:404) | `2.0` | `2.0` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.min_height` | [403](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:403) | `0.15` | `0.15` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.topic` | [402](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:402) | `"scan"` | `"scan"` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.type` | [401](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:401) | `"scan"` | `"scan"` | 공식과 동일 |
| `collision_monitor.ros__parameters.source_timeout` | [386](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:386) | `1.0` | `1.0` | 공식과 동일 |
| `collision_monitor.ros__parameters.state_topic` | [384](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:384) | `"collision_monitor_state"` | `"collision_monitor_state"` | 공식과 동일 |
| `collision_monitor.ros__parameters.stop_pub_timeout` | [388](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:388) | `2.0` | `2.0` | 공식과 동일 |
| `collision_monitor.ros__parameters.transform_tolerance` | [385](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:385) | `0.2` | `0.2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.ConstraintCritic.cost_power` | [147](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:147) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.ConstraintCritic.cost_weight` | [148](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:148) | `4.0` | `4.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.ConstraintCritic.enabled` | [146](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:146) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.collision_cost` | [173](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:173) | `1000000.0` | `1000000.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.consider_footprint` | [172](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:172) | `true` | `false` | 변경 |
| `controller_server.ros__parameters.CurveController.CostCritic.cost_power` | [169](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:169) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.cost_weight` | [170](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:170) | `4.2` | `4.2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.critical_cost` | [171](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:171) | `300.0` | `300.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.enabled` | [168](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:168) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.near_goal_distance` | [174](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:174) | `1.0` | `1.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.trajectory_point_step` | [175](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:175) | `2` | `2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalAngleCritic.cost_power` | [157](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:157) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalAngleCritic.cost_weight` | [158](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:158) | `2.0` | `2.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalAngleCritic.enabled` | [156](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:156) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalAngleCritic.threshold_to_consider` | [159](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:159) | `0.3` | `0.3` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalCritic.cost_power` | [151](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:151) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalCritic.cost_weight` | [152](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:152) | `5.0` | `5.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalCritic.enabled` | [150](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:150) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalCritic.threshold_to_consider` | [153](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:153) | `1.2` | `1.2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.cost_power` | [179](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:179) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.cost_weight` | [180](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:180) | `14.0` | `14.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.enabled` | [178](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:178) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.max_path_occupancy_ratio` | [181](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:181) | `0.05` | `0.05` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.offset_from_furthest` | [184](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:184) | `15` | `15` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.threshold_to_consider` | [183](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:183) | `1.0` | `1.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.trajectory_point_step` | [182](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:182) | `2` | `2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.use_path_orientations` | [185](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:185) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.cost_power` | [196](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:196) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.cost_weight` | [197](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:197) | `6.0` | `6.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.enabled` | [195](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:195) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.max_angle_to_furthest` | [200](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:200) | `0.4` | `0.4` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.mode` | [201](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:201) | `0` | `0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.offset_from_furthest` | [198](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:198) | `3` | `3` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.threshold_to_consider` | [199](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:199) | `0.5` | `0.5` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathFollowCritic.cost_power` | [189](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:189) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathFollowCritic.cost_weight` | [190](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:190) | `6.0` | `6.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathFollowCritic.enabled` | [188](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:188) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathFollowCritic.offset_from_furthest` | [191](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:191) | `5` | `5` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathFollowCritic.threshold_to_consider` | [192](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:192) | `1.2` | `1.2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PreferForwardCritic.cost_power` | [163](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:163) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PreferForwardCritic.cost_weight` | [164](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:164) | `9.0` | `9.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PreferForwardCritic.enabled` | [162](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:162) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PreferForwardCritic.threshold_to_consider` | [165](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:165) | `0.5` | `0.5` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.TrajectoryVisualizer.time_step` | [135](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:135) | `3` | `3` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.TrajectoryVisualizer.trajectory_step` | [134](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:134) | `5` | `5` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.ax_max` | [124](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:124) | `0.5` | `파일에 명시 없음` | 변경 |
| `controller_server.ros__parameters.CurveController.ax_min` | [125](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:125) | `-0.5` | `파일에 명시 없음` | 변경 |
| `controller_server.ros__parameters.CurveController.ay_max` | [126](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:126) | `0.5` | `파일에 명시 없음` | 변경 |
| `controller_server.ros__parameters.CurveController.ay_min` | [127](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:127) | `-0.5` | `파일에 명시 없음` | 변경 |
| `controller_server.ros__parameters.CurveController.az_max` | [128](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:128) | `1.2` | `파일에 명시 없음` | 변경 |
| `controller_server.ros__parameters.CurveController.batch_size` | [114](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:114) | `1200` | `1200` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.critics` | [137](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:137) | `["ConstraintCritic", "CostCritic", "GoalCritic", "GoalAngleCritic", "PathAlignCritic", "PathFollowCritic", "PathAngleCritic", "PreferForwardCritic"]` | `["ConstraintCritic", "CostCritic", "GoalCritic", "GoalAngleCritic", "PathAlignCritic", "PathFollowCritic", "PathAngleCritic", "PreferForwardCritic"]` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.gamma` | [131](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:131) | `0.02` | `0.02` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.iteration_count` | [129](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:129) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.model_dt` | [113](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:113) | `0.05` | `0.05` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.motion_model` | [115](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:115) | `"Omni"` | `"Omni"` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.plugin` | [111](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:111) | `"nav2_mppi_controller::MPPIController"` | `"nav2_mppi_controller::MPPIController"` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.temperature` | [130](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:130) | `0.27` | `0.27` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.time_steps` | [112](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:112) | `40` | `40` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.visualize` | [132](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:132) | `false` | `false` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.vx_max` | [119](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:119) | `0.35` | `0.5` | 변경 |
| `controller_server.ros__parameters.CurveController.vx_min` | [120](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:120) | `0.0` | `0.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.vx_std` | [116](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:116) | `0.17` | `0.17` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.vy_max` | [121](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:121) | `0.25` | `0.25` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.vy_min` | [122](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:122) | `-0.25` | `-0.25` | MPPI 1.3.11은 vy_max를 대칭 상한으로 사용하며 vy_min을 읽지 않음 |
| `controller_server.ros__parameters.CurveController.vy_std` | [117](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:117) | `0.12` | `0.12` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.wz_max` | [123](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:123) | `0.7` | `1.6` | 변경 |
| `controller_server.ros__parameters.CurveController.wz_std` | [118](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:118) | `0.3` | `0.3` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.ConstraintCritic.cost_power` | [82](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:82) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.ConstraintCritic.cost_weight` | [83](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:83) | `4.0` | `4.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.ConstraintCritic.enabled` | [81](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:81) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.collision_cost` | [100](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:100) | `1000000.0` | `1000000.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.consider_footprint` | [99](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:99) | `true` | `false` | 변경 |
| `controller_server.ros__parameters.OmniController.CostCritic.cost_power` | [96](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:96) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.cost_weight` | [97](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:97) | `4.0` | `4.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.critical_cost` | [98](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:98) | `300.0` | `300.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.enabled` | [95](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:95) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.near_goal_distance` | [101](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:101) | `1.0` | `1.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.trajectory_point_step` | [102](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:102) | `2` | `2` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalAngleCritic.cost_power` | [91](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:91) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalAngleCritic.cost_weight` | [92](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:92) | `5.0` | `5.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalAngleCritic.enabled` | [90](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:90) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalAngleCritic.threshold_to_consider` | [93](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:93) | `0.25` | `0.25` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalCritic.cost_power` | [86](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:86) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalCritic.cost_weight` | [87](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:87) | `5.0` | `5.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalCritic.enabled` | [85](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:85) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalCritic.threshold_to_consider` | [88](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:88) | `1.2` | `1.2` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.PathFollowCritic.cost_power` | [105](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:105) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.PathFollowCritic.cost_weight` | [106](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:106) | `5.0` | `5.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.PathFollowCritic.enabled` | [104](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:104) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.PathFollowCritic.offset_from_furthest` | [107](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:107) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.PathFollowCritic.threshold_to_consider` | [108](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:108) | `1.2` | `1.2` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.TrajectoryVisualizer.time_step` | [73](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:73) | `3` | `3` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.TrajectoryVisualizer.trajectory_step` | [72](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:72) | `5` | `5` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.ax_max` | [62](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:62) | `0.5` | `3.0` | 변경 |
| `controller_server.ros__parameters.OmniController.ax_min` | [63](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:63) | `-0.5` | `-3.0` | 변경 |
| `controller_server.ros__parameters.OmniController.ay_max` | [64](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:64) | `0.5` | `3.0` | 변경 |
| `controller_server.ros__parameters.OmniController.ay_min` | [65](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:65) | `-0.5` | `-3.0` | 변경 |
| `controller_server.ros__parameters.OmniController.az_max` | [66](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:66) | `1.2` | `3.0` | 변경 |
| `controller_server.ros__parameters.OmniController.batch_size` | [51](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:51) | `1200` | `1200` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.critics` | [75](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:75) | `["ConstraintCritic", "CostCritic", "GoalCritic", "GoalAngleCritic", "PathFollowCritic"]` | `["ConstraintCritic", "CostCritic", "GoalCritic", "GoalAngleCritic", "PathFollowCritic"]` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.gamma` | [69](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:69) | `0.018` | `0.018` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.iteration_count` | [67](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:67) | `4` | `4` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.model_dt` | [50](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:50) | `0.05` | `0.05` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.motion_model` | [52](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:52) | `"Omni"` | `"Omni"` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.plugin` | [48](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:48) | `"nav2_mppi_controller::MPPIController"` | `"nav2_mppi_controller::MPPIController"` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.temperature` | [68](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:68) | `0.25` | `0.25` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.time_steps` | [49](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:49) | `40` | `40` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.visualize` | [70](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:70) | `false` | `false` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.vx_max` | [57](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:57) | `0.35` | `0.55` | 변경 |
| `controller_server.ros__parameters.OmniController.vx_min` | [58](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:58) | `-0.35` | `-0.55` | 변경 |
| `controller_server.ros__parameters.OmniController.vx_std` | [53](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:53) | `0.15` | `0.15` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.vy_max` | [59](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:59) | `0.35` | `0.55` | 변경 |
| `controller_server.ros__parameters.OmniController.vy_min` | [60](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:60) | `-0.35` | `-0.55` | MPPI 1.3.11은 vy_max를 대칭 상한으로 사용하며 vy_min을 읽지 않음 |
| `controller_server.ros__parameters.OmniController.vy_std` | [54](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:54) | `0.15` | `0.15` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.wz_max` | [61](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:61) | `0.7` | `0.8` | 변경 |
| `controller_server.ros__parameters.OmniController.wz_std` | [55](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:55) | `0.35` | `0.35` | 공식과 동일 |
| `controller_server.ros__parameters.controller_frequency` | [25](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:25) | `20.0` | `20.0` | 공식과 동일 |
| `controller_server.ros__parameters.controller_plugins` | [33](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:33) | `["OmniController", "CurveController"]` | `["OmniController", "CurveController"]` | 공식과 동일 |
| `controller_server.ros__parameters.failure_tolerance` | [30](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:30) | `1.0` | `0.3` | 변경 |
| `controller_server.ros__parameters.general_goal_checker.plugin` | [42](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:42) | `"nav2_controller::SimpleGoalChecker"` | `"nav2_controller::SimpleGoalChecker"` | 공식과 동일 |
| `controller_server.ros__parameters.general_goal_checker.stateful` | [45](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:45) | `false` | `true` | 변경 |
| `controller_server.ros__parameters.general_goal_checker.xy_goal_tolerance` | [43](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:43) | `0.025` | `0.2` | 변경 |
| `controller_server.ros__parameters.general_goal_checker.yaw_goal_tolerance` | [44](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:44) | `0.02` | `0.05` | 변경 |
| `controller_server.ros__parameters.goal_checker_plugins` | [32](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:32) | `["general_goal_checker"]` | `["general_goal_checker"]` | 공식과 동일 |
| `controller_server.ros__parameters.min_theta_velocity_threshold` | [29](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:29) | `0.001` | `0.001` | 공식과 동일 |
| `controller_server.ros__parameters.min_x_velocity_threshold` | [27](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:27) | `0.001` | `0.001` | 공식과 동일 |
| `controller_server.ros__parameters.min_y_velocity_threshold` | [28](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:28) | `0.001` | `0.001` | 공식과 동일 |
| `controller_server.ros__parameters.progress_checker.movement_time_allowance` | [40](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:40) | `20.0` | `10.0` | 변경 |
| `controller_server.ros__parameters.progress_checker.plugin` | [37](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:37) | `"nav2_controller::PoseProgressChecker"` | `"nav2_controller::SimpleProgressChecker"` | 변경 |
| `controller_server.ros__parameters.progress_checker.required_movement_angle` | [38](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:38) | `0.02` | `파일에 명시 없음` | 변경 |
| `controller_server.ros__parameters.progress_checker.required_movement_radius` | [39](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:39) | `0.02` | `0.5` | 변경 |
| `controller_server.ros__parameters.progress_checker_plugin` | 삭제된 키 | `파일에 명시 없음` | `"progress_checker"` | 변경 |
| `controller_server.ros__parameters.progress_checker_plugins` | [31](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:31) | `["progress_checker"]` | `파일에 명시 없음` | 변경 |
| `controller_server.ros__parameters.transform_tolerance` | [26](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:26) | `0.3` | `0.3` | 공식과 동일 |
| `docking_server.ros__parameters.controller.costmap_topic` | [430](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:430) | `"local_costmap/costmap_raw"` | `"local_costmap/costmap_raw"` | 공식과 동일 |
| `docking_server.ros__parameters.controller.dock_collision_threshold` | [435](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:435) | `0.3` | `0.3` | 공식과 동일 |
| `docking_server.ros__parameters.controller.footprint_topic` | [431](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:431) | `"local_costmap/published_footprint"` | `"local_costmap/published_footprint"` | 공식과 동일 |
| `docking_server.ros__parameters.controller.k_delta` | [426](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:426) | `2.0` | `2.0` | 공식과 동일 |
| `docking_server.ros__parameters.controller.k_phi` | [425](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:425) | `3.0` | `3.0` | 공식과 동일 |
| `docking_server.ros__parameters.controller.projection_time` | [433](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:433) | `5.0` | `5.0` | 공식과 동일 |
| `docking_server.ros__parameters.controller.simulation_step` | [434](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:434) | `0.1` | `0.1` | 공식과 동일 |
| `docking_server.ros__parameters.controller.transform_tolerance` | [432](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:432) | `0.1` | `0.1` | 공식과 동일 |
| `docking_server.ros__parameters.controller.use_collision_detection` | [429](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:429) | `true` | `true` | 공식과 동일 |
| `docking_server.ros__parameters.controller.v_linear_max` | [428](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:428) | `0.15` | `0.15` | 공식과 동일 |
| `docking_server.ros__parameters.controller.v_linear_min` | [427](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:427) | `0.15` | `0.15` | 공식과 동일 |
| `docking_server.ros__parameters.dock_plugins` | [409](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:409) | `["simple_charging_dock"]` | `["simple_charging_dock"]` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.docking_threshold` | [412](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:412) | `0.05` | `0.05` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_rotation_pitch` | [421](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:421) | `-1.57` | `-1.57` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_rotation_roll` | [420](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:420) | `-1.57` | `-1.57` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_rotation_yaw` | [422](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:422) | `0.0` | `0.0` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_timeout` | [417](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:417) | `1.0` | `1.0` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_translation_x` | [418](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:418) | `-0.18` | `-0.18` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_translation_y` | [419](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:419) | `0.0` | `0.0` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.filter_coef` | [423](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:423) | `0.1` | `0.1` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.plugin` | [411](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:411) | `"opennav_docking::SimpleChargingDock"` | `"opennav_docking::SimpleChargingDock"` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.staging_x_offset` | [413](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:413) | `-0.7` | `-0.7` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.use_battery_status` | [415](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:415) | `false` | `false` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.use_external_detection_pose` | [414](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:414) | `true` | `true` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.use_stall_detection` | [416](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:416) | `false` | `false` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.always_send_full_costmap` | [281](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:281) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.footprint` | [255](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:255) | `"[[0.25, 0.266], [0.25, -0.266], [0.24, -0.303], [0.216, -0.337], [0.163, -0.366], [0.112, -0.366], [-0.322, -0.236], [-0.363, -0.209], [-0.403, -0.052], [-0.403, 0.009], [-0.377, 0.166], [-0.362, 0.21], [-0.322, 0.236], [0.112, 0.366], [0.163, 0.366], [0.218, 0.335], [0.24, 0.303]]"` | `파일에 명시 없음` | 변경 |
| `global_costmap.global_costmap.ros__parameters.footprint_padding` | [256](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:256) | `0.02` | `파일에 명시 없음` | 변경 |
| `global_costmap.global_costmap.ros__parameters.global_frame` | [250](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:250) | `"map"` | `"map"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.inflation_layer.cost_scaling_factor` | [279](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:279) | `5.0` | `3.0` | 변경 |
| `global_costmap.global_costmap.ros__parameters.inflation_layer.inflation_radius` | [280](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:280) | `0.55` | `0.7` | 변경 |
| `global_costmap.global_costmap.ros__parameters.inflation_layer.plugin` | [278](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:278) | `"nav2_costmap_2d::InflationLayer"` | `"nav2_costmap_2d::InflationLayer"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.enabled` | [262](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:262) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.observation_sources` | [263](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:263) | `"scan"` | `"scan"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.plugin` | [261](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:261) | `"nav2_costmap_2d::ObstacleLayer"` | `"nav2_costmap_2d::ObstacleLayer"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.clearing` | [267](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:267) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.data_type` | [269](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:269) | `"LaserScan"` | `"LaserScan"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.marking` | [268](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:268) | `false` | `false` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.max_obstacle_height` | [266](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:266) | `2.0` | `2.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.obstacle_max_range` | [272](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:272) | `2.5` | `2.5` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.obstacle_min_range` | [273](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:273) | `0.0` | `0.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.raytrace_max_range` | [270](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:270) | `3.0` | `3.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.raytrace_min_range` | [271](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:271) | `0.0` | `0.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.topic` | [265](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:265) | `"/scan"` | `"/scan"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.plugins` | [259](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:259) | `["static_layer", "obstacle_layer", "inflation_layer"]` | `["static_layer", "obstacle_layer", "inflation_layer"]` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.publish_frequency` | [249](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:249) | `1.0` | `1.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.resolution` | [257](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:257) | `0.05` | `0.05` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.robot_base_frame` | [251](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:251) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.robot_radius` | 삭제된 키 | `파일에 명시 없음` | `0.44` | 변경 |
| `global_costmap.global_costmap.ros__parameters.static_layer.map_subscribe_transient_local` | [276](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:276) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.static_layer.plugin` | [275](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:275) | `"nav2_costmap_2d::StaticLayer"` | `"nav2_costmap_2d::StaticLayer"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.track_unknown_space` | [258](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:258) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.transform_tolerance` | [252](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:252) | `0.3` | `0.3` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.update_frequency` | [248](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:248) | `1.0` | `1.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.always_send_full_costmap` | [243](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:243) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.footprint` | [217](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:217) | `"[[0.25, 0.266], [0.25, -0.266], [0.24, -0.303], [0.216, -0.337], [0.163, -0.366], [0.112, -0.366], [-0.322, -0.236], [-0.363, -0.209], [-0.403, -0.052], [-0.403, 0.009], [-0.377, 0.166], [-0.362, 0.21], [-0.322, 0.236], [0.112, 0.366], [0.163, 0.366], [0.218, 0.335], [0.24, 0.303]]"` | `파일에 명시 없음` | 변경 |
| `local_costmap.local_costmap.ros__parameters.footprint_padding` | [218](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:218) | `0.02` | `파일에 명시 없음` | 변경 |
| `local_costmap.local_costmap.ros__parameters.global_frame` | [208](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:208) | `"odom"` | `"odom"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.height` | [213](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:213) | `3` | `3` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.inflation_layer.cost_scaling_factor` | [223](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:223) | `10.0` | `3.0` | 변경 |
| `local_costmap.local_costmap.ros__parameters.inflation_layer.inflation_radius` | [224](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:224) | `0.48` | `0.65` | 변경 |
| `local_costmap.local_costmap.ros__parameters.inflation_layer.plugin` | [221](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:221) | `"nav2_costmap_2d::InflationLayer"` | `"nav2_costmap_2d::InflationLayer"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.enabled` | [227](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:227) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.observation_sources` | [228](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:228) | `"scan"` | `"scan"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.plugin` | [226](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:226) | `"nav2_costmap_2d::ObstacleLayer"` | `"nav2_costmap_2d::ObstacleLayer"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.clearing` | [232](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:232) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.data_type` | [235](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:235) | `"LaserScan"` | `"LaserScan"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.inf_is_valid` | [233](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:233) | `true` | `파일에 명시 없음` | 변경 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.marking` | [234](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:234) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.max_obstacle_height` | [231](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:231) | `2.0` | `2.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.obstacle_max_range` | [238](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:238) | `2.5` | `2.5` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.obstacle_min_range` | [239](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:239) | `0.0` | `0.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.raytrace_max_range` | [236](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:236) | `3.0` | `3.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.raytrace_min_range` | [237](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:237) | `0.0` | `0.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.topic` | [230](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:230) | `"/scan"` | `"/scan"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.plugins` | [219](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:219) | `["obstacle_layer", "inflation_layer"]` | `["obstacle_layer", "inflation_layer"]` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.publish_frequency` | [207](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:207) | `2.0` | `2.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.resolution` | [214](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:214) | `0.025` | `0.05` | 변경 |
| `local_costmap.local_costmap.ros__parameters.robot_base_frame` | [209](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:209) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.robot_radius` | 삭제된 키 | `파일에 명시 없음` | `0.44` | 변경 |
| `local_costmap.local_costmap.ros__parameters.rolling_window` | [211](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:211) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.static_layer.map_subscribe_transient_local` | [242](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:242) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.static_layer.plugin` | [241](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:241) | `"nav2_costmap_2d::StaticLayer"` | `"nav2_costmap_2d::StaticLayer"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.transform_tolerance` | [210](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:210) | `0.3` | `0.3` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.update_frequency` | [206](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:206) | `10.0` | `5.0` | 변경 |
| `local_costmap.local_costmap.ros__parameters.width` | [212](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:212) | `3` | `3` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.allow_reverse` | [295](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:295) | `true` | `true` | Hybrid 1.3.11에서 이 키를 사용하지 않음 |
| `planner_server.ros__parameters.SmacPlannerHybrid.allow_unknown` | [291](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:291) | `true` | `true` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.analytic_expansion_ratio` | [297](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:297) | `1.0` | `1.0` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.angle_quantization_bins` | [296](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:296) | `24` | `24` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.cache_obstacle_heuristic` | [308](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:308) | `true` | `true` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.change_penalty` | [303](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:303) | `2.0` | `2.0` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.cost_heuristic_multiplier` | [301](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:301) | `2.5` | `2.5` | Hybrid 1.3.11에서 이 키를 사용하지 않음 |
| `planner_server.ros__parameters.SmacPlannerHybrid.cost_travel_multiplier` | [300](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:300) | `1.0` | `1.0` | Hybrid 1.3.11에서 이 키를 사용하지 않음 |
| `planner_server.ros__parameters.SmacPlannerHybrid.downsample_costmap` | [305](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:305) | `false` | `false` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.downsampling_factor` | [306](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:306) | `1` | `1` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.max_iterations` | [298](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:298) | `40000` | `40000` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.max_on_approach_iterations` | [299](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:299) | `12000` | `12000` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.minimum_turning_radius` | [293](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:293) | `0.0` | `0.0` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.motion_model_for_search` | [294](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:294) | `"REEDS_SHEPP"` | `"REEDS_SHEPP"` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.non_straight_penalty` | [302](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:302) | `10.5` | `10.5` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.plugin` | [289](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:289) | `"nav2_smac_planner::SmacPlannerHybrid"` | `"nav2_smac_planner::SmacPlannerHybrid"` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.rotation_penalty` | [304](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:304) | `1.5` | `1.5` | Hybrid 1.3.11에서 이 키를 사용하지 않음 |
| `planner_server.ros__parameters.SmacPlannerHybrid.smooth_path` | [307](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:307) | `true` | `true` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.smoother.max_iterations` | [310](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:310) | `800` | `800` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.smoother.tolerance` | [313](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:313) | `1e-10` | `1e-10` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.smoother.w_data` | [312](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:312) | `0.05` | `0.05` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.smoother.w_smooth` | [311](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:311) | `0.9` | `0.9` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.tolerance` | [290](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:290) | `0.0` | `0.5` | 변경 |
| `planner_server.ros__parameters.SmacPlannerHybrid.use_final_approach_orientation` | [292](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:292) | `false` | `false` | Hybrid 1.3.11에서 이 키를 사용하지 않음 |
| `planner_server.ros__parameters.costmap_update_timeout` | [287](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:287) | `1.0` | `1.0` | 공식과 동일 |
| `planner_server.ros__parameters.expected_planner_frequency` | [285](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:285) | `20.0` | `20.0` | 공식과 동일 |
| `planner_server.ros__parameters.planner_plugins` | [286](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:286) | `["SmacPlannerHybrid"]` | `["SmacPlannerHybrid"]` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.do_refinement` | [322](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:322) | `false` | `false` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.max_its` | [321](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:321) | `200` | `200` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.plugin` | [319](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:319) | `"nav2_smoother::SimpleSmoother"` | `"nav2_smoother::SimpleSmoother"` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.tolerance` | [320](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:320) | `1e-10` | `1e-10` | 공식과 동일 |
| `smoother_server.ros__parameters.smoother_plugins` | [317](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:317) | `["simple_smoother"]` | `["simple_smoother"]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.deadband_velocity` | [375](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:375) | `[0.0, 0.0, 0.0]` | `[0.0, 0.0, 0.0]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.feedback` | [366](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:366) | `"OPEN_LOOP"` | `"OPEN_LOOP"` | 공식과 동일 |
| `velocity_smoother.ros__parameters.max_accel` | [370](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:370) | `[0.5, 0.5, 1.2]` | `[2.5, 2.5, 3.2]` | 변경 |
| `velocity_smoother.ros__parameters.max_decel` | [371](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:371) | `[-0.5, -0.5, -1.2]` | `[-2.5, -2.5, -3.2]` | 변경 |
| `velocity_smoother.ros__parameters.max_velocity` | [368](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:368) | `[0.35, 0.35, 0.7]` | `[0.5, 0.5, 2.0]` | 변경 |
| `velocity_smoother.ros__parameters.min_velocity` | [369](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:369) | `[-0.35, -0.35, -0.7]` | `[-0.5, -0.5, -2.0]` | 변경 |
| `velocity_smoother.ros__parameters.odom_duration` | [373](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:373) | `0.1` | `0.1` | 공식과 동일 |
| `velocity_smoother.ros__parameters.odom_topic` | [372](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:372) | `"odom"` | `"odom"` | 공식과 동일 |
| `velocity_smoother.ros__parameters.scale_velocities` | [365](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:365) | `true` | `false` | 변경 |
| `velocity_smoother.ros__parameters.smoothing_frequency` | [364](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:364) | `20.0` | `20.0` | 공식과 동일 |
| `velocity_smoother.ros__parameters.velocity_timeout` | [376](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:376) | `1.0` | `1.0` | 공식과 동일 |
| `waypoint_follower.ros__parameters.action_server_result_timeout` | [355](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:355) | `900.0` | `900.0` | 공식과 동일 |
| `waypoint_follower.ros__parameters.loop_rate` | [353](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:353) | `20` | `20` | 공식과 동일 |
| `waypoint_follower.ros__parameters.stop_on_failure` | [354](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:354) | `false` | `false` | 공식과 동일 |
| `waypoint_follower.ros__parameters.wait_at_waypoint.enabled` | [359](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:359) | `true` | `true` | 공식과 동일 |
| `waypoint_follower.ros__parameters.wait_at_waypoint.plugin` | [358](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:358) | `"nav2_waypoint_follower::WaitAtWaypoint"` | `"nav2_waypoint_follower::WaitAtWaypoint"` | 공식과 동일 |
| `waypoint_follower.ros__parameters.wait_at_waypoint.waypoint_pause_duration` | [360](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:360) | `5` | `5` | 공식과 동일 |
| `waypoint_follower.ros__parameters.waypoint_task_executor_plugin` | [356](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:356) | `"wait_at_waypoint"` | `"wait_at_waypoint"` | 공식과 동일 |

공식 원본: [ffw_navigation/config/navigation_mppi.yaml](/home/robotis/ai_worker/ffw_navigation/docs/reference/robotis_9bc7f7b9/ffw_navigation/config/navigation_mppi.yaml)

**ffw_navigation/config/navigation.yaml — RPP 선택용 및 Design AMCL**

| 파라미터 경로 | 현재 파일 위치 | BGF 값 | 공식 파일 명시값 | 차이와 주의사항 |
|---|---|---|---|---|
| `amcl.ros__parameters.alpha1` | [276](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:276) | `0.05` | `0.05` | 공식과 동일 |
| `amcl.ros__parameters.alpha2` | [277](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:277) | `0.05` | `0.05` | 공식과 동일 |
| `amcl.ros__parameters.alpha3` | [278](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:278) | `0.05` | `0.05` | 공식과 동일 |
| `amcl.ros__parameters.alpha4` | [279](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:279) | `0.05` | `0.05` | 공식과 동일 |
| `amcl.ros__parameters.alpha5` | [280](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:280) | `0.05` | `0.05` | 공식과 동일 |
| `amcl.ros__parameters.always_reset_initial_pose` | [308](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:308) | `false` | `false` | 공식과 동일 |
| `amcl.ros__parameters.base_frame_id` | [281](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:281) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `amcl.ros__parameters.do_beamskip` | [287](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:287) | `false` | `false` | 공식과 동일 |
| `amcl.ros__parameters.first_map_only` | [309](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:309) | `false` | `false` | 공식과 동일 |
| `amcl.ros__parameters.global_frame_id` | [282](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:282) | `"map"` | `"map"` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.x` | [311](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:311) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.y` | [312](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:312) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.yaw` | [314](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:314) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.z` | [313](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:313) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.laser_likelihood_max_dist` | [285](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:285) | `1.5` | `1.5` | 공식과 동일 |
| `amcl.ros__parameters.laser_model_type` | [284](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:284) | `"likelihood_field"` | `"likelihood_field"` | 공식과 동일 |
| `amcl.ros__parameters.map_topic` | [306](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:306) | `"map"` | `"map"` | 공식과 동일 |
| `amcl.ros__parameters.max_beams` | [286](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:286) | `40` | `40` | 공식과 동일 |
| `amcl.ros__parameters.max_particles` | [289](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:289) | `1200` | `1200` | 공식과 동일 |
| `amcl.ros__parameters.min_particles` | [288](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:288) | `400` | `400` | 공식과 동일 |
| `amcl.ros__parameters.odom_frame_id` | [283](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:283) | `"odom"` | `"odom"` | 공식과 동일 |
| `amcl.ros__parameters.pf_err` | [290](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:290) | `0.02` | `0.02` | 공식과 동일 |
| `amcl.ros__parameters.pf_z` | [291](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:291) | `0.99` | `0.99` | 공식과 동일 |
| `amcl.ros__parameters.recovery_alpha_fast` | [292](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:292) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.recovery_alpha_slow` | [293](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:293) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.resample_interval` | [294](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:294) | `2` | `2` | 공식과 동일 |
| `amcl.ros__parameters.robot_model_type` | [295](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:295) | `"nav2_amcl::DifferentialMotionModel"` | `"nav2_amcl::DifferentialMotionModel"` | 공식과 동일 |
| `amcl.ros__parameters.scan_topic` | [305](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:305) | `"/scan"` | `"/scan"` | 공식과 동일 |
| `amcl.ros__parameters.set_initial_pose` | [307](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:307) | `true` | `true` | 공식과 동일 |
| `amcl.ros__parameters.sigma_hit` | [304](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:304) | `0.3` | `0.3` | 공식과 동일 |
| `amcl.ros__parameters.tf_broadcast` | [299](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:299) | `true` | `true` | 공식과 동일 |
| `amcl.ros__parameters.transform_tolerance` | [298](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:298) | `0.5` | `0.5` | 공식과 동일 |
| `amcl.ros__parameters.update_min_a` | [296](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:296) | `0.3` | `0.3` | 공식과 동일 |
| `amcl.ros__parameters.update_min_d` | [297](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:297) | `0.35` | `0.35` | 공식과 동일 |
| `amcl.ros__parameters.z_hit` | [300](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:300) | `0.7` | `0.7` | 공식과 동일 |
| `amcl.ros__parameters.z_max` | [302](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:302) | `0.05` | `0.05` | 공식과 동일 |
| `amcl.ros__parameters.z_rand` | [303](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:303) | `0.2` | `0.2` | 공식과 동일 |
| `amcl.ros__parameters.z_short` | [301](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:301) | `0.05` | `0.05` | 공식과 동일 |
| `behavior_server.ros__parameters.assisted_teleop.plugin` | [176](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:176) | `"nav2_behaviors::AssistedTeleop"` | `"nav2_behaviors::AssistedTeleop"` | 공식과 동일 |
| `behavior_server.ros__parameters.backup.plugin` | [170](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:170) | `"nav2_behaviors::BackUp"` | `"nav2_behaviors::BackUp"` | 공식과 동일 |
| `behavior_server.ros__parameters.behavior_plugins` | [166](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:166) | `["spin", "backup", "drive_on_heading", "assisted_teleop", "wait"]` | `["spin", "backup", "drive_on_heading", "assisted_teleop", "wait"]` | 공식과 동일 |
| `behavior_server.ros__parameters.cycle_frequency` | [165](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:165) | `10.0` | `10.0` | 공식과 동일 |
| `behavior_server.ros__parameters.drive_on_heading.plugin` | [172](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:172) | `"nav2_behaviors::DriveOnHeading"` | `"nav2_behaviors::DriveOnHeading"` | 공식과 동일 |
| `behavior_server.ros__parameters.global_costmap_topic` | [162](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:162) | `"global_costmap/costmap_raw"` | `"global_costmap/costmap_raw"` | 공식과 동일 |
| `behavior_server.ros__parameters.global_footprint_topic` | [164](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:164) | `"global_costmap/published_footprint"` | `"global_costmap/published_footprint"` | 공식과 동일 |
| `behavior_server.ros__parameters.global_frame` | [178](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:178) | `"map"` | `"map"` | 공식과 동일 |
| `behavior_server.ros__parameters.local_costmap_topic` | [161](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:161) | `"local_costmap/costmap_raw"` | `"local_costmap/costmap_raw"` | 공식과 동일 |
| `behavior_server.ros__parameters.local_footprint_topic` | [163](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:163) | `"local_costmap/published_footprint"` | `"local_costmap/published_footprint"` | 공식과 동일 |
| `behavior_server.ros__parameters.local_frame` | [177](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:177) | `"odom"` | `"odom"` | 공식과 동일 |
| `behavior_server.ros__parameters.max_rotational_vel` | [182](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:182) | `1.0` | `1.0` | 공식과 동일 |
| `behavior_server.ros__parameters.min_rotational_vel` | [183](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:183) | `0.4` | `0.4` | 공식과 동일 |
| `behavior_server.ros__parameters.robot_base_frame` | [179](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:179) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `behavior_server.ros__parameters.rotational_acc_lim` | [184](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:184) | `3.2` | `3.2` | 공식과 동일 |
| `behavior_server.ros__parameters.simulate_ahead_time` | [181](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:181) | `2.0` | `2.0` | 공식과 동일 |
| `behavior_server.ros__parameters.spin.plugin` | [168](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:168) | `"nav2_behaviors::Spin"` | `"nav2_behaviors::Spin"` | 공식과 동일 |
| `behavior_server.ros__parameters.transform_tolerance` | [180](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:180) | `0.1` | `0.1` | 공식과 동일 |
| `behavior_server.ros__parameters.wait.plugin` | [174](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:174) | `"nav2_behaviors::Wait"` | `"nav2_behaviors::Wait"` | 공식과 동일 |
| `bt_navigator.ros__parameters.action_server_result_timeout` | [9](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:9) | `900.0` | `900.0` | 공식과 동일 |
| `bt_navigator.ros__parameters.bt_loop_duration` | [6](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:6) | `10` | `10` | 공식과 동일 |
| `bt_navigator.ros__parameters.default_server_timeout` | [7](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:7) | `20` | `20` | 공식과 동일 |
| `bt_navigator.ros__parameters.error_code_names` | [16](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:16) | `["compute_path_error_code", "follow_path_error_code"]` | `["compute_path_error_code", "follow_path_error_code"]` | 공식과 동일 |
| `bt_navigator.ros__parameters.global_frame` | [3](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:3) | `"map"` | `"map"` | 공식과 동일 |
| `bt_navigator.ros__parameters.navigate_through_poses.plugin` | [14](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:14) | `"nav2_bt_navigator::NavigateThroughPosesNavigator"` | `"nav2_bt_navigator::NavigateThroughPosesNavigator"` | 공식과 동일 |
| `bt_navigator.ros__parameters.navigate_to_pose.plugin` | [12](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:12) | `"nav2_bt_navigator::NavigateToPoseNavigator"` | `"nav2_bt_navigator::NavigateToPoseNavigator"` | 공식과 동일 |
| `bt_navigator.ros__parameters.navigators` | [10](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:10) | `["navigate_to_pose", "navigate_through_poses"]` | `["navigate_to_pose", "navigate_through_poses"]` | 공식과 동일 |
| `bt_navigator.ros__parameters.odom_topic` | [5](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:5) | `"/odom"` | `"/odom"` | 공식과 동일 |
| `bt_navigator.ros__parameters.robot_base_frame` | [4](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:4) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `bt_navigator.ros__parameters.wait_for_service_timeout` | [8](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:8) | `1000` | `1000` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.action_type` | [225](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:225) | `"approach"` | `"approach"` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.enabled` | [231](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:231) | `false` | `false` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.footprint_topic` | [226](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:226) | `"/local_costmap/published_footprint"` | `"/local_costmap/published_footprint"` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.min_points` | [229](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:229) | `8` | `8` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.simulation_time_step` | [228](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:228) | `0.1` | `0.1` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.time_before_collision` | [227](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:227) | `1.6` | `1.6` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.type` | [224](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:224) | `"polygon"` | `"polygon"` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.visualize` | [230](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:230) | `false` | `false` | 공식과 동일 |
| `collision_monitor.ros__parameters.base_frame_id` | [213](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:213) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `collision_monitor.ros__parameters.base_shift_correction` | [220](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:220) | `true` | `true` | 공식과 동일 |
| `collision_monitor.ros__parameters.cmd_vel_in_topic` | [215](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:215) | `"cmd_vel_smoothed"` | `"cmd_vel_smoothed"` | 공식과 동일 |
| `collision_monitor.ros__parameters.cmd_vel_out_topic` | [216](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:216) | `"cmd_vel"` | `"cmd_vel"` | 공식과 동일 |
| `collision_monitor.ros__parameters.observation_sources` | [232](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:232) | `["scan"]` | `["scan"]` | 공식과 동일 |
| `collision_monitor.ros__parameters.odom_frame_id` | [214](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:214) | `"odom"` | `"odom"` | 공식과 동일 |
| `collision_monitor.ros__parameters.polygons` | [222](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:222) | `["FootprintApproach"]` | `["FootprintApproach"]` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.enabled` | [238](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:238) | `true` | `true` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.max_height` | [237](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:237) | `2.0` | `2.0` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.min_height` | [236](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:236) | `0.15` | `0.15` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.topic` | [235](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:235) | `"scan"` | `"scan"` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.type` | [234](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:234) | `"scan"` | `"scan"` | 공식과 동일 |
| `collision_monitor.ros__parameters.source_timeout` | [219](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:219) | `1.0` | `1.0` | 공식과 동일 |
| `collision_monitor.ros__parameters.state_topic` | [217](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:217) | `"collision_monitor_state"` | `"collision_monitor_state"` | 공식과 동일 |
| `collision_monitor.ros__parameters.stop_pub_timeout` | [221](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:221) | `2.0` | `2.0` | 공식과 동일 |
| `collision_monitor.ros__parameters.transform_tolerance` | [218](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:218) | `0.2` | `0.2` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.allow_reversing` | [62](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:62) | `false` | `false` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.approach_velocity_scaling_dist` | [50](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:50) | `0.4` | `0.4` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.cost_scaling_dist` | [57](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:57) | `0.3` | `0.3` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.cost_scaling_gain` | [58](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:58) | `1.0` | `1.0` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.curvature_lookahead_dist` | [55](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:55) | `0.25` | `0.25` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.desired_linear_vel` | [42](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:42) | `0.5` | `0.5` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.lookahead_dist` | [43](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:43) | `0.4` | `0.4` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.lookahead_time` | [46](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:46) | `2.0` | `2.0` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.max_allowed_time_to_collision_up_to_carrot` | [52](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:52) | `1.0` | `1.0` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.max_angular_accel` | [64](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:64) | `2.0` | `2.0` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.max_lookahead_dist` | [45](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:45) | `0.6` | `0.6` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.min_approach_linear_velocity` | [49](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:49) | `0.1` | `0.1` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.min_distance_to_obstacle` | [65](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:65) | `0.0` | `0.0` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.min_lookahead_dist` | [44](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:44) | `0.4` | `0.4` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.plugin` | [41](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:41) | `"nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController"` | `"nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController"` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.regulated_linear_scaling_min_radius` | [59](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:59) | `0.9` | `0.9` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.regulated_linear_scaling_min_speed` | [60](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:60) | `0.25` | `0.25` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.rotate_to_heading_angular_vel` | [47](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:47) | `1.5` | `1.5` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.rotate_to_heading_min_angle` | [63](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:63) | `0.5` | `0.5` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.stateful` | [66](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:66) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.use_collision_detection` | [51](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:51) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.use_cost_regulated_linear_velocity_scaling` | [56](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:56) | `false` | `false` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.use_fixed_curvature_lookahead` | [54](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:54) | `false` | `false` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.use_regulated_linear_velocity_scaling` | [53](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:53) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.use_rotate_to_heading` | [61](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:61) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.FollowPath.use_velocity_scaled_lookahead_dist` | [48](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:48) | `false` | `false` | 공식과 동일 |
| `controller_server.ros__parameters.controller_frequency` | [21](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:21) | `20.0` | `20.0` | 공식과 동일 |
| `controller_server.ros__parameters.controller_plugins` | [29](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:29) | `["FollowPath"]` | `["FollowPath"]` | 공식과 동일 |
| `controller_server.ros__parameters.costmap_update_timeout` | [22](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:22) | `0.3` | `0.3` | 공식과 동일 |
| `controller_server.ros__parameters.failure_tolerance` | [26](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:26) | `0.3` | `0.3` | 공식과 동일 |
| `controller_server.ros__parameters.general_goal_checker.plugin` | [37](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:37) | `"nav2_controller::SimpleGoalChecker"` | `"nav2_controller::SimpleGoalChecker"` | 공식과 동일 |
| `controller_server.ros__parameters.general_goal_checker.stateful` | [36](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:36) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.general_goal_checker.xy_goal_tolerance` | [38](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:38) | `0.25` | `0.25` | 공식과 동일 |
| `controller_server.ros__parameters.general_goal_checker.yaw_goal_tolerance` | [39](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:39) | `0.05` | `0.05` | 공식과 동일 |
| `controller_server.ros__parameters.goal_checker_plugins` | [28](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:28) | `["general_goal_checker"]` | `["general_goal_checker"]` | 공식과 동일 |
| `controller_server.ros__parameters.min_theta_velocity_threshold` | [25](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:25) | `0.001` | `0.001` | 공식과 동일 |
| `controller_server.ros__parameters.min_x_velocity_threshold` | [23](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:23) | `0.001` | `0.001` | 공식과 동일 |
| `controller_server.ros__parameters.min_y_velocity_threshold` | [24](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:24) | `0.0` | `0.0` | 공식과 동일 |
| `controller_server.ros__parameters.progress_checker.movement_time_allowance` | [34](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:34) | `10.0` | `10.0` | 공식과 동일 |
| `controller_server.ros__parameters.progress_checker.plugin` | [32](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:32) | `"nav2_controller::SimpleProgressChecker"` | `"nav2_controller::SimpleProgressChecker"` | 공식과 동일 |
| `controller_server.ros__parameters.progress_checker.required_movement_radius` | [33](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:33) | `0.5` | `0.5` | 공식과 동일 |
| `controller_server.ros__parameters.progress_checker_plugins` | [27](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:27) | `["progress_checker"]` | `["progress_checker"]` | 공식과 동일 |
| `controller_server.ros__parameters.use_realtime_priority` | [30](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:30) | `false` | `false` | 공식과 동일 |
| `docking_server.ros__parameters.base_frame` | [249](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:249) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `docking_server.ros__parameters.controller.k_delta` | [270](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:270) | `2.0` | `2.0` | 공식과 동일 |
| `docking_server.ros__parameters.controller.k_phi` | [269](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:269) | `3.0` | `3.0` | 공식과 동일 |
| `docking_server.ros__parameters.controller.v_linear_max` | [272](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:272) | `0.15` | `0.15` | 공식과 동일 |
| `docking_server.ros__parameters.controller.v_linear_min` | [271](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:271) | `0.15` | `0.15` | 공식과 동일 |
| `docking_server.ros__parameters.controller_frequency` | [242](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:242) | `50.0` | `50.0` | 공식과 동일 |
| `docking_server.ros__parameters.dock_approach_timeout` | [245](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:245) | `30.0` | `30.0` | 공식과 동일 |
| `docking_server.ros__parameters.dock_backwards` | [251](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:251) | `false` | `false` | 공식과 동일 |
| `docking_server.ros__parameters.dock_plugins` | [253](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:253) | `["simple_charging_dock"]` | `["simple_charging_dock"]` | 공식과 동일 |
| `docking_server.ros__parameters.dock_prestaging_tolerance` | [252](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:252) | `0.5` | `0.5` | 공식과 동일 |
| `docking_server.ros__parameters.fixed_frame` | [250](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:250) | `"odom"` | `"odom"` | 공식과 동일 |
| `docking_server.ros__parameters.initial_perception_timeout` | [243](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:243) | `5.0` | `5.0` | 공식과 동일 |
| `docking_server.ros__parameters.max_retries` | [248](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:248) | `3` | `3` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.docking_threshold` | [256](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:256) | `0.05` | `0.05` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_rotation_pitch` | [265](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:265) | `-1.57` | `-1.57` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_rotation_roll` | [264](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:264) | `-1.57` | `-1.57` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_rotation_yaw` | [266](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:266) | `0.0` | `0.0` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_timeout` | [261](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:261) | `1.0` | `1.0` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_translation_x` | [262](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:262) | `-0.18` | `-0.18` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_translation_y` | [263](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:263) | `0.0` | `0.0` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.filter_coef` | [267](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:267) | `0.1` | `0.1` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.plugin` | [255](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:255) | `"opennav_docking::SimpleChargingDock"` | `"opennav_docking::SimpleChargingDock"` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.staging_x_offset` | [257](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:257) | `-0.7` | `-0.7` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.use_battery_status` | [259](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:259) | `false` | `false` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.use_external_detection_pose` | [258](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:258) | `true` | `true` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.use_stall_detection` | [260](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:260) | `false` | `false` | 공식과 동일 |
| `docking_server.ros__parameters.undock_angular_tolerance` | [247](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:247) | `0.1` | `0.1` | 공식과 동일 |
| `docking_server.ros__parameters.undock_linear_tolerance` | [246](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:246) | `0.05` | `0.05` | 공식과 동일 |
| `docking_server.ros__parameters.wait_charge_timeout` | [244](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:244) | `5.0` | `5.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.always_send_full_costmap` | [136](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:136) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.global_frame` | [106](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:106) | `"map"` | `"map"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.inflation_layer.cost_scaling_factor` | [134](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:134) | `3.0` | `3.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.inflation_layer.inflation_radius` | [135](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:135) | `0.7` | `0.7` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.inflation_layer.plugin` | [133](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:133) | `"nav2_costmap_2d::InflationLayer"` | `"nav2_costmap_2d::InflationLayer"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.combination_method` | [115](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:115) | `1` | `1` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.enabled` | [117](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:117) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.expected_update_rate` | [114](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:114) | `0.0` | `0.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.observation_persistence` | [113](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:113) | `0.0` | `0.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.observation_sources` | [118](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:118) | `"scan"` | `"scan"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.plugin` | [116](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:116) | `"nav2_costmap_2d::ObstacleLayer"` | `"nav2_costmap_2d::ObstacleLayer"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.clearing` | [122](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:122) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.data_type` | [124](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:124) | `"LaserScan"` | `"LaserScan"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.marking` | [123](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:123) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.max_obstacle_height` | [121](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:121) | `2.0` | `2.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.obstacle_max_range` | [127](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:127) | `5.0` | `5.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.obstacle_min_range` | [128](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:128) | `0.35` | `0.35` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.raytrace_max_range` | [125](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:125) | `15.0` | `15.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.raytrace_min_range` | [126](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:126) | `0.05` | `0.05` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.topic` | [120](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:120) | `"/scan"` | `"/scan"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.plugins` | [111](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:111) | `["static_layer", "obstacle_layer", "inflation_layer"]` | `["static_layer", "obstacle_layer", "inflation_layer"]` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.publish_frequency` | [105](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:105) | `2.0` | `2.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.resolution` | [109](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:109) | `0.05` | `0.05` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.robot_base_frame` | [107](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:107) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.robot_radius` | [108](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:108) | `0.4` | `0.4` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.static_layer.map_subscribe_transient_local` | [131](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:131) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.static_layer.plugin` | [130](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:130) | `"nav2_costmap_2d::StaticLayer"` | `"nav2_costmap_2d::StaticLayer"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.track_unknown_space` | [110](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:110) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.update_frequency` | [104](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:104) | `5.0` | `5.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.always_send_full_costmap` | [99](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:99) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.global_frame` | [73](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:73) | `"odom"` | `"odom"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.height` | [77](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:77) | `4` | `4` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.inflation_layer.cost_scaling_factor` | [83](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:83) | `3.0` | `3.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.inflation_layer.inflation_radius` | [84](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:84) | `0.7` | `0.7` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.inflation_layer.plugin` | [82](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:82) | `"nav2_costmap_2d::InflationLayer"` | `"nav2_costmap_2d::InflationLayer"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.enabled` | [87](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:87) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.observation_sources` | [88](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:88) | `"scan"` | `"scan"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.plugin` | [86](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:86) | `"nav2_costmap_2d::ObstacleLayer"` | `"nav2_costmap_2d::ObstacleLayer"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.clearing` | [92](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:92) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.data_type` | [94](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:94) | `"LaserScan"` | `"LaserScan"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.marking` | [93](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:93) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.max_obstacle_height` | [91](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:91) | `2.0` | `2.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.obstacle_max_range` | [97](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:97) | `5.0` | `5.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.obstacle_min_range` | [98](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:98) | `0.35` | `0.35` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.raytrace_max_range` | [95](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:95) | `11.0` | `11.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.raytrace_min_range` | [96](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:96) | `0.1` | `0.1` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.topic` | [90](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:90) | `"/scan"` | `"/scan"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.plugins` | [80](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:80) | `["obstacle_layer", "inflation_layer"]` | `["obstacle_layer", "inflation_layer"]` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.publish_frequency` | [72](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:72) | `2.0` | `2.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.resolution` | [78](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:78) | `0.05` | `0.05` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.robot_base_frame` | [74](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:74) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.robot_radius` | [79](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:79) | `0.4` | `0.4` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.rolling_window` | [75](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:75) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.update_frequency` | [71](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:71) | `5.0` | `5.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.width` | [76](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:76) | `4` | `4` | 공식과 동일 |
| `planner_server.ros__parameters.GridBased.allow_unknown` | [148](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:148) | `true` | `true` | 공식과 동일 |
| `planner_server.ros__parameters.GridBased.plugin` | [145](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:145) | `"nav2_navfn_planner::NavfnPlanner"` | `"nav2_navfn_planner::NavfnPlanner"` | 공식과 동일 |
| `planner_server.ros__parameters.GridBased.tolerance` | [146](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:146) | `0.5` | `0.5` | 공식과 동일 |
| `planner_server.ros__parameters.GridBased.use_astar` | [147](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:147) | `false` | `false` | 공식과 동일 |
| `planner_server.ros__parameters.costmap_update_timeout` | [143](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:143) | `1.0` | `1.0` | 공식과 동일 |
| `planner_server.ros__parameters.expected_planner_frequency` | [141](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:141) | `20.0` | `20.0` | 공식과 동일 |
| `planner_server.ros__parameters.planner_plugins` | [142](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:142) | `["GridBased"]` | `["GridBased"]` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.do_refinement` | [157](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:157) | `true` | `true` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.max_its` | [156](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:156) | `1000` | `1000` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.plugin` | [154](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:154) | `"nav2_smoother::SimpleSmoother"` | `"nav2_smoother::SimpleSmoother"` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.tolerance` | [155](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:155) | `1e-10` | `1e-10` | 공식과 동일 |
| `smoother_server.ros__parameters.smoother_plugins` | [152](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:152) | `["simple_smoother"]` | `["simple_smoother"]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.deadband_velocity` | [208](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:208) | `[0.03, 0.0, 0.03]` | `[0.03, 0.0, 0.03]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.feedback` | [201](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:201) | `"OPEN_LOOP"` | `"OPEN_LOOP"` | 공식과 동일 |
| `velocity_smoother.ros__parameters.max_accel` | [204](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:204) | `[0.5, 0.0, 1.5]` | `[0.5, 0.0, 1.5]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.max_decel` | [205](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:205) | `[-0.5, 0.0, -1.5]` | `[-0.5, 0.0, -1.5]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.max_velocity` | [202](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:202) | `[0.5, 0.0, 1.5]` | `[0.5, 0.0, 1.5]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.min_velocity` | [203](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:203) | `[-0.5, 0.0, -1.5]` | `[-0.5, 0.0, -1.5]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.odom_duration` | [207](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:207) | `0.1` | `0.1` | 공식과 동일 |
| `velocity_smoother.ros__parameters.odom_topic` | [206](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:206) | `"odom"` | `"odom"` | 공식과 동일 |
| `velocity_smoother.ros__parameters.scale_velocities` | [200](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:200) | `false` | `false` | 공식과 동일 |
| `velocity_smoother.ros__parameters.smoothing_frequency` | [199](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:199) | `20.0` | `20.0` | 공식과 동일 |
| `velocity_smoother.ros__parameters.velocity_timeout` | [209](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:209) | `1.0` | `1.0` | 공식과 동일 |
| `waypoint_follower.ros__parameters.action_server_result_timeout` | [190](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:190) | `900.0` | `900.0` | 공식과 동일 |
| `waypoint_follower.ros__parameters.loop_rate` | [188](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:188) | `20` | `20` | 공식과 동일 |
| `waypoint_follower.ros__parameters.stop_on_failure` | [189](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:189) | `false` | `false` | 공식과 동일 |
| `waypoint_follower.ros__parameters.wait_at_waypoint.enabled` | [194](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:194) | `true` | `true` | 공식과 동일 |
| `waypoint_follower.ros__parameters.wait_at_waypoint.plugin` | [193](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:193) | `"nav2_waypoint_follower::WaitAtWaypoint"` | `"nav2_waypoint_follower::WaitAtWaypoint"` | 공식과 동일 |
| `waypoint_follower.ros__parameters.wait_at_waypoint.waypoint_pause_duration` | [195](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:195) | `5` | `5` | 공식과 동일 |
| `waypoint_follower.ros__parameters.waypoint_task_executor_plugin` | [191](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:191) | `"wait_at_waypoint"` | `"wait_at_waypoint"` | 공식과 동일 |

공식 원본: [ffw_navigation/config/navigation.yaml](/home/robotis/ai_worker/ffw_navigation/docs/reference/robotis_9bc7f7b9/ffw_navigation/config/navigation.yaml)

**ffw_navigation/config/navigation_mppi.yaml — 공식 MPPI 선택용**

| 파라미터 경로 | 현재 파일 위치 | BGF 값 | 공식 파일 명시값 | 차이와 주의사항 |
|---|---|---|---|---|
| `amcl.ros__parameters.alpha1` | [420](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:420) | `0.4` | `0.4` | 공식과 동일 |
| `amcl.ros__parameters.alpha2` | [421](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:421) | `0.4` | `0.4` | 공식과 동일 |
| `amcl.ros__parameters.alpha3` | [422](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:422) | `0.4` | `0.4` | 공식과 동일 |
| `amcl.ros__parameters.alpha4` | [423](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:423) | `0.4` | `0.4` | 공식과 동일 |
| `amcl.ros__parameters.alpha5` | [424](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:424) | `0.4` | `0.4` | 공식과 동일 |
| `amcl.ros__parameters.always_reset_initial_pose` | [459](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:459) | `false` | `false` | 공식과 동일 |
| `amcl.ros__parameters.base_frame_id` | [425](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:425) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `amcl.ros__parameters.beam_skip_distance` | [426](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:426) | `0.5` | `0.5` | 공식과 동일 |
| `amcl.ros__parameters.beam_skip_error_threshold` | [427](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:427) | `0.9` | `0.9` | 공식과 동일 |
| `amcl.ros__parameters.beam_skip_threshold` | [428](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:428) | `0.3` | `0.3` | 공식과 동일 |
| `amcl.ros__parameters.do_beamskip` | [429](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:429) | `false` | `false` | 공식과 동일 |
| `amcl.ros__parameters.first_map_only` | [460](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:460) | `false` | `false` | 공식과 동일 |
| `amcl.ros__parameters.global_frame_id` | [430](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:430) | `"map"` | `"map"` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.x` | [462](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:462) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.y` | [463](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:463) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.yaw` | [465](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:465) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.initial_pose.z` | [464](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:464) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.lambda_short` | [431](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:431) | `0.1` | `0.1` | 공식과 동일 |
| `amcl.ros__parameters.laser_likelihood_max_dist` | [432](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:432) | `2.0` | `2.0` | 공식과 동일 |
| `amcl.ros__parameters.laser_max_range` | [433](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:433) | `100.0` | `100.0` | 공식과 동일 |
| `amcl.ros__parameters.laser_min_range` | [434](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:434) | `-1.0` | `-1.0` | 공식과 동일 |
| `amcl.ros__parameters.laser_model_type` | [435](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:435) | `"likelihood_field"` | `"likelihood_field"` | 공식과 동일 |
| `amcl.ros__parameters.map_topic` | [457](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:457) | `"map"` | `"map"` | 공식과 동일 |
| `amcl.ros__parameters.max_beams` | [436](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:436) | `60` | `60` | 공식과 동일 |
| `amcl.ros__parameters.max_particles` | [437](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:437) | `2000` | `2000` | 공식과 동일 |
| `amcl.ros__parameters.min_particles` | [438](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:438) | `500` | `500` | 공식과 동일 |
| `amcl.ros__parameters.odom_frame_id` | [439](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:439) | `"odom"` | `"odom"` | 공식과 동일 |
| `amcl.ros__parameters.pf_err` | [440](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:440) | `0.05` | `0.05` | 공식과 동일 |
| `amcl.ros__parameters.pf_z` | [441](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:441) | `0.99` | `0.99` | 공식과 동일 |
| `amcl.ros__parameters.recovery_alpha_fast` | [442](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:442) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.recovery_alpha_slow` | [443](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:443) | `0.0` | `0.0` | 공식과 동일 |
| `amcl.ros__parameters.resample_interval` | [444](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:444) | `1` | `1` | 공식과 동일 |
| `amcl.ros__parameters.robot_model_type` | [445](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:445) | `"nav2_amcl::OmniMotionModel"` | `"nav2_amcl::OmniMotionModel"` | 공식과 동일 |
| `amcl.ros__parameters.save_pose_rate` | [446](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:446) | `0.5` | `0.5` | 공식과 동일 |
| `amcl.ros__parameters.scan_topic` | [456](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:456) | `"/scan"` | `"/scan"` | 공식과 동일 |
| `amcl.ros__parameters.set_initial_pose` | [458](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:458) | `true` | `true` | 공식과 동일 |
| `amcl.ros__parameters.sigma_hit` | [447](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:447) | `0.2` | `0.2` | 공식과 동일 |
| `amcl.ros__parameters.tf_broadcast` | [448](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:448) | `true` | `true` | 공식과 동일 |
| `amcl.ros__parameters.transform_tolerance` | [449](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:449) | `1.0` | `1.0` | 공식과 동일 |
| `amcl.ros__parameters.update_min_a` | [450](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:450) | `0.01` | `0.01` | 공식과 동일 |
| `amcl.ros__parameters.update_min_d` | [451](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:451) | `0.25` | `0.25` | 공식과 동일 |
| `amcl.ros__parameters.z_hit` | [452](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:452) | `0.5` | `0.5` | 공식과 동일 |
| `amcl.ros__parameters.z_max` | [453](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:453) | `0.05` | `0.05` | 공식과 동일 |
| `amcl.ros__parameters.z_rand` | [454](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:454) | `0.5` | `0.5` | 공식과 동일 |
| `amcl.ros__parameters.z_short` | [455](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:455) | `0.05` | `0.05` | 공식과 동일 |
| `behavior_server.ros__parameters.assisted_teleop.plugin` | [324](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:324) | `"nav2_behaviors::AssistedTeleop"` | `"nav2_behaviors::AssistedTeleop"` | 공식과 동일 |
| `behavior_server.ros__parameters.backup.plugin` | [318](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:318) | `"nav2_behaviors::BackUp"` | `"nav2_behaviors::BackUp"` | 공식과 동일 |
| `behavior_server.ros__parameters.behavior_plugins` | [314](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:314) | `["spin", "backup", "drive_on_heading", "assisted_teleop", "wait"]` | `["spin", "backup", "drive_on_heading", "assisted_teleop", "wait"]` | 공식과 동일 |
| `behavior_server.ros__parameters.cycle_frequency` | [313](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:313) | `10.0` | `10.0` | 공식과 동일 |
| `behavior_server.ros__parameters.drive_on_heading.plugin` | [320](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:320) | `"nav2_behaviors::DriveOnHeading"` | `"nav2_behaviors::DriveOnHeading"` | 공식과 동일 |
| `behavior_server.ros__parameters.global_costmap_topic` | [310](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:310) | `"global_costmap/costmap_raw"` | `"global_costmap/costmap_raw"` | 공식과 동일 |
| `behavior_server.ros__parameters.global_footprint_topic` | [312](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:312) | `"global_costmap/published_footprint"` | `"global_costmap/published_footprint"` | 공식과 동일 |
| `behavior_server.ros__parameters.global_frame` | [326](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:326) | `"map"` | `"map"` | 공식과 동일 |
| `behavior_server.ros__parameters.local_costmap_topic` | [309](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:309) | `"local_costmap/costmap_raw"` | `"local_costmap/costmap_raw"` | 공식과 동일 |
| `behavior_server.ros__parameters.local_footprint_topic` | [311](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:311) | `"local_costmap/published_footprint"` | `"local_costmap/published_footprint"` | 공식과 동일 |
| `behavior_server.ros__parameters.local_frame` | [325](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:325) | `"odom"` | `"odom"` | 공식과 동일 |
| `behavior_server.ros__parameters.max_rotational_vel` | [330](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:330) | `1.0` | `1.0` | 공식과 동일 |
| `behavior_server.ros__parameters.min_rotational_vel` | [331](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:331) | `0.4` | `0.4` | 공식과 동일 |
| `behavior_server.ros__parameters.robot_base_frame` | [327](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:327) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `behavior_server.ros__parameters.rotational_acc_lim` | [332](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:332) | `3.2` | `3.2` | 공식과 동일 |
| `behavior_server.ros__parameters.simulate_ahead_time` | [329](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:329) | `2.0` | `2.0` | 공식과 동일 |
| `behavior_server.ros__parameters.spin.plugin` | [316](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:316) | `"nav2_behaviors::Spin"` | `"nav2_behaviors::Spin"` | 공식과 동일 |
| `behavior_server.ros__parameters.transform_tolerance` | [328](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:328) | `0.3` | `0.3` | 공식과 동일 |
| `behavior_server.ros__parameters.wait.plugin` | [322](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:322) | `"nav2_behaviors::Wait"` | `"nav2_behaviors::Wait"` | 공식과 동일 |
| `bt_navigator.ros__parameters.action_server_result_timeout` | [9](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:9) | `900.0` | `900.0` | 공식과 동일 |
| `bt_navigator.ros__parameters.bt_loop_duration` | [6](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:6) | `10` | `10` | 공식과 동일 |
| `bt_navigator.ros__parameters.default_nav_through_poses_bt_xml` | [16](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:16) | `"$(find-pkg-share ffw_navigation)/config/bt/nav_modes.xml"` | `"$(find-pkg-share ffw_navigation)/config/bt/nav_modes.xml"` | 공식과 동일 |
| `bt_navigator.ros__parameters.default_nav_to_pose_bt_xml` | [15](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:15) | `"$(find-pkg-share ffw_navigation)/config/bt/nav_modes.xml"` | `"$(find-pkg-share ffw_navigation)/config/bt/nav_modes.xml"` | 공식과 동일 |
| `bt_navigator.ros__parameters.default_server_timeout` | [7](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:7) | `20` | `20` | 공식과 동일 |
| `bt_navigator.ros__parameters.error_code_names` | [19](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:19) | `["compute_path_error_code", "follow_path_error_code"]` | `["compute_path_error_code", "follow_path_error_code"]` | 공식과 동일 |
| `bt_navigator.ros__parameters.global_frame` | [3](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:3) | `"map"` | `"map"` | 공식과 동일 |
| `bt_navigator.ros__parameters.navigate_through_poses.plugin` | [14](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:14) | `"nav2_bt_navigator::NavigateThroughPosesNavigator"` | `"nav2_bt_navigator::NavigateThroughPosesNavigator"` | 공식과 동일 |
| `bt_navigator.ros__parameters.navigate_to_pose.plugin` | [12](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:12) | `"nav2_bt_navigator::NavigateToPoseNavigator"` | `"nav2_bt_navigator::NavigateToPoseNavigator"` | 공식과 동일 |
| `bt_navigator.ros__parameters.navigators` | [10](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:10) | `["navigate_to_pose", "navigate_through_poses"]` | `["navigate_to_pose", "navigate_through_poses"]` | 공식과 동일 |
| `bt_navigator.ros__parameters.odom_topic` | [5](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:5) | `"/odom"` | `"/odom"` | 공식과 동일 |
| `bt_navigator.ros__parameters.plugin_lib_names` | [17](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:17) | `["is_path_length_under_plugin", "nav2_behavior_tree"]` | `["is_path_length_under_plugin", "nav2_behavior_tree"]` | 공식과 동일 |
| `bt_navigator.ros__parameters.robot_base_frame` | [4](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:4) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `bt_navigator.ros__parameters.wait_for_service_timeout` | [8](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:8) | `1000` | `1000` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.action_type` | [373](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:373) | `"approach"` | `"approach"` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.enabled` | [379](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:379) | `false` | `false` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.footprint_topic` | [374](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:374) | `"/local_costmap/published_footprint"` | `"/local_costmap/published_footprint"` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.min_points` | [377](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:377) | `6` | `6` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.simulation_time_step` | [376](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:376) | `0.1` | `0.1` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.time_before_collision` | [375](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:375) | `1.0` | `1.0` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.type` | [372](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:372) | `"polygon"` | `"polygon"` | 공식과 동일 |
| `collision_monitor.ros__parameters.FootprintApproach.visualize` | [378](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:378) | `false` | `false` | 공식과 동일 |
| `collision_monitor.ros__parameters.base_frame_id` | [361](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:361) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `collision_monitor.ros__parameters.base_shift_correction` | [368](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:368) | `true` | `true` | 공식과 동일 |
| `collision_monitor.ros__parameters.cmd_vel_in_topic` | [363](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:363) | `"cmd_vel_smoothed"` | `"cmd_vel_smoothed"` | 공식과 동일 |
| `collision_monitor.ros__parameters.cmd_vel_out_topic` | [364](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:364) | `"cmd_vel"` | `"cmd_vel"` | 공식과 동일 |
| `collision_monitor.ros__parameters.observation_sources` | [380](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:380) | `["scan"]` | `["scan"]` | 공식과 동일 |
| `collision_monitor.ros__parameters.odom_frame_id` | [362](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:362) | `"odom"` | `"odom"` | 공식과 동일 |
| `collision_monitor.ros__parameters.polygons` | [370](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:370) | `["FootprintApproach"]` | `["FootprintApproach"]` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.enabled` | [386](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:386) | `true` | `true` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.max_height` | [385](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:385) | `2.0` | `2.0` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.min_height` | [384](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:384) | `0.15` | `0.15` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.topic` | [383](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:383) | `"scan"` | `"scan"` | 공식과 동일 |
| `collision_monitor.ros__parameters.scan.type` | [382](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:382) | `"scan"` | `"scan"` | 공식과 동일 |
| `collision_monitor.ros__parameters.source_timeout` | [367](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:367) | `1.0` | `1.0` | 공식과 동일 |
| `collision_monitor.ros__parameters.state_topic` | [365](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:365) | `"collision_monitor_state"` | `"collision_monitor_state"` | 공식과 동일 |
| `collision_monitor.ros__parameters.stop_pub_timeout` | [369](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:369) | `2.0` | `2.0` | 공식과 동일 |
| `collision_monitor.ros__parameters.transform_tolerance` | [366](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:366) | `0.2` | `0.2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.ConstraintCritic.cost_power` | [138](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:138) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.ConstraintCritic.cost_weight` | [139](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:139) | `4.0` | `4.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.ConstraintCritic.enabled` | [137](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:137) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.collision_cost` | [164](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:164) | `1000000.0` | `1000000.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.consider_footprint` | [163](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:163) | `false` | `false` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.cost_power` | [160](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:160) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.cost_weight` | [161](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:161) | `4.2` | `4.2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.critical_cost` | [162](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:162) | `300.0` | `300.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.enabled` | [159](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:159) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.near_goal_distance` | [165](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:165) | `1.0` | `1.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.CostCritic.trajectory_point_step` | [166](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:166) | `2` | `2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalAngleCritic.cost_power` | [148](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:148) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalAngleCritic.cost_weight` | [149](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:149) | `2.0` | `2.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalAngleCritic.enabled` | [147](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:147) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalAngleCritic.threshold_to_consider` | [150](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:150) | `0.3` | `0.3` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalCritic.cost_power` | [142](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:142) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalCritic.cost_weight` | [143](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:143) | `5.0` | `5.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalCritic.enabled` | [141](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:141) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.GoalCritic.threshold_to_consider` | [144](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:144) | `1.2` | `1.2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.cost_power` | [170](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:170) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.cost_weight` | [171](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:171) | `14.0` | `14.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.enabled` | [169](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:169) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.max_path_occupancy_ratio` | [172](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:172) | `0.05` | `0.05` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.offset_from_furthest` | [175](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:175) | `15` | `15` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.threshold_to_consider` | [174](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:174) | `1.0` | `1.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.trajectory_point_step` | [173](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:173) | `2` | `2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAlignCritic.use_path_orientations` | [176](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:176) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.cost_power` | [187](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:187) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.cost_weight` | [188](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:188) | `6.0` | `6.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.enabled` | [186](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:186) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.max_angle_to_furthest` | [191](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:191) | `0.4` | `0.4` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.mode` | [192](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:192) | `0` | `0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.offset_from_furthest` | [189](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:189) | `3` | `3` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathAngleCritic.threshold_to_consider` | [190](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:190) | `0.5` | `0.5` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathFollowCritic.cost_power` | [180](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:180) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathFollowCritic.cost_weight` | [181](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:181) | `6.0` | `6.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathFollowCritic.enabled` | [179](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:179) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathFollowCritic.offset_from_furthest` | [182](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:182) | `5` | `5` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PathFollowCritic.threshold_to_consider` | [183](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:183) | `1.2` | `1.2` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PreferForwardCritic.cost_power` | [154](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:154) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PreferForwardCritic.cost_weight` | [155](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:155) | `9.0` | `9.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PreferForwardCritic.enabled` | [153](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:153) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.PreferForwardCritic.threshold_to_consider` | [156](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:156) | `0.5` | `0.5` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.TrajectoryVisualizer.time_step` | [126](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:126) | `3` | `3` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.TrajectoryVisualizer.trajectory_step` | [125](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:125) | `5` | `5` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.batch_size` | [110](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:110) | `1200` | `1200` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.critics` | [128](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:128) | `["ConstraintCritic", "CostCritic", "GoalCritic", "GoalAngleCritic", "PathAlignCritic", "PathFollowCritic", "PathAngleCritic", "PreferForwardCritic"]` | `["ConstraintCritic", "CostCritic", "GoalCritic", "GoalAngleCritic", "PathAlignCritic", "PathFollowCritic", "PathAngleCritic", "PreferForwardCritic"]` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.gamma` | [122](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:122) | `0.02` | `0.02` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.iteration_count` | [120](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:120) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.model_dt` | [109](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:109) | `0.05` | `0.05` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.motion_model` | [111](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:111) | `"Omni"` | `"Omni"` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.plugin` | [107](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:107) | `"nav2_mppi_controller::MPPIController"` | `"nav2_mppi_controller::MPPIController"` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.temperature` | [121](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:121) | `0.27` | `0.27` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.time_steps` | [108](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:108) | `40` | `40` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.visualize` | [123](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:123) | `false` | `false` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.vx_max` | [115](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:115) | `0.5` | `0.5` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.vx_min` | [116](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:116) | `0.0` | `0.0` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.vx_std` | [112](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:112) | `0.17` | `0.17` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.vy_max` | [117](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:117) | `0.25` | `0.25` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.vy_min` | [118](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:118) | `-0.25` | `-0.25` | MPPI 1.3.11은 vy_max를 대칭 상한으로 사용하며 vy_min을 읽지 않음 |
| `controller_server.ros__parameters.CurveController.vy_std` | [113](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:113) | `0.12` | `0.12` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.wz_max` | [119](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:119) | `1.6` | `1.6` | 공식과 동일 |
| `controller_server.ros__parameters.CurveController.wz_std` | [114](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:114) | `0.3` | `0.3` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.ConstraintCritic.cost_power` | [78](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:78) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.ConstraintCritic.cost_weight` | [79](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:79) | `4.0` | `4.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.ConstraintCritic.enabled` | [77](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:77) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.collision_cost` | [96](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:96) | `1000000.0` | `1000000.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.consider_footprint` | [95](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:95) | `false` | `false` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.cost_power` | [92](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:92) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.cost_weight` | [93](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:93) | `4.0` | `4.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.critical_cost` | [94](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:94) | `300.0` | `300.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.enabled` | [91](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:91) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.near_goal_distance` | [97](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:97) | `1.0` | `1.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.CostCritic.trajectory_point_step` | [98](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:98) | `2` | `2` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalAngleCritic.cost_power` | [87](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:87) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalAngleCritic.cost_weight` | [88](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:88) | `5.0` | `5.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalAngleCritic.enabled` | [86](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:86) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalAngleCritic.threshold_to_consider` | [89](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:89) | `0.25` | `0.25` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalCritic.cost_power` | [82](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:82) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalCritic.cost_weight` | [83](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:83) | `5.0` | `5.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalCritic.enabled` | [81](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:81) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.GoalCritic.threshold_to_consider` | [84](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:84) | `1.2` | `1.2` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.PathFollowCritic.cost_power` | [101](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:101) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.PathFollowCritic.cost_weight` | [102](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:102) | `5.0` | `5.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.PathFollowCritic.enabled` | [100](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:100) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.PathFollowCritic.offset_from_furthest` | [103](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:103) | `1` | `1` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.PathFollowCritic.threshold_to_consider` | [104](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:104) | `1.2` | `1.2` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.TrajectoryVisualizer.time_step` | [69](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:69) | `3` | `3` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.TrajectoryVisualizer.trajectory_step` | [68](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:68) | `5` | `5` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.ax_max` | [58](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:58) | `3.0` | `3.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.ax_min` | [59](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:59) | `-3.0` | `-3.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.ay_max` | [60](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:60) | `3.0` | `3.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.ay_min` | [61](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:61) | `-3.0` | `-3.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.az_max` | [62](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:62) | `3.0` | `3.0` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.batch_size` | [48](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:48) | `1200` | `1200` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.critics` | [71](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:71) | `["ConstraintCritic", "CostCritic", "GoalCritic", "GoalAngleCritic", "PathFollowCritic"]` | `["ConstraintCritic", "CostCritic", "GoalCritic", "GoalAngleCritic", "PathFollowCritic"]` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.gamma` | [65](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:65) | `0.018` | `0.018` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.iteration_count` | [63](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:63) | `4` | `4` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.model_dt` | [47](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:47) | `0.05` | `0.05` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.motion_model` | [49](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:49) | `"Omni"` | `"Omni"` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.plugin` | [45](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:45) | `"nav2_mppi_controller::MPPIController"` | `"nav2_mppi_controller::MPPIController"` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.temperature` | [64](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:64) | `0.25` | `0.25` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.time_steps` | [46](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:46) | `40` | `40` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.visualize` | [66](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:66) | `false` | `false` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.vx_max` | [53](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:53) | `0.55` | `0.55` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.vx_min` | [54](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:54) | `-0.55` | `-0.55` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.vx_std` | [50](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:50) | `0.15` | `0.15` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.vy_max` | [55](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:55) | `0.55` | `0.55` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.vy_min` | [56](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:56) | `-0.55` | `-0.55` | MPPI 1.3.11은 vy_max를 대칭 상한으로 사용하며 vy_min을 읽지 않음 |
| `controller_server.ros__parameters.OmniController.vy_std` | [51](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:51) | `0.15` | `0.15` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.wz_max` | [57](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:57) | `0.8` | `0.8` | 공식과 동일 |
| `controller_server.ros__parameters.OmniController.wz_std` | [52](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:52) | `0.35` | `0.35` | 공식과 동일 |
| `controller_server.ros__parameters.controller_frequency` | [24](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:24) | `20.0` | `20.0` | 공식과 동일 |
| `controller_server.ros__parameters.controller_plugins` | [32](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:32) | `["OmniController", "CurveController"]` | `["OmniController", "CurveController"]` | 공식과 동일 |
| `controller_server.ros__parameters.failure_tolerance` | [29](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:29) | `0.3` | `0.3` | 공식과 동일 |
| `controller_server.ros__parameters.general_goal_checker.plugin` | [39](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:39) | `"nav2_controller::SimpleGoalChecker"` | `"nav2_controller::SimpleGoalChecker"` | 공식과 동일 |
| `controller_server.ros__parameters.general_goal_checker.stateful` | [42](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:42) | `true` | `true` | 공식과 동일 |
| `controller_server.ros__parameters.general_goal_checker.xy_goal_tolerance` | [40](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:40) | `0.2` | `0.2` | 공식과 동일 |
| `controller_server.ros__parameters.general_goal_checker.yaw_goal_tolerance` | [41](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:41) | `0.05` | `0.05` | 공식과 동일 |
| `controller_server.ros__parameters.goal_checker_plugins` | [31](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:31) | `["general_goal_checker"]` | `["general_goal_checker"]` | 공식과 동일 |
| `controller_server.ros__parameters.min_theta_velocity_threshold` | [28](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:28) | `0.001` | `0.001` | 공식과 동일 |
| `controller_server.ros__parameters.min_x_velocity_threshold` | [26](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:26) | `0.001` | `0.001` | 공식과 동일 |
| `controller_server.ros__parameters.min_y_velocity_threshold` | [27](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:27) | `0.001` | `0.001` | 공식과 동일 |
| `controller_server.ros__parameters.progress_checker.movement_time_allowance` | [37](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:37) | `10.0` | `10.0` | 공식과 동일 |
| `controller_server.ros__parameters.progress_checker.plugin` | [35](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:35) | `"nav2_controller::SimpleProgressChecker"` | `"nav2_controller::SimpleProgressChecker"` | 공식과 동일 |
| `controller_server.ros__parameters.progress_checker.required_movement_radius` | [36](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:36) | `0.5` | `0.5` | 공식과 동일 |
| `controller_server.ros__parameters.progress_checker_plugin` | [30](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:30) | `"progress_checker"` | `"progress_checker"` | 공식과 동일 |
| `controller_server.ros__parameters.transform_tolerance` | [25](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:25) | `0.3` | `0.3` | 공식과 동일 |
| `docking_server.ros__parameters.controller.costmap_topic` | [411](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:411) | `"local_costmap/costmap_raw"` | `"local_costmap/costmap_raw"` | 공식과 동일 |
| `docking_server.ros__parameters.controller.dock_collision_threshold` | [416](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:416) | `0.3` | `0.3` | 공식과 동일 |
| `docking_server.ros__parameters.controller.footprint_topic` | [412](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:412) | `"local_costmap/published_footprint"` | `"local_costmap/published_footprint"` | 공식과 동일 |
| `docking_server.ros__parameters.controller.k_delta` | [407](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:407) | `2.0` | `2.0` | 공식과 동일 |
| `docking_server.ros__parameters.controller.k_phi` | [406](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:406) | `3.0` | `3.0` | 공식과 동일 |
| `docking_server.ros__parameters.controller.projection_time` | [414](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:414) | `5.0` | `5.0` | 공식과 동일 |
| `docking_server.ros__parameters.controller.simulation_step` | [415](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:415) | `0.1` | `0.1` | 공식과 동일 |
| `docking_server.ros__parameters.controller.transform_tolerance` | [413](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:413) | `0.1` | `0.1` | 공식과 동일 |
| `docking_server.ros__parameters.controller.use_collision_detection` | [410](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:410) | `true` | `true` | 공식과 동일 |
| `docking_server.ros__parameters.controller.v_linear_max` | [409](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:409) | `0.15` | `0.15` | 공식과 동일 |
| `docking_server.ros__parameters.controller.v_linear_min` | [408](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:408) | `0.15` | `0.15` | 공식과 동일 |
| `docking_server.ros__parameters.dock_plugins` | [390](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:390) | `["simple_charging_dock"]` | `["simple_charging_dock"]` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.docking_threshold` | [393](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:393) | `0.05` | `0.05` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_rotation_pitch` | [402](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:402) | `-1.57` | `-1.57` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_rotation_roll` | [401](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:401) | `-1.57` | `-1.57` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_rotation_yaw` | [403](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:403) | `0.0` | `0.0` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_timeout` | [398](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:398) | `1.0` | `1.0` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_translation_x` | [399](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:399) | `-0.18` | `-0.18` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.external_detection_translation_y` | [400](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:400) | `0.0` | `0.0` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.filter_coef` | [404](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:404) | `0.1` | `0.1` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.plugin` | [392](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:392) | `"opennav_docking::SimpleChargingDock"` | `"opennav_docking::SimpleChargingDock"` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.staging_x_offset` | [394](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:394) | `-0.7` | `-0.7` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.use_battery_status` | [396](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:396) | `false` | `false` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.use_external_detection_pose` | [395](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:395) | `true` | `true` | 공식과 동일 |
| `docking_server.ros__parameters.simple_charging_dock.use_stall_detection` | [397](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:397) | `false` | `false` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.always_send_full_costmap` | [264](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:264) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.global_frame` | [236](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:236) | `"map"` | `"map"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.inflation_layer.cost_scaling_factor` | [262](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:262) | `3.0` | `3.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.inflation_layer.inflation_radius` | [263](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:263) | `0.7` | `0.7` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.inflation_layer.plugin` | [261](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:261) | `"nav2_costmap_2d::InflationLayer"` | `"nav2_costmap_2d::InflationLayer"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.enabled` | [245](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:245) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.observation_sources` | [246](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:246) | `"scan"` | `"scan"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.plugin` | [244](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:244) | `"nav2_costmap_2d::ObstacleLayer"` | `"nav2_costmap_2d::ObstacleLayer"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.clearing` | [250](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:250) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.data_type` | [252](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:252) | `"LaserScan"` | `"LaserScan"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.marking` | [251](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:251) | `false` | `false` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.max_obstacle_height` | [249](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:249) | `2.0` | `2.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.obstacle_max_range` | [255](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:255) | `2.5` | `2.5` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.obstacle_min_range` | [256](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:256) | `0.0` | `0.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.raytrace_max_range` | [253](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:253) | `3.0` | `3.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.raytrace_min_range` | [254](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:254) | `0.0` | `0.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.obstacle_layer.scan.topic` | [248](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:248) | `"/scan"` | `"/scan"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.plugins` | [242](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:242) | `["static_layer", "obstacle_layer", "inflation_layer"]` | `["static_layer", "obstacle_layer", "inflation_layer"]` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.publish_frequency` | [235](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:235) | `1.0` | `1.0` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.resolution` | [240](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:240) | `0.05` | `0.05` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.robot_base_frame` | [237](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:237) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.robot_radius` | [239](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:239) | `0.44` | `0.44` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.static_layer.map_subscribe_transient_local` | [259](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:259) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.static_layer.plugin` | [258](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:258) | `"nav2_costmap_2d::StaticLayer"` | `"nav2_costmap_2d::StaticLayer"` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.track_unknown_space` | [241](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:241) | `true` | `true` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.transform_tolerance` | [238](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:238) | `0.3` | `0.3` | 공식과 동일 |
| `global_costmap.global_costmap.ros__parameters.update_frequency` | [234](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:234) | `1.0` | `1.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.always_send_full_costmap` | [229](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:229) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.global_frame` | [199](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:199) | `"odom"` | `"odom"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.height` | [204](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:204) | `3` | `3` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.inflation_layer.cost_scaling_factor` | [210](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:210) | `3.0` | `3.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.inflation_layer.inflation_radius` | [211](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:211) | `0.65` | `0.65` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.inflation_layer.plugin` | [209](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:209) | `"nav2_costmap_2d::InflationLayer"` | `"nav2_costmap_2d::InflationLayer"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.enabled` | [214](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:214) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.observation_sources` | [215](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:215) | `"scan"` | `"scan"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.plugin` | [213](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:213) | `"nav2_costmap_2d::ObstacleLayer"` | `"nav2_costmap_2d::ObstacleLayer"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.clearing` | [219](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:219) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.data_type` | [221](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:221) | `"LaserScan"` | `"LaserScan"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.marking` | [220](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:220) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.max_obstacle_height` | [218](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:218) | `2.0` | `2.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.obstacle_max_range` | [224](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:224) | `2.5` | `2.5` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.obstacle_min_range` | [225](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:225) | `0.0` | `0.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.raytrace_max_range` | [222](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:222) | `3.0` | `3.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.raytrace_min_range` | [223](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:223) | `0.0` | `0.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.obstacle_layer.scan.topic` | [217](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:217) | `"/scan"` | `"/scan"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.plugins` | [207](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:207) | `["obstacle_layer", "inflation_layer"]` | `["obstacle_layer", "inflation_layer"]` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.publish_frequency` | [198](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:198) | `2.0` | `2.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.resolution` | [205](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:205) | `0.05` | `0.05` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.robot_base_frame` | [200](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:200) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.robot_radius` | [206](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:206) | `0.44` | `0.44` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.rolling_window` | [202](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:202) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.static_layer.map_subscribe_transient_local` | [228](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:228) | `true` | `true` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.static_layer.plugin` | [227](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:227) | `"nav2_costmap_2d::StaticLayer"` | `"nav2_costmap_2d::StaticLayer"` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.transform_tolerance` | [201](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:201) | `0.3` | `0.3` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.update_frequency` | [197](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:197) | `5.0` | `5.0` | 공식과 동일 |
| `local_costmap.local_costmap.ros__parameters.width` | [203](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:203) | `3` | `3` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.allow_reverse` | [278](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:278) | `true` | `true` | Hybrid 1.3.11에서 이 키를 사용하지 않음 |
| `planner_server.ros__parameters.SmacPlannerHybrid.allow_unknown` | [274](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:274) | `true` | `true` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.analytic_expansion_ratio` | [280](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:280) | `1.0` | `1.0` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.angle_quantization_bins` | [279](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:279) | `24` | `24` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.cache_obstacle_heuristic` | [291](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:291) | `true` | `true` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.change_penalty` | [286](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:286) | `2.0` | `2.0` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.cost_heuristic_multiplier` | [284](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:284) | `2.5` | `2.5` | Hybrid 1.3.11에서 이 키를 사용하지 않음 |
| `planner_server.ros__parameters.SmacPlannerHybrid.cost_travel_multiplier` | [283](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:283) | `1.0` | `1.0` | Hybrid 1.3.11에서 이 키를 사용하지 않음 |
| `planner_server.ros__parameters.SmacPlannerHybrid.downsample_costmap` | [288](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:288) | `false` | `false` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.downsampling_factor` | [289](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:289) | `1` | `1` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.max_iterations` | [281](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:281) | `40000` | `40000` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.max_on_approach_iterations` | [282](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:282) | `12000` | `12000` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.minimum_turning_radius` | [276](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:276) | `0.0` | `0.0` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.motion_model_for_search` | [277](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:277) | `"REEDS_SHEPP"` | `"REEDS_SHEPP"` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.non_straight_penalty` | [285](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:285) | `10.5` | `10.5` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.plugin` | [272](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:272) | `"nav2_smac_planner::SmacPlannerHybrid"` | `"nav2_smac_planner::SmacPlannerHybrid"` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.rotation_penalty` | [287](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:287) | `1.5` | `1.5` | Hybrid 1.3.11에서 이 키를 사용하지 않음 |
| `planner_server.ros__parameters.SmacPlannerHybrid.smooth_path` | [290](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:290) | `true` | `true` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.smoother.max_iterations` | [293](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:293) | `800` | `800` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.smoother.tolerance` | [296](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:296) | `1e-10` | `1e-10` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.smoother.w_data` | [295](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:295) | `0.05` | `0.05` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.smoother.w_smooth` | [294](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:294) | `0.9` | `0.9` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.tolerance` | [273](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:273) | `0.5` | `0.5` | 공식과 동일 |
| `planner_server.ros__parameters.SmacPlannerHybrid.use_final_approach_orientation` | [275](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:275) | `false` | `false` | Hybrid 1.3.11에서 이 키를 사용하지 않음 |
| `planner_server.ros__parameters.costmap_update_timeout` | [270](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:270) | `1.0` | `1.0` | 공식과 동일 |
| `planner_server.ros__parameters.expected_planner_frequency` | [268](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:268) | `20.0` | `20.0` | 공식과 동일 |
| `planner_server.ros__parameters.planner_plugins` | [269](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:269) | `["SmacPlannerHybrid"]` | `["SmacPlannerHybrid"]` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.do_refinement` | [305](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:305) | `false` | `false` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.max_its` | [304](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:304) | `200` | `200` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.plugin` | [302](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:302) | `"nav2_smoother::SimpleSmoother"` | `"nav2_smoother::SimpleSmoother"` | 공식과 동일 |
| `smoother_server.ros__parameters.simple_smoother.tolerance` | [303](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:303) | `1e-10` | `1e-10` | 공식과 동일 |
| `smoother_server.ros__parameters.smoother_plugins` | [300](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:300) | `["simple_smoother"]` | `["simple_smoother"]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.deadband_velocity` | [356](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:356) | `[0.0, 0.0, 0.0]` | `[0.0, 0.0, 0.0]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.feedback` | [349](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:349) | `"OPEN_LOOP"` | `"OPEN_LOOP"` | 공식과 동일 |
| `velocity_smoother.ros__parameters.max_accel` | [352](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:352) | `[2.5, 2.5, 3.2]` | `[2.5, 2.5, 3.2]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.max_decel` | [353](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:353) | `[-2.5, -2.5, -3.2]` | `[-2.5, -2.5, -3.2]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.max_velocity` | [350](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:350) | `[0.5, 0.5, 2.0]` | `[0.5, 0.5, 2.0]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.min_velocity` | [351](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:351) | `[-0.5, -0.5, -2.0]` | `[-0.5, -0.5, -2.0]` | 공식과 동일 |
| `velocity_smoother.ros__parameters.odom_duration` | [355](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:355) | `0.1` | `0.1` | 공식과 동일 |
| `velocity_smoother.ros__parameters.odom_topic` | [354](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:354) | `"odom"` | `"odom"` | 공식과 동일 |
| `velocity_smoother.ros__parameters.scale_velocities` | [348](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:348) | `false` | `false` | 공식과 동일 |
| `velocity_smoother.ros__parameters.smoothing_frequency` | [347](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:347) | `20.0` | `20.0` | 공식과 동일 |
| `velocity_smoother.ros__parameters.velocity_timeout` | [357](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:357) | `1.0` | `1.0` | 공식과 동일 |
| `waypoint_follower.ros__parameters.action_server_result_timeout` | [338](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:338) | `900.0` | `900.0` | 공식과 동일 |
| `waypoint_follower.ros__parameters.loop_rate` | [336](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:336) | `20` | `20` | 공식과 동일 |
| `waypoint_follower.ros__parameters.stop_on_failure` | [337](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:337) | `false` | `false` | 공식과 동일 |
| `waypoint_follower.ros__parameters.wait_at_waypoint.enabled` | [342](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:342) | `true` | `true` | 공식과 동일 |
| `waypoint_follower.ros__parameters.wait_at_waypoint.plugin` | [341](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:341) | `"nav2_waypoint_follower::WaitAtWaypoint"` | `"nav2_waypoint_follower::WaitAtWaypoint"` | 공식과 동일 |
| `waypoint_follower.ros__parameters.wait_at_waypoint.waypoint_pause_duration` | [343](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:343) | `5` | `5` | 공식과 동일 |
| `waypoint_follower.ros__parameters.waypoint_task_executor_plugin` | [339](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:339) | `"wait_at_waypoint"` | `"wait_at_waypoint"` | 공식과 동일 |

공식 원본: [ffw_navigation/config/navigation_mppi.yaml](/home/robotis/ai_worker/ffw_navigation/docs/reference/robotis_9bc7f7b9/ffw_navigation/config/navigation_mppi.yaml)

**ffw_navigation/config/mapper_params_online_sync.yaml — Mapping**

| 파라미터 경로 | 현재 파일 위치 | BGF 값 | 공식 파일 명시값 | 차이와 주의사항 |
|---|---|---|---|---|
| `slam_toolbox.ros__parameters.angle_variance_penalty` | [56](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:56) | `1.0` | `1.0` | 공식과 동일 |
| `slam_toolbox.ros__parameters.base_frame` | [12](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:12) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `slam_toolbox.ros__parameters.ceres_dogleg_type` | [7](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:7) | `"TRADITIONAL_DOGLEG"` | `"TRADITIONAL_DOGLEG"` | 공식과 동일 |
| `slam_toolbox.ros__parameters.ceres_linear_solver` | [4](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:4) | `"SPARSE_NORMAL_CHOLESKY"` | `"SPARSE_NORMAL_CHOLESKY"` | 공식과 동일 |
| `slam_toolbox.ros__parameters.ceres_loss_function` | [8](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:8) | `"None"` | `"None"` | 공식과 동일 |
| `slam_toolbox.ros__parameters.ceres_preconditioner` | [5](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:5) | `"SCHUR_JACOBI"` | `"SCHUR_JACOBI"` | 공식과 동일 |
| `slam_toolbox.ros__parameters.ceres_trust_strategy` | [6](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:6) | `"LEVENBERG_MARQUARDT"` | `"LEVENBERG_MARQUARDT"` | 공식과 동일 |
| `slam_toolbox.ros__parameters.check_min_dist_and_heading_precisely` | [35](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:35) | `false` | `false` | 공식과 동일 |
| `slam_toolbox.ros__parameters.coarse_angle_resolution` | [60](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:60) | `0.0349` | `0.0349` | 공식과 동일 |
| `slam_toolbox.ros__parameters.coarse_search_angle_offset` | [59](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:59) | `0.349` | `0.349` | 공식과 동일 |
| `slam_toolbox.ros__parameters.correlation_search_space_dimension` | [47](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:47) | `0.5` | `0.5` | 공식과 동일 |
| `slam_toolbox.ros__parameters.correlation_search_space_resolution` | [48](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:48) | `0.01` | `0.01` | 공식과 동일 |
| `slam_toolbox.ros__parameters.correlation_search_space_smear_deviation` | [49](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:49) | `0.1` | `0.1` | 공식과 동일 |
| `slam_toolbox.ros__parameters.debug_logging` | [17](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:17) | `false` | `false` | 공식과 동일 |
| `slam_toolbox.ros__parameters.distance_variance_penalty` | [55](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:55) | `0.5` | `0.5` | 공식과 동일 |
| `slam_toolbox.ros__parameters.do_loop_closing` | [41](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:41) | `true` | `true` | 공식과 동일 |
| `slam_toolbox.ros__parameters.enable_interactive_mode` | [29](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:29) | `true` | `true` | 공식과 동일 |
| `slam_toolbox.ros__parameters.fine_search_angle_offset` | [58](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:58) | `0.00349` | `0.00349` | 공식과 동일 |
| `slam_toolbox.ros__parameters.link_match_minimum_response_fine` | [38](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:38) | `0.1` | `0.1` | 공식과 동일 |
| `slam_toolbox.ros__parameters.link_scan_maximum_distance` | [39](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:39) | `1.5` | `1.5` | 공식과 동일 |
| `slam_toolbox.ros__parameters.loop_match_maximum_variance_coarse` | [43](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:43) | `3.0` | `3.0` | 공식과 동일 |
| `slam_toolbox.ros__parameters.loop_match_minimum_chain_size` | [42](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:42) | `10` | `10` | 공식과 동일 |
| `slam_toolbox.ros__parameters.loop_match_minimum_response_coarse` | [44](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:44) | `0.35` | `0.35` | 공식과 동일 |
| `slam_toolbox.ros__parameters.loop_match_minimum_response_fine` | [45](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:45) | `0.45` | `0.45` | 공식과 동일 |
| `slam_toolbox.ros__parameters.loop_search_maximum_distance` | [40](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:40) | `3.0` | `3.0` | 공식과 동일 |
| `slam_toolbox.ros__parameters.loop_search_space_dimension` | [51](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:51) | `8.0` | `8.0` | 공식과 동일 |
| `slam_toolbox.ros__parameters.loop_search_space_resolution` | [52](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:52) | `0.05` | `0.05` | 공식과 동일 |
| `slam_toolbox.ros__parameters.loop_search_space_smear_deviation` | [53](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:53) | `0.03` | `0.03` | 공식과 동일 |
| `slam_toolbox.ros__parameters.map_frame` | [11](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:11) | `"map"` | `"map"` | 공식과 동일 |
| `slam_toolbox.ros__parameters.map_update_interval` | [20](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:20) | `1.0` | `5.0` | 변경 |
| `slam_toolbox.ros__parameters.max_laser_range` | [24](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:24) | `20.0` | `20.0` | 공식과 동일 |
| `slam_toolbox.ros__parameters.min_laser_range` | [23](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:23) | `0.0` | `0.0` | 공식과 동일 |
| `slam_toolbox.ros__parameters.min_pass_through` | [64](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:64) | `2` | `2` | 공식과 동일 |
| `slam_toolbox.ros__parameters.minimum_angle_penalty` | [61](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:61) | `0.9` | `0.9` | 공식과 동일 |
| `slam_toolbox.ros__parameters.minimum_distance_penalty` | [62](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:62) | `0.5` | `0.5` | 공식과 동일 |
| `slam_toolbox.ros__parameters.minimum_time_interval` | [25](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:25) | `0.5` | `0.5` | 공식과 동일 |
| `slam_toolbox.ros__parameters.minimum_travel_distance` | [33](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:33) | `0.1` | `0.5` | 변경 |
| `slam_toolbox.ros__parameters.minimum_travel_heading` | [34](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:34) | `0.1` | `0.5` | 변경 |
| `slam_toolbox.ros__parameters.mode` | [15](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:15) | `"mapping"` | `"mapping"` | 공식과 동일 |
| `slam_toolbox.ros__parameters.occupancy_threshold` | [65](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:65) | `0.1` | `0.1` | 공식과 동일 |
| `slam_toolbox.ros__parameters.odom_frame` | [10](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:10) | `"odom"` | `"odom"` | 공식과 동일 |
| `slam_toolbox.ros__parameters.resolution` | [21](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:21) | `0.05` | `0.05` | 공식과 동일 |
| `slam_toolbox.ros__parameters.restamp_tf` | [22](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:22) | `false` | `false` | 공식과 동일 |
| `slam_toolbox.ros__parameters.scan_buffer_maximum_scan_distance` | [37](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:37) | `10.0` | `10.0` | 공식과 동일 |
| `slam_toolbox.ros__parameters.scan_buffer_size` | [36](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:36) | `10` | `10` | 공식과 동일 |
| `slam_toolbox.ros__parameters.scan_topic` | [13](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:13) | `"/scan"` | `"/scan"` | 공식과 동일 |
| `slam_toolbox.ros__parameters.solver_plugin` | [3](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:3) | `"solver_plugins::CeresSolver"` | `"solver_plugins::CeresSolver"` | 공식과 동일 |
| `slam_toolbox.ros__parameters.stack_size_to_use` | [28](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:28) | `40000000` | `40000000` | 공식과 동일 |
| `slam_toolbox.ros__parameters.tf_buffer_duration` | [27](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:27) | `30.0` | `30.0` | 공식과 동일 |
| `slam_toolbox.ros__parameters.throttle_scans` | [18](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:18) | `1` | `1` | 공식과 동일 |
| `slam_toolbox.ros__parameters.transform_publish_period` | [19](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:19) | `0.02` | `0.02` | 공식과 동일 |
| `slam_toolbox.ros__parameters.transform_timeout` | [26](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:26) | `0.2` | `0.2` | 공식과 동일 |
| `slam_toolbox.ros__parameters.use_map_saver` | [14](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:14) | `true` | `true` | 공식과 동일 |
| `slam_toolbox.ros__parameters.use_response_expansion` | [63](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:63) | `true` | `true` | 공식과 동일 |
| `slam_toolbox.ros__parameters.use_scan_barycenter` | [32](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:32) | `true` | `true` | 공식과 동일 |
| `slam_toolbox.ros__parameters.use_scan_matching` | [31](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:31) | `true` | `true` | 공식과 동일 |

공식 원본: [ffw_navigation/config/mapper_params_online_sync.yaml](/home/robotis/ai_worker/ffw_navigation/docs/reference/robotis_9bc7f7b9/ffw_navigation/config/mapper_params_online_sync.yaml)

**ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml — SH5 베이스**

| 파라미터 경로 | 현재 파일 위치 | BGF 값 | 공식 파일 명시값 | 차이와 주의사항 |
|---|---|---|---|---|
| `/**.swerve_drive_controller.ros__parameters.angular.z.has_acceleration_limits` | [218](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:218) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.angular.z.has_jerk_limits` | [220](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:220) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.angular.z.has_velocity_limits` | [216](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:216) | `false` | `false` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.angular.z.max_acceleration` | [219](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:219) | `1.5` | `1.5` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.angular.z.max_jerk` | [221](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:221) | `3.0` | `3.0` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.angular.z.max_velocity` | [217](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:217) | `1.7` | `1.7` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.angular_vel_deadband` | [141](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:141) | `0.005` | `파일에 명시 없음` | 변경 |
| `/**.swerve_drive_controller.ros__parameters.base_frame_id` | [170](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:170) | `"base_link"` | `"base_link"` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.cmd_vel_timeout` | [138](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:138) | `1.0` | `1.0` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.direct_joint_command_timeout_sec` | [184](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:184) | `1.0` | `1.0` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.direct_joint_command_topic` | [185](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:185) | `"~/direct_joint_commands"` | `"~/direct_joint_commands"` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.enable_direct_joint_commands` | [183](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:183) | `false` | `false` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.enable_odom_tf` | [172](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:172) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.enable_visualization` | [178](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:178) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.enabled_open_loop` | [161](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:161) | `false` | `false` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.enabled_speed_limits` | [191](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:191) | `false` | `false` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.enabled_steering_angular_limit` | [187](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:187) | `false` | `false` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.enabled_steering_angular_velocity_limit` | [155](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:155) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.enabled_steering_flip` | [154](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:154) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.enabled_wheel_saturation_scaling` | [164](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:164) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.x.has_acceleration_limits` | [198](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:198) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.x.has_jerk_limits` | [201](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:201) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.x.has_velocity_limits` | [195](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:195) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.x.max_acceleration` | [199](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:199) | `0.5` | `0.5` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.x.max_jerk` | [202](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:202) | `1.0` | `1.0` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.x.max_velocity` | [196](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:196) | `1.5` | `1.5` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.x.min_acceleration` | [200](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:200) | `-0.5` | `-0.5` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.x.min_jerk` | [203](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:203) | `-1.0` | `-1.0` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.x.min_velocity` | [197](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:197) | `-1.5` | `-1.5` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.y.has_acceleration_limits` | [208](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:208) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.y.has_jerk_limits` | [211](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:211) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.y.has_velocity_limits` | [205](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:205) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.y.max_acceleration` | [209](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:209) | `0.5` | `0.5` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.y.max_jerk` | [212](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:212) | `1.0` | `1.0` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.y.max_velocity` | [206](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:206) | `1.5` | `1.5` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.y.min_acceleration` | [210](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:210) | `-0.5` | `-0.5` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.y.min_jerk` | [213](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:213) | `-1.0` | `-1.0` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear.y.min_velocity` | [207](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:207) | `-1.5` | `-1.5` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.linear_vel_deadband` | [140](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:140) | `0.005` | `파일에 명시 없음` | 변경 |
| `/**.swerve_drive_controller.ros__parameters.module_angle_offsets` | [145](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:145) | `[0.0, 0.0, 0.0]` | `[0.0, 0.0, 0.0]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.module_steering_limit_lower` | [146](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:146) | `[-6.28, -6.28, -6.28]` | `[-6.28, -6.28, -6.28]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.module_steering_limit_upper` | [147](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:147) | `[6.28, 6.28, 6.28]` | `[6.28, 6.28, 6.28]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.module_wheel_speed_limit_lower` | [150](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:150) | `[-50.0, -50.0, -50.0]` | `[-50.0, -50.0, -50.0]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.module_wheel_speed_limit_upper` | [151](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:151) | `[50.0, 50.0, 50.0]` | `[50.0, 50.0, 50.0]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.module_x_offsets` | [143](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:143) | `[0.1371, 0.1371, -0.2899]` | `[0.1371, 0.1371, -0.2899]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.module_y_offsets` | [144](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:144) | `[0.2554, -0.2554, 0.0]` | `[0.2554, -0.2554, 0.0]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.odom_frame_id` | [171](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:171) | `"odom"` | `"odom"` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.odom_integration_method` | [168](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:168) | `"euler"` | `"euler"` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.odom_solver_method` | [167](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:167) | `"svd"` | `"svd"` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.odom_source` | [169](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:169) | `"feedback"` | `"feedback"` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.pose_covariance_diagonal` | [173](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:173) | `[0.001, 0.001, 0.001, 0.001, 0.001, 0.001]` | `[0.001, 0.001, 0.001, 0.001, 0.001, 0.001]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.publish_limited_velocity` | [192](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:192) | `true` | `true` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.steering_alignment_angle_error_threshold` | [158](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:158) | `1.0` | `1.0` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.steering_alignment_start_angle_error_threshold` | [159](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:159) | `0.01` | `0.01` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.steering_alignment_start_speed_error_threshold` | [160](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:160) | `0.1` | `0.1` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.steering_angular_velocity_limit` | [156](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:156) | `100.0` | `100.0` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.steering_joint_names` | [133](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:133) | `["left_wheel_steer", "right_wheel_steer", "rear_wheel_steer"]` | `["left_wheel_steer", "right_wheel_steer", "rear_wheel_steer"]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.steering_to_wheel_y_offsets` | [148](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:148) | `[0.0, -0.0, 0.0]` | `[0.0, -0.0, 0.0]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.twist_covariance_diagonal` | [174](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:174) | `[0.001, 0.001, 0.001, 0.001, 0.001, 0.001]` | `[0.001, 0.001, 0.001, 0.001, 0.001, 0.001]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.velocity_rolling_window_size` | [175](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:175) | `10` | `10` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.visualization_marker_topic` | [179](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:179) | `"swerve_visualization_markers"` | `"swerve_visualization_markers"` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.visualization_update_time` | [180](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:180) | `0.1` | `0.1` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.wheel_joint_names` | [135](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:135) | `["left_wheel_drive", "right_wheel_drive", "rear_wheel_drive"]` | `["left_wheel_drive", "right_wheel_drive", "rear_wheel_drive"]` | 공식과 동일 |
| `/**.swerve_drive_controller.ros__parameters.wheel_radius` | [137](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:137) | `0.0825` | `0.0865` | 변경 |

공식 원본: [ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml](/home/robotis/ai_worker/ffw_navigation/docs/reference/robotis_9bc7f7b9/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml)
