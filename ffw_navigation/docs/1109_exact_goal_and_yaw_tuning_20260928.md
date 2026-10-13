# 1109 waypoint 성공 판정 및 yaw 정렬 개선 (2026-09-28)

## 확인한 원인

사용자가 기본 이동과 yaw 정렬이 정상 동작한다고 확인한 뒤, `bgf_0923_3 / 0923_1`의
Waypoint 2 복귀에서 Canvas가 위치 2.3 cm / 각도 6.6° 오차를 보고했다.

실제 로봇의 `/compute_path_to_pose`에 **주행 명령 없이 경로만 요청**한 결과:

| 목표 | 저장된 yaw | 기존 경로 끝 yaw | 경로가 바꾼 각도 |
|---|---:|---:|---:|
| Waypoint 1 | -17.642198643° | -14.999986984° | 2.642211658° |
| Waypoint 2 | -112.702689936° | -119.999993321° | 7.297303386° |

기존 `SmacPlannerHybrid.angle_quantization_bins: 24`는 15° 간격으로 goal heading을
양자화한다. Nav2의 controller는 경로 끝 자세를 기준으로 완료하지만 Canvas는 저장된
원래 waypoint를 검사하므로 서로 다른 목표를 검사했다. 마지막 보정 요청도 같은 planner를
거치므로 같은 잘못된 heading을 반환하고 즉시 성공할 수 있었다.
`use_final_approach_orientation`은 Hybrid가 사용하는 파라미터가 아니며 runtime에도 선언되지 않았다.

주행 로그의 별도 문제: 목표 20 Hz에 비해 실제 제어 주기가 반복해서 약 6–14 Hz로 떨어졌다.
짧은 경로에서 사용하는 Omni MPPI는 1200 samples × 40 steps × 4 iterations를 계산했다.
각도 critic은 목표 0.25 m 이내에서만 켜져 접근 후 마지막에 정렬이 집중됐다.
계산 반복 감소와 조기 정렬은 개선 가설이며, 개선 후 실제 소요 시간은 재주행 측정이 필요하다.

## 변경 파일 및 모델

### config/navigation_mppi_1109.yaml

| 항목 | 이전 | 변경 |
|---|---|---|
| `planner_server.SmacPlannerHybrid.plugin` | `nav2_smac_planner::SmacPlannerHybrid` | `ffw_navigation::ExactGoalSmacPlanner` |
| `OmniController.iteration_count` | 4 | 1 |
| `OmniController.GoalAngleCritic.threshold_to_consider` | 0.25 m | 0.60 m |
| `OmniController.GoalAngleCritic.cost_weight` | 5 | 8 |
| `CurveController.GoalAngleCritic.threshold_to_consider` | 0.30 m | 0.60 m |
| `CurveController.GoalAngleCritic.cost_weight` | 2 | 8 |

MPPI `motion_model: Omni`와 Hybrid `motion_model_for_search: REEDS_SHEPP`를 사용한다.
새 planner는 기존 SE2 footprint 경로 탐색을 상속하고, 마지막 양자화 자세에서 정확한
목표 자세까지 SH5의 전방향 이동/제자리 회전으로 실행 가능한 짧은 연결을 추가한다.
각도 구간 수를 늘리는 방법은 잔여 양자화 오차와 추가 탐색 비용이 있으므로 정확한 목표
연결을 사용했다. 이 확장은 holonomic SH5용이며 Ackermann 차량에는 사용하지 않는다.

최대 속도 0.35 m/s, 최대 yaw 속도 0.7 rad/s, yaw 가속도 1.2 rad/s²,
Nav2 위치 0.025 m / yaw 0.02 rad(약 1.15°), stateful=false가 적용된다.
Canvas 검증은 위치 0.03 m / yaw 0.02 rad이다.
회전 시간을 더 조정할 때는 우선 위 critic과 제어 주기를 측정한다.
`wz_max`, `az_max`는 controller뿐 아니라 velocity_smoother의 회전 상한/가속도와
함께 검토해야 한다. 이번 변경은 속도 상한 증가 없이 수행했다.

### src/exact_goal_smac_planner.cpp

`SmacPlannerHybrid::createPlan()` 뒤에 정확한 목표 연결을 수행하는 pluginlib planner.
기존 BT의 planner ID `SmacPlannerHybrid`를 그대로 사용하므로 BT 변경은 필요 없다.

### include/ffw_navigation/exact_goal_connection.hpp

- 최종 위치 차이가 costmap 한 셀 대각선 이내, 각도 차이가 반 개 heading bin 이내일 때만 연결.
- 연결 전체를 footprint 외곽점 이동량 기준 최대 반 셀 간격으로 샘플링.
- padded footprint와 중심 셀을 검사하며 lethal/unknown/맵 밖 또는 중심의 inscribed 충돌을 거부.
- 중간 회전이 막히면 `GoalOccupied`로 실패하고 임의의 대체 자세를 성공으로 반환하지 않음.
- 마지막 pose에 사용자 목표 좌표와 quaternion을 그대로 넣음.
- 취소 요청을 처리하고 실패한 연결은 원래 path에 일부만 추가하지 않음.

`planner_plugins.xml`, `CMakeLists.txt`, `package.xml`에 플러그인 등록/빌드 의존성을 추가했다.

## 검증과 배포 상태

- `colcon build --packages-select ffw_navigation --symlink-install --cmake-args -DBUILD_TESTING=ON`: 성공.
- `colcon test --packages-select ffw_navigation`: 7개 gtest 통과.
  실제 waypoint yaw 보존, ±pi 경계, 목표 충돌, 회전 중간 충돌, 과도한 endpoint 차이,
  unknown/맵 밖, 취소 처리를 검증했다.
- 실제 runtime 종료 후 독립 ROS_DOMAIN_ID=91에서 `bgf_0923_3` static map과 동일한
  footprint/inflation을 사용하는 planner를 띄워 새 플러그인 로드/activate 성공을 확인했다.
  실제 장애물 토픽은 연결하지 않았으며 물리 로봇의 domain 30에는 이동 명령을 보내지 않았다.
- Waypoint 1→2, 2→1, (-0.34,0.53,-120°)→2 보정의 3개 경로 모두
  반환된 목표 위치 오차 **0 m**, 각도 오차 **0°**. 이는 **경로 끝의 오차**이며 실제 도착 오차가 아니다.
- 사용자 runtime은 작업 중 종료됐다. 실제 navigation service를 다시 시작하지 않았다.
- `launch/navigation.launch.py` 기본값은 `navigation_mppi_1109.yaml`이며 installed config는
  source에 symlink된다. 다음 Mission Canvas navigation runtime 시작에서 새 플러그인/설정을 읽는다.
- 남은 실차 확인: 같은 경로 Run에서 waypoint별 도착 오차, yaw 정렬 소요 시간,
  `Control loop missed its desired rate` 빈도. 단축 시간을 아직 측정하지 않았다.

## 근거

- Nav2 Jazzy Hybrid planner: https://github.com/ros-navigation/navigation2/blob/jazzy/nav2_smac_planner/src/smac_planner_hybrid.cpp
- Nav2 Jazzy MPPI 설정: https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/controller_plugins/mppi_controller/configuring_mppic/
- 이전 정지/라이다 조치: `1109_navigation_stop_and_lidar_noise_20260928.md`
