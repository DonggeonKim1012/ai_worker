# 1109 조향 정지 및 장거리 전방 주행 변경

## 1. 재현한 정지 원인

2026-09-28 사용자 재현 시 ROS domain 30에서 `/cmd_vel_nav`, `/cmd_vel_smoothed`,
`/cmd_vel`, `/joint_commanders`, `/joint_states`, `/odom`을 함께 기록했다.

- 이전 08:44 Run은 08:44:46 시작, 08:45:21 `Failed to make progress`, 08:45:24 종료.
  당시에는 바퀴 상태 기록이 없어 이 로그만으로 원인을 확정하지 않았다.
- 사용자 재현 약 79초 구간에서 Nav2의 작은 X/Y/yaw 명령이 `/cmd_vel`까지 전달됐다.
  예: vx=0.0072, vy=-0.0055 m/s, wz=0.032 rad/s.
- 정지 상태 조향 허용치 runtime은 **0.01 rad = 0.57°**였다.
- 0.15초 이내의 joint state와 command를 대응시킨 303개 샘플에서
  왼쪽 구동 명령 0 비율 86.5%, 오른쪽 62.0%, 후방 28.7%.
  조향 오차 중앙값은 각각 3.66°, 0.93°, 0.26°.
- 베이스는 작은 조향 오차에도 구동을 차단하고, MPPI는 바뀌는 조향 목표를 계속 생성했다.
  실제 바퀴 구동이 충분히 따라오지 못해 odometry도 작게 유지되는 피드백 문제가 확인됐다.
- 설치된 베이스는 2026-05-15 바이너리이며 현재 저장소 소스와 동작이 일부 다르다.
  현재 소스의 모든 바퀴 동시 gating 로직을 설치 바이너리에도 동일하다고 가정하지 않았다.

### 수정 및 실제 적용

`ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml`

| 파라미터 | 이전 | 새 값 |
|---|---:|---:|
| steering_alignment_start_angle_error_threshold | 0.01 rad | 0.10 rad (5.7°) |
| steering_alignment_angle_error_threshold | 1.0 rad | 0.35 rad (20.1°) |
| steering_alignment_start_speed_error_threshold | 0.1 rad/s | 0.1 rad/s |

정지 시 출발 허용치를 실측 오차 수준에 맞추고, 움직이는 바퀴의 과도한 misalignment는
기존보다 빨리 차단하도록 했다. Nav2 goal yaw tolerance와는 다른 값이다.
진단 목표를 취소한 뒤 navigation runtime이 종료된 상태에서 베이스 controller를
inactive → unconfigured → parameter set → configure → active로 재설정했다.
실제 runtime `steering_alignment_start_angle_error_threshold=0.1`을 확인했다.

물리 재주행 후 지속적인 정지 해소 여부는 별도로 확인해야 한다. 이 기록의 배포 시점까지
수정 후 사용자 Run은 수집되지 않았다.

## 2. 먼 구간 전방 주행

기존 CurveController도 `motion_model: Omni`여서 횡속도를 사용할 수 있었다.
이제 다음 세 단계로 동작한다.

1. 전체 계획 경로 길이가 2 m보다 길면 CurveController 선택.
2. RotationShim이 경로 진행 방향으로 몸체를 먼저 정렬하고, MPPI DiffDrive 모델로 전진.
3. 남은 경로 길이가 0.6 m 이내이면 OmniController로 한 번 전환하여 위치와 최종 yaw를 함께 정렬.

2 m 이하의 짧은 경로는 기존처럼 처음부터 OmniController를 사용한다.
기준은 waypoint 직선거리가 아니라 planner가 만든 **경로 길이**다.

### navigation_mppi_1109.yaml

- CurveController plugin: `nav2_rotation_shim_controller::RotationShimController`.
- primary_controller: `nav2_mppi_controller::MPPIController`.
- Curve motion_model: `Omni` → `DiffDrive`; vx_min=0, vy_max=0, vy_std=0.
- RotationShim: angular_dist_threshold=0.5 rad, angular_disengage_threshold=0.2 rad,
  forward_sampling_distance=0.5 m, angular velocity=0.5 rad/s, max acceleration=1.2 rad/s².
- PathAlignCritic.use_path_orientations=false: REEDS_SHEPP의 후진용 자세보다 경로 위치를 추종.
- Curve GoalAngleCritic.enabled=false: 장거리에는 진행 방향을 바라보고, 최종 yaw는 Omni가 담당.
- Omni GoalAngleCritic은 weight=8, threshold=0.6 m로 접근 중 정렬 유지.
- 베이스는 계속 swerve이며 AMCL도 OmniMotionModel이다. DiffDrive는 장거리 명령에서
  횡이동을 배제하는 MPPI 예측/명령 모델로만 사용한다.

### config/bt/nav_modes_1109.xml / src/select_navigation_controller.cpp

새 `SelectNavigationController` BT 노드는 현재 TF 위치와 남은 경로 길이를 사용해
controller ID를 갱신한다. Nav2 FollowPath는 controller_id 변경을 preemption으로 수용한다.
전환 후에는 같은 경로에서 Omni를 유지해 경계에서 왕복 전환하지 않는다.
TF를 얻을 수 없으면 선택을 실패시키며, controller 실패는 기존 RecoveryNode로 전달된다.

거리 계산/전환 상태: `include/ffw_navigation/approach_mode.hpp`.
플러그인 등록/의존성은 CMakeLists.txt 및 package.xml에 포함했다.

## 3. 검증

- ffw_navigation 빌드 성공.
- 기존 정확한 목표 연결 7개 + 접근 모드 4개 = **11개 gtest 통과**.
- ROS_DOMAIN_ID=91 / FastDDS / 로컬 전용의 분리된 환경에서 controller/planner/BT/behavior 활성화 성공.
- 빈 맵과 운동학 모의 로봇으로 3 m 목표 이동 실행. 실제 domain 30 하드웨어에는 목표를 보내지 않음.
- 시작 yaw 90°, 이동 방향 +X, 최종 yaw 90°.
- CurveController → OmniController 한 번 전환, 약 16.86초 후 성공.
- 장거리 254개 명령: 횡속도 최대 절댓값 **0.0 m/s**, 최소 vx **0.0 m/s**.
- Omni 접근 84개 명령: 횡속도 사용을 확인 (최대 약 0.0758 m/s).
- 최종 위치 [2.98968, 0.01190], 목표 [3,0] 대비 약 **1.58 cm**.
- 최종 yaw 88.938°, 목표 90° 대비 **1.062°**.
- 모의 결과는 하드웨어의 조향 마찰/통신/센서 오차를 포함하지 않으며 실차 개선 시간으로 해석하지 않는다.

## 4. 이전 버전 보관

- GitHub private: https://github.com/YWhero/BGF_navigation_0928
- 별도 작업 트리: `/home/robotis/BGF_navigation_0928`.
- ExactGoalSmacPlanner 및 직전 MPPI yaw/iteration 변경 **이전**의 YAML과 IfThenElse BT.
- 이번 조향 허용오차 및 전방 주행 변경도 포함하지 않음.
- 당시 Docker base digest를 고정하고 설치 swerve 바이너리 SHA-256이 1109와 같음을 확인.
- 전체 명시 파라미터 512행 문서: 저장소 `docs/PARAMETERS.md`.
- 다른 물리 로봇에서는 모터/센서 연결, 조향 영점, 지도 및 localization을 맞춰야 한다.

## 소스 근거

- https://github.com/ros-navigation/navigation2/blob/jazzy/nav2_behavior_tree/plugins/action/follow_path_action.cpp
- https://github.com/ros-navigation/navigation2/blob/jazzy/nav2_mppi_controller/include/nav2_mppi_controller/motion_models.hpp
- https://github.com/ros-navigation/navigation2/blob/jazzy/nav2_rotation_shim_controller/src/nav2_rotation_shim_controller.cpp
