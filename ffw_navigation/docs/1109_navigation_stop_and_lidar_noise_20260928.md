# 1109 navigation 정지 및 후방 라이다 허위 점 수정 (2026-09-28)

## 실측으로 확인한 정지 원인

사용자가 Mission Canvas에서 재실행하는 동안 ROS domain 30에서 `/cmd_vel_nav`, `/cmd_vel_smoothed`, `/cmd_vel`, `/joint_commanders`, `/joint_states`, `/odom`, 구동기 marker를 동시에 수집했다.

- MPPI 출력 약 X=-0.008, Y=0.023 m/s가 스무더와 collision monitor를 지나 `/cmd_vel`까지 그대로 전달됐다.
- 베이스의 실제 `linear_vel_deadband`와 `angular_vel_deadband`는 모두 0.1이었다. 베이스 내부 marker와 3개 구동 바퀴 명령은 모두 0이었다.
- MPPI의 출발 가속도 한도는 0.5 m/s², model_dt는 0.05 s이므로 정지 상태의 첫 속도는 최대 약 0.025 m/s다. 이 값이 데드밴드보다 작아 바퀴가 움직이지 않고, odometry가 계속 0이므로 MPPI도 출발 속도에서 벗어나지 못했다.
- 현재 소스의 기본값은 0.001이지만 설치된 구동 라이브러리는 2026-05-15 빌드였고 런타임 기본값은 0.1이었다. 소스만 보고 실제 값이 작다고 판단하면 안 된다.

`ffw_bringup/config/ffw_sh5_rev1_follower/ffw_sh5_follower_ai_hardware_controller.yaml`에 두 데드밴드를 0.005로 명시했다. 진단 목표를 취소하고 베이스 컨트롤러만 deactivate → cleanup → parameter set → configure → activate하여 실제 제어 루프에 적용했다.

## 후방 점의 출처와 수정

30초 원본 기록에서 왼쪽 센서의 132~133°에 0.205~0.208 m 반사가, 오른쪽 -134° 부근에 0.455~0.469 m 반사가 있었다. 차체를 향하는 센서 시야 끝부분이며, 병합 스캔에서는 후방 약 159° / 0.282 m에 1~4개 점이 간헐적으로 남았다. 차체 자기반사로 해석된다.

SH5 런치에서 두 라이다의 장치 스캔 범위를 45~315°에서 50~310°로 제한했다. ROS 센서 좌표의 유효 구간은 약 -130~130°다. 반대 방향으로 장착된 두 센서의 겹치는 시야를 사용하며, 전체 방향이나 특정 거리 이내의 장애물을 일괄 삭제하는 필터는 넣지 않았다.

병합기의 `enable_average_filter`도 false로 설정했다. 기존 구현은 거리 경계의 이웃 값을 평균하여 실제로 없는 중간 거리 점을 만들 수 있고, `i <= ranges.size()` 루프가 배열 범위를 초과한다. 해당 경로를 비활성화했다. shadow filter는 계속 사용한다.

변경 전 병합 스캔 112개 중 110개에서 후방 근거리 점이 관측됐다. 변경 후 25초의 병합 스캔 93개에서는 0개였으며, 원본 좌우 스캔 93/94개에서도 해당 근거리 점은 0개였다. 실제 센서 API에서 새 범위를 확인했고, 재시작 시에도 SH5 런치가 이 값을 적용한다.

## 추가 파라미터 및 BT 점검

| 항목 | 현재 설정 / 판단 |
| --- | --- |
| 베이스 선속도·각속도 데드밴드 | 0.1 → 0.005; 출발 및 정밀 보정 명령 전달 |
| MPPI 속도 상한 | X/Y 0.35 m/s, yaw 0.7 rad/s; 정지 원인 아님 |
| MPPI 가속도 한도 | X/Y 0.5 m/s², yaw 1.2 rad/s²; 베이스 데드밴드와의 불일치를 수정 |
| local inflation | 0.48 m / scaling 10.0; 이전 접근용 조정값 유지 |
| footprint padding | 0.02 m; 실제 외곽선 유지 |
| 목표 허용오차 | XY 0.025 m / yaw 0.02 rad; 작은 속도 명령이 전달되어야 달성 가능 |
| progress checker | 0.02 m 또는 0.02 rad / 20초; timeout을 늘려 증상을 숨기지 않음 |
| no-return clearing | local scan `inf_is_valid: true`; +inf 광선으로 사라진 점의 이전 비용을 clearing |
| BT 컨트롤러 선택 | `ReactiveFallback` 대신 `IfThenElse`; 길이로 선택한 컨트롤러 실패를 RecoveryNode로 전달 |

새 BT는 `config/bt/nav_modes_1109.xml`이며 1109 프리셋의 두 navigator 경로에 지정했다. 기존 구조는 짧은 경로의 Omni 실패 후 Curve를 시작했다가 다음 tick에 Omni로 돌아가 실패 복구 전에 재시도를 반복할 수 있었다.

Nav2를 재시작하고 저장한 AMCL 위치/공분산을 복원했다. 새 BT 파싱 및 navigator/controller active 상태, 데드밴드 0.005, inf_is_valid true를 런타임에서 확인했다.

## 해석 정정과 검증 범위

코스트맵 값 253은 `consider_footprint=true`인 Jazzy MPPI에서 실제 충돌 확정값이 아니다. 254 장애물과 외곽선 교차를 별도로 검사한다. 앞선 253 해석과 inflation만으로 정지 원인을 추정한 설명을 정정한다. 이번 정지 원인은 속도 체인과 바퀴 명령을 동시에 계측하여 확인했다.

수정 후 추가 Run은 아직 관측되지 않았다. 런타임 적용과 후방 허위 점 제거는 검증했으며, 실제 이동 및 최종 목표 도착 검증은 사용자의 재실행 대기 상태다.


## 후속 확인

사용자가 수정 후 실제 주행과 waypoint yaw 정렬이 잘 동작한다고 확인했다.
이후 왕복 종료의 각도 검증 불일치와 정렬 시간 개선은
`1109_exact_goal_and_yaw_tuning_20260928.md`에 원인, 변경 및 검증 결과를 기록했다.
