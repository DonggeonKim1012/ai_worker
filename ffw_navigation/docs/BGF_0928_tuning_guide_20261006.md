# 1109 BGF navigation 복원과 튜닝 안내

1109의 주행 기본 설정을 BGF_navigation_0928 커밋 `5745b7a5f15f236e51cd9d9a0cd3c3f776ea129c`로 복원했다. Run은 두 개의 MPPI Omni controller와 기본 SmacPlannerHybrid를 사용한다. 경로 길이 2 m로 controller를 선택하며 RotationShim, DiffDrive 주행 모델, 남은 거리 0.6 m 전환, ExactGoal 연결은 이 버전에 없다.

공식 비교 기준은 ROBOTIS-GIT/ai_worker main의 `9bc7f7b93ee118f4f3f47016d2f2314c0d0895e4`이다. 공식 기본 navigation.yaml은 RPP와 Navfn을 사용하고, 공식 navigation_mppi.yaml은 MPPI Omni 두 개와 Smac Hybrid를 사용한다. MPPI 튜닝 차이는 같은 알고리즘인 공식 MPPI 파일과 비교한다. [공식 MPPI 파일](https://github.com/ROBOTIS-GIT/ai_worker/blob/9bc7f7b93ee118f4f3f47016d2f2314c0d0895e4/ffw_navigation/config/navigation_mppi.yaml)

BGF 보관본의 upstream 기준은 `21bebbb968fea3364f513191ff25c48d1c3856f5`다. 최신 공식 main과의 비교에는 upstream 버전 차이도 포함된다. 특히 wheel_radius 등의 값 차이를 모두 1109에서 새로 실험해 튜닝한 이력으로 해석하지 않는다. 아래 표는 고정된 두 소스에서 실제로 확인한 값 차이다.

주요 파라미터를 아래에서 설명하고, 명시된 전체 값과 현재 파일 줄번호는 [파라미터 위치 목록](BGF_0928_parameter_index_20261006.md)에 정리했다. [공식과 달라진 62개 항목 CSV](BGF_0928_official_changes_20261006.csv), [전체 1103개 항목 CSV](BGF_0928_parameters_20261006.csv), [공식 대비 텍스트 diff](BGF_0928_vs_ROBOTIS_9bc7f7b.patch)도 함께 사용할 수 있다. 항목 수에는 세 navigation 프로필, SLAM, 베이스의 명시값과 삭제된 공식 키가 포함된다.

줄번호는 2026년 10월 6일 복원본 기준이다. 이후 줄이 이동하면 표의 블록 이름과 키로 검색한다. 호스트 `/home/robotis/ai_worker`는 컨테이너 `/root/ros2_ws/src/ai_worker`와 같은 소스다.

**Run 주행을 튜닝할 파일은 navigation_mppi_1109.yaml이다.**

| 파일과 위치 | 실행 경로와 역할 | 직접 수정할 내용 |
|---|---|---|
| [launch/navigation.launch.py:68](/home/robotis/ai_worker/ffw_navigation/launch/navigation.launch.py:68) | 기본 params_file 지정 | 공식은 navigation.yaml, BGF는 navigation_mppi_1109.yaml. rviz 기본값도 공식 false에서 BGF true |
| [config/navigation_mppi_1109.yaml:1](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:1) | Run 기본, Mapping 시 Nav2 설정 | controller·planner·costmap·AMCL·스무더 |
| [config/navigation.yaml:41](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:41) | 공식 RPP 프로필, Cyclo Design 위치추정의 AMCL 입력 | RPP를 명시적으로 선택할 때의 설정. Run 기본 MPPI 튜닝에는 사용되지 않음 |
| [config/navigation_mppi.yaml:1](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi.yaml:1) | 공식 MPPI 선택 프로필 | BGF 1109 튜닝 전 원본과 비교할 때 사용 |
| [config/navigation_mppi_robotis_official.yaml:1](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_robotis_official.yaml:1) | 공식 MPPI 원본 보관 | 비교 기준으로 보존 |
| [config/bt/nav_modes_1109.xml:20](/home/robotis/ai_worker/ffw_navigation/config/bt/nav_modes_1109.xml:20) | Run controller 선택·복구 정책 | 2 m 기준, controller ID, 재계획·복구 순서 |
| [docker/s6-services/ai_worker_navigation/run:8](/home/robotis/ai_worker/docker/s6-services/ai_worker_navigation/run:8) | map/nav 모드와 지도 결정 | 지도 이름·실행 인자 연결 |

복원한 navigation.yaml과 navigation_mppi.yaml은 위 공식 main 파일과 바이트 단위로 같다. 이름이 유사해도 실제로 선택된 params_file을 확인해야 한다. 기본 launch는 navigation_mppi_1109.yaml을 읽는다.

Cyclo의 Design 위치추정 전용 경로는 [navigation.py:65](/mnt/ssd/cyclo_intelligence/docker/supervisor_api/navigation.py:65)의 NAVIGATION_PARAMS_FILE로 navigation.yaml을 읽는다. 복원 후 Design은 Differential AMCL, Run은 Omni AMCL이다. 이 차이도 BGF 기준 설정 그대로다. 위치추정 일관성을 바꾸려면 별도 수정으로 두 경로의 AMCL 또는 실행 파일 선택을 맞춘다.

**MPPI의 두 controller는 모두 Omni 모델이다.**

| 설정과 위치 | OmniController | CurveController | 공식과의 관계 |
|---|---:|---:|---|
| plugin, [48행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:48) / [111행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:111) | MPPIController | MPPIController | 동일 |
| motion_model, [52행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:52) / [115행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:115) | Omni | Omni | 동일. Curve라는 이름은 DiffDrive 모델을 뜻하지 않음 |
| vx_max | 0.35 | 0.35 | 공식 0.55 / 0.50에서 낮춤 |
| vx_min | -0.35 | 0.0 | 공식 -0.55 / 0.0. Omni만 후진 명령 허용 |
| vy_max | 0.35 | 0.25 | 공식 0.55 / 0.25. Curve도 횡이동 가능 |
| wz_max | 0.7 | 0.7 | 공식 0.8 / 1.6에서 낮춤 |
| ax_max / ax_min | 0.5 / -0.5 | 0.5 / -0.5 | 공식 Omni 3 / -3에서 낮춤. Curve는 공식 파일에 없던 제한을 명시 |
| ay_max / ay_min | 0.5 / -0.5 | 0.5 / -0.5 | 같은 이유로 횡가속도 제한 |
| az_max | 1.2 | 1.2 | 공식 Omni 3에서 낮춤. Curve는 새로 명시 |

속도 단위는 m/s, 회전 속도는 rad/s, 가속도는 m/s²와 rad/s²다. 두 controller의 속도·가속도는 [57행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:57), [119행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:119)에서 수정한다. `vy_min`도 파일에 적혀 있지만 설치된 MPPI 1.3.11은 이 키를 읽지 않는다. 횡속도는 vy_max를 양방향 상한으로 사용한다.

속도를 올릴 때는 controller 값과 [velocity_smoother:368](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:368)을 같이 확인한다. 예측 속도보다 스무더 상한이 낮으면 실제 명령이 제한되어 예측과 실행이 달라진다. 가속도도 같은 관계다. [MPPI 1.3.11 구현](https://github.com/ros-navigation/navigation2/blob/1.3.11/nav2_mppi_controller/src/optimizer.cpp)

**예측 범위와 샘플링 값은 공식 MPPI에서 유지한 값이다.**

| 키 | Omni / Curve 값 | 튜닝할 때 바뀌는 성질 |
|---|---|---|
| time_steps / model_dt | 둘 다 40 / 0.05 | 예측 시간 2초. time_steps를 늘리면 예측 범위와 계산량 증가 |
| batch_size | 둘 다 1200 | 후보 궤적 수. 증가하면 더 많은 후보를 평가 |
| iteration_count | 4 / 1 | 최적화 반복. Omni는 BGF 원래 값인 4로 복원 |
| vx_std | 0.15 / 0.17 | 전후 속도 후보의 분산 |
| vy_std | 0.15 / 0.12 | 횡속도 후보의 분산 |
| wz_std | 0.35 / 0.3 | 회전 속도 후보의 분산 |
| temperature | 0.25 / 0.27 | 비용별 후보 가중 분포 |
| gamma | 0.018 / 0.02 | 제어 비용 항의 비중 |
| visualize | 둘 다 false | 궤적 시각화. 켜면 디버깅 출력·계산 부담 증가 |

위치는 Omni [49행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:49), Curve [112행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:112)이다. controller_frequency=20 Hz와 model_dt=0.05초가 대응한다. 주기를 바꾸면 이 관계와 CPU 제어 주기를 함께 검토한다. 과거 1109 기록에는 Omni iteration 4에서 목표 20 Hz를 못 맞춘 사례가 있지만, 이번 복원에서는 원래 값 4를 유지했다.

**Critic weight를 바꾸면 속도 상한 안에서 선택하는 움직임이 달라진다.**

| Critic와 위치 | BGF 값 | 공식 대비 | 효과와 조정 기준 |
|---|---|---|---|
| ConstraintCritic, [80행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:80) / [145행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:145) | weight 4 / 4 | 동일 | 운동 제약 위반 후보 억제 |
| GoalCritic, [84행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:84) / [149행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:149) | weight 5 / 5, 거리 1.2 / 1.2 m | 동일 | 목표 위치 접근 비용 |
| GoalAngleCritic, [89행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:89) / [155행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:155) | weight 5 / 2, 거리 0.25 / 0.3 m | 동일 | 목표 근처 yaw 정렬. threshold는 접근 거리 조건이며 각도 허용오차가 아님 |
| CostCritic, [94행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:94) / [167행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:167) | weight 4 / 4.2, footprint true | footprint false → true | 차체 형상을 고려한 장애물 비용·충돌 평가 |
| PathFollowCritic, [103행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:103) / [187행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:187) | weight 5 / 6 | 동일 | 경로를 따라 진행하는 성향 |
| PathAlignCritic, [177행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:177) | Curve만 weight 14, use_path_orientations=true | 동일 | 경로 위치·자세 정렬 |
| PathAngleCritic, [194행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:194) | Curve만 weight 6, mode 0 | 동일 | 경로 진행 방향과의 각도 평가 |
| PreferForwardCritic, [161행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:161) | Curve만 weight 9 | 동일 | 후진 비용을 높여 전진 선호 |

cost_weight는 해당 비용의 상대적 비중이며 단독으로 성공 동작을 보장하지 않는다. cost_power는 비용에 적용할 지수, offset_from_furthest는 경로 점 기준 오프셋, trajectory_point_step은 평가 샘플 간격이다. `critics` 목록에서 빠진 critic은 해당 controller에서 실행되지 않는다. weight 증가로 다른 비용과의 균형이 달라지므로 한 종류씩 조정하고 실제 출력과 궤적을 확인한다. [MPPI critic 설명](https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/controller_plugins/mppi_controller/configuring_mppic/)

**도착 조건과 정체 판단은 서로 다른 블록에서 정한다.**

| 키와 위치 | 공식 MPPI | BGF | 의미 |
|---|---|---|---|
| failure_tolerance, [30행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:30) | 0.3 s | 1.0 s | 제어 계산 실패를 허용하는 시간. 목표 도착 timeout과 다름 |
| progress_checker.plugin, [37행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:37) | SimpleProgressChecker | PoseProgressChecker | 위치뿐 아니라 회전도 진행으로 판단 |
| required_movement_radius | 0.5 m | 0.02 m | 위치 진행 기준 |
| required_movement_angle | 명시 없음 | 0.02 rad | 회전 진행 기준, 약 1.15° |
| movement_time_allowance | 10 s | 20 s | 진행이 없으면 실패하는 시간 |
| xy_goal_tolerance, [43행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:43) | 0.2 m | 0.025 m | 도착 위치 허용오차 |
| yaw_goal_tolerance | 0.05 rad | 0.02 rad | 도착 yaw 허용오차 |
| stateful | true | false | 최종 회전 중에도 XY를 재검사 |

controller의 min_x/y/theta_velocity_threshold=0.001은 odometry 입력의 작은 속도를 0으로 취급하는 기준이다. 출력 최소 속도나 베이스 deadband가 아니다. 목표 오차는 추정 pose에 대한 판정이며 물리 도착 정확도와 구분한다.

**차체 형상과 장애물 주변 비용은 local과 global에서 함께 관리한다.**

| 파라미터와 위치 | 공식 MPPI | BGF | 튜닝 영향 |
|---|---|---|---|
| Local footprint, [217행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:217) | robot_radius=0.44 m 원 | SH5 17점 다각형 | 비대칭 차체와 조향 바퀴 회전 범위 반영 |
| Global footprint, [255행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:255) | 같은 원 | 같은 다각형 | 전역 경로 충돌 검사에 사용할 형상 |
| footprint_padding | 명시 없음 | 양쪽 0.02 m | 형상 주변 여유 |
| Local resolution, [214행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:214) | 0.05 m | 0.025 m | 근거리 장애물 표현 세밀화 |
| Local update_frequency, [206행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:206) | 5 Hz | 10 Hz | 센서에 따른 비용 갱신 빈도 |
| Local inflation_radius, [224행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:224) | 0.65 m | 0.48 m | 장애물 주변 비용 띠 범위 |
| Local cost_scaling_factor | 3 | 10 | 더 빠른 비용 감쇠 |
| Global inflation_radius, [280행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:280) | 0.7 m | 0.55 m | 전역 경로의 장애물 접근 성향 |
| Global cost_scaling_factor | 3 | 5 | 전역 비용 감쇠 |
| Local scan.inf_is_valid, [233행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:233) | 명시 없음 | true | +inf no-return ray의 clearing 허용 |

footprint 좌표는 base_link 기준 m 단위다. 현재 외곽은 x=-0.403~0.25, y=-0.366~0.366이다. inflation은 실제 충돌 형상 밖에 만드는 비용 영역이며 차체와 벽 사이의 확보 거리를 직접 지정하는 값은 아니다. 벽에 가까이 가는 성향은 footprint, padding, inflation, MPPI CostCritic이 함께 결정한다. [Nav2 inflation 설명](https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/costmap_2d/costmap_plugins/inflation/)

Local은 3×3 m rolling window, odom frame, obstacle+inflation이고 Global은 map frame, 0.05 m, 1 Hz, static+obstacle+inflation이다. 이 값들은 공식 MPPI에서 유지했다. Local marking=true, Global marking=false도 유지했다. 움직이는 장애물 대응은 local에 의존하며 주기적 전역 재계획 정책은 기본 BT에 없다. Local static_layer 블록은 적혀 있지만 plugins 목록에 없어 실행되지 않는다.

Footprint를 바꾸면 [waypointClearance.js:18](/mnt/ssd/cyclo_intelligence/orchestrator/ui/src/features/missionCanvas/lib/waypointClearance.js:18)의 UI 형상도 대조한다. 실제 runner에서 그 검사 함수를 호출하는지까지 확인해야 UI 검사를 활성화했다고 말할 수 있다. 팔·적재물의 돌출을 반영하려면 실제 투영 형상을 기준으로 footprint를 설계한다.

**Smac Hybrid의 모델은 공식 MPPI와 같고 목표 tolerance만 더 엄격하다.**

위치는 [planner_server:283](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:283)이다. plugin은 `nav2_smac_planner::SmacPlannerHybrid`, 검색 모델은 REEDS_SHEPP, angle_quantization_bins=24이다. 360°/24=15° 간격이다. MPPI Omni와 AMCL Omni는 각각 제어 예측과 위치추정의 이동 모델이고, REEDS_SHEPP은 전역 경로 탐색 모델이다.

| 키 | 공식 MPPI → BGF | 튜닝 영향 |
|---|---|---|
| tolerance | 0.5 → 0.0 m | 가까운 대체 목표를 허용하는 fallback 범위 제거 |
| angle_quantization_bins | 24 → 24 | 방향 해상도와 검색 비용. 최종 yaw 양자화에도 영향 |
| max_iterations / max_on_approach_iterations | 40000 / 12000 유지 | 탐색 반복 한도 |
| analytic_expansion_ratio | 1.0 유지 | 목표에 직접 연결하는 analytic expansion 빈도 |
| non_straight_penalty / change_penalty | 10.5 / 2.0 유지 | 곡선 및 방향전환 비용 |
| smooth_path / cache_obstacle_heuristic | true / true 유지 | 내부 smoothing과 heuristic 재사용 |
| smoother.w_smooth / w_data | 0.9 / 0.05 유지 | 매끄러움과 원래 경로 보존의 균형 |

minimum_turning_radius=0.0은 내부에서 최소 검색 해상도로 보정된다. 현재 Global 해상도와 downsampling_factor=1 기준으로 0.05 m다. 이 키를 0으로 적는 것으로 전역 탐색이 Omni가 되지는 않는다.

다음 키는 복원 재현을 위해 파일에 보존했지만 Hybrid 1.3.11에서 사용되지 않는다: use_final_approach_orientation, allow_reverse, cost_travel_multiplier, cost_heuristic_multiplier, rotation_penalty. 후진 탐색은 REEDS_SHEPP 또는 DUBIN 선택으로 다루고, 실제 비용 조정은 지원 키인 reverse_penalty와 cost_penalty 등을 사용한다. [Hybrid 1.3.11 구현](https://github.com/ros-navigation/navigation2/blob/1.3.11/nav2_smac_planner/src/smac_planner_hybrid.cpp)

ExactGoal 보정을 제거했으므로 waypoint yaw와 양자화된 경로 끝 yaw가 다를 수 있다. GoalAngleCritic weight나 goal checker tolerance를 바꾸는 것만으로 planner가 원래 yaw를 그대로 반환하게 되는 것은 아니다.

**Velocity smoother는 세 속도 축을 함께 제한한다.**

[362행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:362)에서 수정한다. 배열 순서는 `[vx, vy, wz]`다.

| 키 | 공식 MPPI | BGF |
|---|---|---|
| max_velocity / min_velocity | ±[0.5,0.5,2.0] | ±[0.35,0.35,0.7] |
| max_accel | [2.5,2.5,3.2] | [0.5,0.5,1.2] |
| max_decel | [-2.5,-2.5,-3.2] | [-0.5,-0.5,-1.2] |
| scale_velocities | false | true |
| smoothing_frequency / feedback | 20 / OPEN_LOOP | 동일 |
| deadband_velocity | [0,0,0] | 동일 |
| velocity_timeout | 1.0 s | 동일 |

OPEN_LOOP는 이전 출력 속도를 기준으로 smoothing한다는 뜻이다. 베이스의 enabled_open_loop=false 및 wheel feedback odometry와 별개다. scale_velocities=true는 축별 제한이 걸릴 때 속도 성분 비율을 함께 조정한다.

Collision monitor의 [FootprintApproach:398](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:398)은 enabled=false로 공식 MPPI와 같다. time_before_collision=1.0과 min_points=6은 이 polygon을 활성화했을 때 적용된다. costmap·MPPI 장애물 회피는 별도로 동작한다. 별도 smoother_server도 등록되어 있지만 현재 BT에 SmoothPath 호출이 없어 그 설정이 현재 경로 smoothing을 수행하지 않는다.

**AMCL은 공식 MPPI의 Omni 모델을 유지하면서 갱신 조건과 관측 수를 바꿨다.**

[437행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:437)에서 수정한다.

| 키 | 공식 MPPI | BGF | 효과 |
|---|---:|---:|---|
| robot_model_type | OmniMotionModel | 동일 | 횡이동을 포함한 odometry 이동 모델 |
| max_beams | 60 | 80 | 관측에 사용할 라이다 beam 수 증가 |
| min_particles | 500 | 800 | 최소 위치 후보 수 증가 |
| max_particles | 2000 | 2000 | 동일 |
| update_min_d | 0.25 m | 0.02 m | 작은 이동에서도 업데이트 |
| update_min_a | 0.01 rad | 0.02 rad | 회전 갱신 기준 변경 |

alpha1~alpha5=0.4, likelihood_field, sigma_hit=0.2, resample_interval=1, pf_err=0.05, z_hit=0.5, z_rand=0.5는 공식 MPPI 값이다. alpha는 odometry 오차 가정, sigma_hit는 관측 일치 폭, particles·beams·갱신 기준은 추정 품질과 계산량에 영향을 준다. 초기 pose는 map 좌표계이며 x/y/yaw를 실제 시작 위치에 맞춘다.

Run AMCL을 수정해도 Design 전용 AMCL 설정은 자동으로 바뀌지 않는다. Design은 복원된 navigation.yaml [274행](/home/robotis/ai_worker/ffw_navigation/config/navigation.yaml:274)을 읽고, Cyclo가 max_beams 등 일부 파라미터를 런타임에 덮어쓸 수 있다. 실제 값은 해당 모드가 켜진 상태에서 ros2 param dump /amcl로 확인한다.

**Mapping은 SLAM 파일의 세 값이 공식과 다르다.**

| 위치와 키 | 공식 | BGF | 효과 |
|---|---:|---:|---|
| [mapper_params_online_sync.yaml:20](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:20), map_update_interval | 5 s | 1 s | 지도 발행 갱신 간격 단축 |
| [33행](/home/robotis/ai_worker/ffw_navigation/config/mapper_params_online_sync.yaml:33), minimum_travel_distance | 0.5 m | 0.1 m | 더 작은 이동을 scan 처리 조건에 반영 |
| 34행, minimum_travel_heading | 0.5 rad | 0.1 rad | 회전 조건 세밀화 |

CeresSolver, 0.05 m 해상도, loop closure와 나머지 명시값은 공식과 같다. SLAM 갱신은 시간·scan matching·거리 조건을 함께 따른다. 이 값만 바꾸어 일정 발행·처리 주기를 보장한다고 해석하지 않는다. [bgf_0923_3.yaml](/home/robotis/ai_worker/ffw_navigation/maps/bgf_0923_3.yaml:1)의 resolution과 origin은 저장 waypoint의 좌표 해석에도 영향을 준다.

**BT의 2 m는 경로 길이 기준이며 controller 선택 정책이다.**

공식 nav_modes.xml의 ReactiveFallback을 BGF에서는 [nav_modes_1109.xml:20](/home/robotis/ai_worker/ffw_navigation/config/bt/nav_modes_1109.xml:20)의 IfThenElse로 바꿨다. controller 실패가 다른 controller로 숨겨지지 않고 RecoveryNode에 전달되도록 한 변경이다.

- 전체 path 길이 ≤2 m면 OmniController, >2 m면 CurveController를 사용한다.
- IfThenElse가 FollowPath를 실행하는 동안 해당 branch를 유지한다. 목표가 바뀌거나 재시도하면 다시 평가할 수 있다.
- [is_path_length_under.cpp:56](/home/robotis/ai_worker/ffw_navigation/src/is_path_length_under.cpp:56)은 경로 점 사이의 거리 합을 계산한다. 목표 직선거리나 남은 거리가 아니다. 이 C++는 공식과 동일하다.
- [8행](/home/robotis/ai_worker/ffw_navigation/config/bt/nav_modes_1109.xml:8)의 GoalUpdatedController는 기본 주행 중 주기적 전역 재계획을 하지 않는다.
- 외부 RecoveryNode 재시도는 6회, 내부 planner/controller 복구는 각각 1회다. 복구는 costmap clearing, Spin 1.57 rad, Wait 5 s, BackUp 0.3 m/0.15 m/s 순환이다.

YAML [15행](/home/robotis/ai_worker/ffw_navigation/config/navigation_mppi_1109.yaml:15)에서 두 navigator의 BT 경로를 BGF XML로 지정했고 plugin_lib_names는 is_path_length_under_plugin만 남겼다. Jazzy 내장 BT 노드는 자동 등록되므로 공식 파일의 nav2_behavior_tree 항목을 제거했다. default_server_timeout은 20→1000 ms, progress_checker_plugin 단수 키는 progress_checker_plugins 배열로 바꿨다. BT loop duration과 service timeout은 ms 단위이며 action_server_result_timeout은 s 단위다.

BGF의 두 navigator가 같은 단일 목표용 XML을 가리키는 점도 복원했다. 현재 Cyclo는 여러 waypoint를 NavigateThroughPoses로 묶을 수 있으나 이 XML은 ComputePathToPose와 {goal}을 사용한다. 다중 목표용 연결은 별도 수정이 필요하다. 현재 baseline을 보존하려고 자동 수정하지 않았다. Nav2 waypoint_follower의 waypoint_pause_duration=5는 1.3.11에서 5 ms이며, Mission Canvas의 waypoint 작업 대기 시간과도 별개다.

**라이다 튜닝은 SH5 bringup launch에서 한다.**

| 파일과 위치 | 공식 → BGF | 영향 |
|---|---|---|
| [ffw_sh5_follower_ai.launch.py:428](/home/robotis/ai_worker/ffw_bringup/launch/ffw_sh5_follower_ai.launch.py:428) | 장치 기본 범위 45~315° → SH5 override 50~310° | 센서 시야 끝의 차체 자기반사 제외 |
| [465행](/home/robotis/ai_worker/ffw_bringup/launch/ffw_sh5_follower_ai.launch.py:465) | enable_average_filter true → false | 거리 불연속을 평균해 허위 중간점을 만드는 경로 비활성 |
| [464행](/home/robotis/ai_worker/ffw_bringup/launch/ffw_sh5_follower_ai.launch.py:464) | enable_shadow_filter true 유지 | 그림자 필터 유지 |
| [lidar_dual.launch.py:95](/home/robotis/ai_worker/ffw_bringup/launch/lidar_dual.launch.py:95) | 센서 기본값은 유지 | IP·port·scan frequency·개별 scan 설정 |
| [ffw_sh5_follower.urdf.xacro:48](/home/robotis/ai_worker/ffw_description/urdf/ffw_sh5_rev1_follower/ffw_sh5_follower.urdf.xacro:48) | lidar 장착 TF는 현재 공식과 동일 | 왼쪽/오른쪽 센서의 위치·방향 |

현재 SH5 launch에는 Task별 팔·손·리프트·카메라 설정도 있다. navigation 복원을 위해 파일 전체를 옛 버전으로 덮어쓰지 않았으며, 라이다와 병합 설정 부분은 BGF와 동일함을 확인했다. 센서 장착 TF를 바꾸면 AMCL과 장애물 좌표가 함께 바뀐다. URDF의 visual/inertia와 Nav2의 2D footprint는 별개의 표현이다.

**베이스는 BGF 당시 설치 바이너리를 유지한다.**

파일은 [ffw_sh5_follower_ai_hardware_controller.yaml:131](/home/robotis/ai_worker/ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml:131)이다. 공식 main 대비 베이스 명시값 차이는 wheel_radius와 두 deadband다.

| 위치와 키 | 공식 main 명시값 | BGF | 의미 |
|---|---|---:|---|
| 137행, wheel_radius | 0.0865 m | 0.0825 m | 차체 속도와 wheel rad/s 변환 및 odometry 거리 척도 |
| 140행, linear_vel_deadband | 명시 없음 | 0.005 m/s | 더 작은 선속도 명령 제거 |
| 141행, angular_vel_deadband | 명시 없음 | 0.005 rad/s | 더 작은 회전 명령 제거 |
| 158행, steering_alignment_angle_error_threshold | 1.0 rad | 1.0 rad | 움직이는 바퀴의 정렬 조건 |
| 159행, steering_alignment_start_angle_error_threshold | 0.01 rad | 0.01 rad | 정지한 바퀴가 출발하기 위한 조향 오차 조건 |
| 160행, steering_alignment_start_speed_error_threshold | 0.1 rad/s | 0.1 rad/s | 정지/이동 상태 구분에 사용하는 바퀴 속도 기준 |
| 191행, enabled_speed_limits | false | false | 아래 linear/angular limiter 비활성 |

조향 기준 1.0/0.01은 공식 대비 튜닝값이 아니라 복원 전 로컬 개선값 0.35/0.10에서 BGF 값으로 되돌린 것이다. 0.01 rad는 약 0.57°로 엄격하며, 과거 기록의 정렬 지연·정지 조건을 다시 포함한다. 베이스가 명령을 받아도 움직이지 않으면 cmd_vel, 조향 오차, joint_commanders, joint_states, odom을 함께 확인한다. 과거 설치 라이브러리 기본 deadband=0.1은 소스 기본값이나 “공식 파일에 명시 없음”과 구분한다.

module_x/y_offsets, module_angle_offsets, wheel speed 제한, steering flip, wheel feedback odometry는 파라미터 위치 목록에서 찾을 수 있다. 바퀴 반경·조향 영점·기하 값은 실제 보정에 근거해 수정한다. enabled_speed_limits=false 상태에서 linear.x.max_velocity만 수정해도 limiter는 작동하지 않는다.

구동 바이너리 SHA-256은 `a7dfbe4d0ad2662c8588688bed4a32ab5600505581d92c074910c529fd0043a8`로 BGF manifest와 같다. swerve C++를 재빌드하면 당시 바이너리 재현 조건이 달라진다. 베이스 알고리즘 수정은 [swerve_drive_controller.cpp](/home/robotis/ai_worker/ffw_swerve_drive_controller/src/swerve_drive_controller.cpp)와 [odometry.cpp](/home/robotis/ai_worker/ffw_swerve_drive_controller/src/odometry.cpp)에서 하지만 현재 소스와 설치 바이너리의 기능 차이를 먼저 대조해야 한다.

**편집한 파일의 종류에 맞게 적용하고 실제 값을 확인한다.**

1. Run 주행 성향은 navigation_mppi_1109.yaml에서 변경한다. 같은 값을 controller와 velocity_smoother에 일관되게 반영한다.
2. 기존 YAML·BT XML은 현재 symlink 설치라 소스에 연결되지만 실행 중인 노드가 자동으로 다시 읽지는 않는다. Mission Canvas runtime을 중지하고 다시 시작해 적용한다.
3. C++ 또는 새 설치 파일을 추가하면 컨테이너에서 ffw_navigation을 재빌드한다.
4. 베이스 YAML은 새 bringup 시작에 반영된다. 실행 중 적용은 base controller를 inactive→unconfigured→파라미터 적용→configure→active로 재설정한다. 이 과정은 odometry 상태에도 영향을 줄 수 있으므로 정지 상태에서 수행한다.
5. 라이다 launch·TF 변경은 해당 노드를 재시작해 읽는다. 전체 bringup 재시작은 팔·손 초기 동작도 포함할 수 있으므로 작업용 설정과 함께 검토한다.

컨테이너 빌드 명령:

```bash
docker exec ai_worker bash -c '
  source /opt/ros/jazzy/setup.bash
  source /root/ros2_ws/install/setup.bash
  cd /root/ros2_ws
  colcon build --base-paths src/ai_worker/ffw_navigation \
    --packages-select ffw_navigation --symlink-install \
    --cmake-args -DBUILD_TESTING=OFF
'
```

아래는 runtime이 시작된 후 읽기 전용으로 실제 설정을 확인하는 예다.

```bash
docker exec ai_worker bash -c '
  source /opt/ros/jazzy/setup.bash
  source /root/ros2_ws/install/setup.bash
  export ROS_DOMAIN_ID=30 RMW_IMPLEMENTATION=rmw_zenoh_cpp
  ros2 param get /controller_server OmniController.motion_model
  ros2 param get /controller_server OmniController.vx_max
  ros2 param get /controller_server CurveController.motion_model
  ros2 param get /planner_server SmacPlannerHybrid.plugin
  ros2 param get /bt_navigator default_nav_to_pose_bt_xml
  ros2 param dump /velocity_smoother
  ros2 param dump /amcl
  ros2 param dump /swerve_drive_controller
'
```

한 번의 튜닝에서는 변경 목적을 하나로 정하고, 같은 경로에서 변경 전후의 도착 오차·yaw 정렬 시간·제어 주기·장애물 거리·실제 바퀴 명령을 비교한다. 추정 pose와 물리 측정값은 구분해서 기록한다.

**복원 전 상태와 검증 기록은 백업에 보관한다.**

백업 위치는 `/home/robotis/navigation_backups/bgf0928_restore_20261006_033056`이다. `source/ffw_navigation`에는 기존 YAML·BT·커스텀 C++와 기록을, `source/ffw_bringup/...`에는 기존 베이스 YAML을 보관한다. `runtime_navigation.tar.gz`는 이전 navigation build/install 결과물이다. Git 상태·diff와 복원 manifest도 포함한다.

BGF의 ffw_navigation 20개 파일과 베이스 YAML은 복원 원본과 바이트 단위로 일치한다. 추가 지도 bgf_0923_1/2, RViz 진단 화면, 과거 docs는 보존했다. 이후 추가된 ExactGoal 및 controller 선택 C++·헤더·등록·테스트는 백업으로 옮기고 현재 빌드에서 제거했다. 베이스 외 다른 controller의 활성 상태는 유지했다.

실차 navigation은 작업 시작과 같은 중지 상태다. 실차 이동 목표 없이 ROS domain 91의 독립 환경에서 controller, planner, BT navigator, behavior, AMCL, velocity smoother, collision monitor의 active 상태와 실제 파라미터를 확인했다. 설치된 설정의 SHA-256은 BGF manifest와 같은 `2b6ac2317d156adc2057d5baf9876c7004f49494947615beb9cebd930210273d`다. 실주행 성공·도착 정확도는 별도 주행 측정 대상이다. [검증 결과](BGF_0928_validation_20261006.json)
