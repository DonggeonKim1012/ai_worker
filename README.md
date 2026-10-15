# ROBOTIS AI Worker ROS 2 Packages

This repository contains the official ROS 2 packages for the ROBOTIS AI Worker platform. These packages provide the necessary interfaces and tools to control the robot, integrate with its sensors, and develop physical AI applications, including those utilizing frameworks like LeRobot. For detailed usage instructions, please refer to the documentation below.
  - [Documentation for AI Worker](https://ai.robotis.com/)

To learn more about the Physical AI Tools, visit:
  - [Physical AI Tools](https://github.com/ROBOTIS-GIT/physical_ai_tools)

To explore our open-source platforms in a simulation environment, visit:
  - [Simulation Models](https://github.com/ROBOTIS-GIT/robotis_mujoco_menagerie)

For usage instructions and demonstrations of the AI Worker, check out:
  - [Tutorial Videos](https://www.youtube.com/@ROBOTISOpenSourceTeam)

To access datasets and pre-trained models for our open-source platforms, see:
  - [AI Models & Datasets](https://huggingface.co/ROBOTIS)

To use the Docker image for running ROS packages and Physical AI tools with the AI Worker, visit:
  - [Docker Images](https://hub.docker.com/r/robotis/ros/tags)

## LG2 mini leader + SH5: 독립 클린 빌드와 배포

이 절은 `DonggeonKim1012/ai_worker`의 `lg2-recording-controls-20261014`와
`DonggeonKim1012/cyclo_intelligence`의 `dg-branch`를 **한 쌍으로** 배포하는 절차다.
2026-10-15 Jetson Orin/ARM64, L4T 36.4, ROS 2 Jazzy에서 검증한 환경을 기준으로 한다.
x86 PC나 다른 JetPack 버전에 그대로 적용하는 절차가 아니다.
일반 사용자는 기존 실행 경로를 유지한다. 아래 전용 파일은 `docker/lg2-sh5/`에만 있다.

### 클린 빌드의 범위와 upstream clone 주의

- `./container.sh start`는 배포 이미지를 pull/실행할 수 있으므로 현재 fork 소스의 빌드 증거가 아니다.
- 기존 `docker/Dockerfile.arm64`는 upstream `ROBOTIS-GIT/ai_worker`의 `jazzy`를 clone한다.
  여기에 `--no-cache`만 붙여도 내 수정 코드가 빌드되는 것은 아니다. 일반 Dockerfile은 변경하지 않았다.
- 아래 전용 Dockerfile은 고정된 ROS 베이스와 SDK 위에 **직접 checkout한 fork 소스**를 COPY한다.
  AI ROS 패키지 전체와 Cyclo ROS 패키지를 각각 비어 있는 `build/install/log`에서 빌드한다.
  이전 AI 이미지, 호스트 ROS overlay, 기존 colcon 결과를 가져오지 않는다.
- upstream 의존성은 [sources.repos](docker/lg2-sh5/sources.repos)의 커밋으로 고정한다.
  `robotis_interfaces`는 두 워크스페이스에서 같은 커밋을 사용한다.
- apt/rosdep 및 일부 Python 전이 의존성은 완전한 lockfile이 아니다. 이는 소스와 배포 구성을
  재현하는 절차이며 bit-for-bit 재현을 보장하지 않는다. 정확히 같은 바이너리는 이미지 아카이브도 보관한다.

### 1. 새 디렉터리와 두 저장소 준비

호스트에 Docker, NVIDIA Container Runtime, Git, `vcs`(python3-vcstool)가 필요하다.
아래는 Bash 명령이다. **두 변경 커밋이 원격에 push된 후** 각 40자리 SHA를 입력한다.
브랜치 이름만 고정하면 이후 push에 따라 결과가 달라진다. 아직 push 전이라면 원격 URL 대신
해당 커밋이 있는 로컬 저장소 경로로 clone할 수 있다.

```bash
export AI_REF='여기에_AI_커밋_SHA_40자리'
export CYCLO_REF='여기에_Cyclo_커밋_SHA_40자리'
[[ "$AI_REF" =~ ^[0-9a-f]{40}$ && "$CYCLO_REF" =~ ^[0-9a-f]{40}$ ]] || exit 1
export DEPLOY_ROOT="$(mktemp -d /home/robotis/lg2-sh5-XXXXXX)"
mkdir -p "$DEPLOY_ROOT/ai_ws/src" "$DEPLOY_ROOT/cyclo_ws/src" \
  "$DEPLOY_ROOT/hardware" "$DEPLOY_ROOT/real-data/ai" \
  "$DEPLOY_ROOT/real-data/cyclo/.web-relay" "$DEPLOY_ROOT/evidence"

git clone --branch lg2-recording-controls-20261014 \
  https://github.com/DonggeonKim1012/ai_worker.git "$DEPLOY_ROOT/ai_ws/src/ai_worker"
git -C "$DEPLOY_ROOT/ai_ws/src/ai_worker" checkout --detach "$AI_REF"
git clone --branch dg-branch https://github.com/DonggeonKim1012/cyclo_intelligence.git \
  "$DEPLOY_ROOT/cyclo_ws/src/cyclo_intelligence"
git -C "$DEPLOY_ROOT/cyclo_ws/src/cyclo_intelligence" checkout --detach "$CYCLO_REF"

vcs import "$DEPLOY_ROOT/ai_ws/src" \
  < "$DEPLOY_ROOT/ai_ws/src/ai_worker/docker/lg2-sh5/sources.repos"
git -C "$DEPLOY_ROOT/ai_ws/src/zed-ros2-wrapper" submodule update --init --recursive
git clone https://github.com/ROBOTIS-GIT/robotis_interfaces.git \
  "$DEPLOY_ROOT/cyclo_ws/src/robotis_interfaces"
git -C "$DEPLOY_ROOT/cyclo_ws/src/robotis_interfaces" checkout --detach \
  7a5670cb3fb3f42b479a1fbf17c1e767b43db067
vcs export --exact "$DEPLOY_ROOT/ai_ws/src" > "$DEPLOY_ROOT/evidence/ai-sources.repos"
vcs export --exact "$DEPLOY_ROOT/cyclo_ws/src" > "$DEPLOY_ROOT/evidence/cyclo-sources.repos"
```

다른 호스트에서는 `/home/robotis`를 자신의 작업 디렉터리로 바꾼다.
이후 터미널에서도 `DEPLOY_ROOT`를 실제 생성된 경로로 설정한다.
기존 폴더 삭제나 Docker 전체 prune은 필요 없다. 각 명령 실패 시 다음 단계로 진행하지 않는다.

### 2. 실제 USB와 카메라 설정

아래는 검증에 사용한 **이 로봇의 값**이다. 다른 장비에 일괄 적용하지 않는다.
`ttyUSB4`, `ttyACM0` 같은 번호는 재연결마다 바뀔 수 있으므로 by-id를 해석해 매핑한다.
미니 리더 오른쪽은 오른쪽 USB만 분리하여 긴 시리얼 보드임을 확인했다.

| 역할 | 호스트 `/dev/serial/by-id/` 아래 ID | 컨테이너 경로 |
| --- | --- | --- |
| SH5 follower | `usb-FTDI_USB__-__Serial_Converter_FOLLOWER-if00-port0` | `/dev/follower` |
| 미니 리더 왼쪽 | `usb-ROBOTIS_OpenRB-150_00000002-if00` | `/dev/left_leader` |
| 미니 리더 오른쪽 | `usb-ROBOTIS_OpenRB-150_20FBBD68503059384C2E3120FF08322D-if00` | `/dev/right_leader` |
| ORIN 보드 포트 0 | `usb-ROBOTIS_ORIN_BD_V0.2-if00-port0` | `/dev/ttyUSB0` |
| ORIN 보드 포트 1 | `usb-ROBOTIS_ORIN_BD_V0.2-if01-port0` | `/dev/ttyUSB1` |

| 카메라 | 시리얼 | 설정 |
| --- | --- | --- |
| 왼쪽 D405 | `335122271364` | `camera1_serial` |
| 오른쪽 D405 | `335122273200` | `camera2_serial` |
| 머리 ZED-M | `13018209` | `SN13018209.conf` 보정 파일 |

```bash
ls -l /dev/serial/by-id/
cp "$DEPLOY_ROOT/ai_ws/src/ai_worker/docker/lg2-sh5/rs_serial.example.yaml" \
  "$DEPLOY_ROOT/hardware/rs_serial.yaml"
```

장비가 다르면 먼저 `hardware/rs_serial.yaml`과 아래 USB ID, `ZED_SERIAL`을 수정한다.
RealSense 설정은 `camera1_serial: "'335122271364'"`처럼 **안쪽 작은따옴표도 유지**한다.
`auto_assign_cameras:=false`로 실행하여 좌우 자동 배정을 막는다.
ZED는 한 대 연결된 구성을 전제로 하며, `ZED_SERIAL` 빌드 인자는 보정 파일을 받는 값이지
여러 ZED 중 장치를 선택하는 launch 인자가 아니다.

전용 Dockerfile은 RealSense SDK 2.56.4 소스 커밋과 ZED SDK 5.0.7 설치 파일 SHA256을 고정한다.
ZED 다운로드 URL의 내용이 바뀌면 checksum 검증에서 실패한다. 검증을 제거하지 말고 SDK 호환성을 확인한다.
보정 파일은 `https://calib.stereolabs.com/?SN=13018209`에서 받아
`/usr/local/zed/settings/SN13018209.conf`에 넣는다. 당시 파일 SHA256은
`f74f62c3d7a213a0986c6c701fcf48c702c03e55882f8a56251ed49383e11f91`이었다.
카메라 교체 시 다른 시리얼의 보정을 재사용하지 않는다.

### 3. AI 이미지 전체 빌드와 컨테이너 생성

```bash
export AI_IMAGE="local/ai-worker-lg2-sh5:$(git -C "$DEPLOY_ROOT/ai_ws/src/ai_worker" rev-parse --short=12 HEAD)"
docker build --no-cache --progress=plain --build-arg ZED_SERIAL=13018209 \
  -f "$DEPLOY_ROOT/ai_ws/src/ai_worker/docker/lg2-sh5/Dockerfile" \
  -t "$AI_IMAGE" "$DEPLOY_ROOT"
```

빌드가 성공한 뒤 Cyclo README의 **2. 의존성 이미지·ROS·UI 빌드**도 완료한다.
기존 로봇 제어 프로세스가 같은 USB 장치를 점유하지 않는지 운영자가 확인한 뒤 아래를 실행한다.
컨테이너를 만드는 것만으로는 로봇 노드가 실행되지 않는다. `--privileged`와 host network는 사용하지 않는다.

```bash
device_args=()
map_device() {
  local actual
  actual=$(readlink -e "/dev/serial/by-id/$1") || return 1
  test -c "$actual" || return 1
  device_args+=(--device "$actual:$2")
}
map_device usb-FTDI_USB__-__Serial_Converter_FOLLOWER-if00-port0 /dev/follower || exit 1
map_device usb-ROBOTIS_OpenRB-150_00000002-if00 /dev/left_leader || exit 1
map_device usb-ROBOTIS_OpenRB-150_20FBBD68503059384C2E3120FF08322D-if00 /dev/right_leader || exit 1
map_device usb-ROBOTIS_ORIN_BD_V0.2-if00-port0 /dev/ttyUSB0 || exit 1
map_device usb-ROBOTIS_ORIN_BD_V0.2-if01-port0 /dev/ttyUSB1 || exit 1
for device in /dev/video*; do
  test ! -c "$device" || device_args+=(--device "$device:$device")
done
docker run -d --name ai_worker_lg2_sh5 --network none --runtime nvidia --shm-size 1g \
  "${device_args[@]}" --device /dev/bus/usb:/dev/bus/usb \
  -v /run/udev:/run/udev:ro -v "$DEPLOY_ROOT/real-data/ai:/workspace" "$AI_IMAGE"
```

이 이미지의 소스·빌드·설치는 `/full/ros_ws` **이미지 내부**에 있다. 호스트 ROS 코드는 마운트하지 않는다.
`/workspace`만 기록·프리셋·로그 보존용 RW bind mount다. host udev 규칙을 새로 쓰지 않아도
by-id → `--device` 매핑으로 컨테이너 이름을 고정할 수 있다.
USB 재연결로 장치 노드가 바뀌면 실행 중인 제어를 안전하게 정지한 뒤 두 ROS 컨테이너를 재생성한다.
AI 컨테이너는 공유 네트워크의 기준이므로 Cyclo도 함께 재생성해야 한다.

### 4. 실행: router → Cyclo → follower → leader

Cyclo README의 **3. 컨테이너·브라우저 구성**까지 완료한다. AI/Cyclo는 같은 격리 네트워크에서
`ROS_DOMAIN_ID=174`, `rmw_zenoh_cpp`, `tcp/127.0.0.1:7447`을 사용한다.
멀티캐스트와 공유 메모리 discovery를 끈다. 기존 ROS graph와 합치지 않는다.
명령은 별도 터미널에서 실행한다. SSH 종료로 프로세스가 끊어지지 않게 하려면 tmux 안에서 실행한다.

```bash
# 터미널 1: ROS router (로봇을 움직이지 않음)
docker exec -it ai_worker_lg2_sh5 env -i HOME=/workspace LANG=C.UTF-8 \
  PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
  bash --noprofile --norc /usr/local/bin/lg2-sh5-ros router

# 터미널 2: Cyclo
docker exec -it cyclo_lg2_sh5 env -i HOME=/workspace LANG=C.UTF-8 \
  PATH=/opt/validation-venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
  bash --noprofile --norc /validation/cyclo_ws/src/cyclo_intelligence/docker/lg2-sh5/cyclo-command.sh

# 터미널 3: SH5 follower — 이 명령은 실제 init pose 이동을 수행함!
docker exec -it ai_worker_lg2_sh5 env -i HOME=/workspace LANG=C.UTF-8 \
  PATH=/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
  bash --noprofile --norc /usr/local/bin/lg2-sh5-ros follower

# 터미널 4: 초기화 완료 후 미니 리더. 양쪽 트리거를 놓고 시작.
docker exec -it ai_worker_lg2_sh5 env -i HOME=/workspace LANG=C.UTF-8 \
  PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
  bash --noprofile --norc /usr/local/bin/lg2-sh5-ros leader
```

작업 공간을 비우고 비상정지를 준비한다. 기존 controller/hand bridge와 중복 실행하지 않는다.
helper의 flock은 **이 helper의 같은 역할 중복 실행만** 막으며 다른 컨테이너의 제어기를 막지는 못한다.
NVIDIA 라이브러리를 CUDA 경로보다 먼저 두어 Jetson 카메라의 JPEG 라이브러리 충돌을 피한다.
helper가 실행하는 핵심 명령은 다음과 같다.

```bash
ros2 launch ffw_bringup ffw_sh5_follower_ai.launch.py \
  init_position:=true launch_cameras:=true head_camera_type:=zed \
  auto_assign_cameras:=false launch_lidar:=false
ros2 launch ffw_bringup ffw_lg2_mini_leader_recording.launch.py launch_final_pose:=false
```

### 5. 사용자 기능의 적용 범위와 확인

- 기본 `ffw_lg2_mini_leader_ai.launch.py`에서는 `enable_sh5_recording_controls:=false`다.
  `ffw_lg2_mini_leader_recording.launch.py`만 미니 리더 + `follower_type:=ffw_sh5_rev1`을 명시해 활성화한다.
  잘못된 follower/description 조합은 거부한다. 종료 자세 노드는 별도 opt-in이며 위 명령에서는 꺼져 있다.
- 해당 모드에서 팔 추종은 좌우 각각 7축으로 전달한다. SH5에 없는 `gripper_l/r` 상태를 기다리지 않는다.
  손은 `/leader/joint_states`의 트리거를 별도 bridge가 읽어 SH5 finger 프리셋으로 보낸다.
- 이 모드의 teleop 시작/정지는 **해당 쪽 조이스틱 짧은 클릭**이다. 트리거만 당기는 것은 시작 명령이 아니다.
  양쪽 동시 클릭은 별도 모드 전환이므로 처음 검증할 때 한쪽씩 누른다.
  리더와 follower 자세를 맞춘 뒤 추종을 켠다. 3초 slow-start가 있어도 큰 자세 차이는 위험하다.
- 긴 오른쪽 클릭은 녹화 시작/저장, 긴 왼쪽 클릭은 취소다.
  Cyclo에서 SH5를 선택하고 녹화 세션을 준비한 상태에서 확인한다.
- status의 `control_profile=lg2_mini_sh5_recording`이 Cyclo에 전달되어야 Hand Preset Studio가 표시된다.
  일반 로봇/기본 launch에는 새 녹화 매핑을 강제하지 않는다. 다른 로봇의 모든 기능을 실기기로 검증했다는 뜻은 아니다.

다음은 로봇을 움직이지 않는 확인이다. helper의 `shell`에 들어가 실행한다.

```bash
ros2 pkg prefix ffw_bringup
ros2 topic echo /leader/hand_preset/status std_msgs/msg/String --once
ros2 control list_controllers -c /controller_manager
ros2 control list_controllers -c /leader/controller_manager
```

prefix는 `/full/ros_ws/install/ffw_bringup`이어야 한다. 두 controller 목록이 active이고
status에 프로필·프리셋 목록이 보이는지 확인한다. UI에서 카메라 좌우와 SH5 모델, 프리셋 목록/편집/저장,
짧은 클릭 추종 및 긴 클릭 녹화를 순서대로 확인한다. subscriber만 존재하는 것을 실제 추종 성공으로 간주하지 않는다.
`Aborted <<< ...`는 후속 패키지 중단일 수 있으므로 첫 `Failed <<< ...`의 실제 stderr부터 확인한다.

### 6. 당시 실행 환경과 이번 재현 절차의 차이

| 당시 대상 (2026-10-15) | 이미지 / 실행 코드 |
| --- | --- |
| `ai_worker_full_real_20261015` | 생성 이미지 `local/ai-worker-full:82a1b35-presetfix-20261015`; `/full/ros_ws/install` 이미지 내부 |
| 후속 AI 빌드 | `local/ai-worker-full:82a1b35-teleopfix-20261015`; 기존 컨테이너에는 수정 artifact를 복사해 적용했으므로 생성 이미지 태그와 live 코드가 달랐음 |
| `cyclo_clean_real_20261015` | `local/interop-hardware-runtime:20261015`; 호스트 `cyclo_ws` → `/validation/cyclo_ws` 읽기 전용 bind mount |
| `ai_worker_clean_real_20261015` | 이전 실험의 Zenoh router/network 기준 컨테이너; 위 full AI 컨테이너와 혼동하지 않음 |

당시 AI의 `/validation-full`은 참고 자료 mount, `/workspace`는 데이터 mount였다.
당시 Cyclo image ID는 `sha256:6405094691176155f772cc9233f35312f69728d8ec83f876a6250996df2466d1`이다.
새 절차는 컨테이너 안에 사후 복사하지 않고 두 커밋을 함께 빌드하며, AI 컨테이너 자체에 router를 둔다.
옛 태그 이름에 새 커밋이 포함되어 있다고 가정하지 않는다.

실제 카메라·추종 성공 확인은 scope 분리 전 환경에서 수행했다. 이후 기본/opt-in 분기, Python 계약,
C++/ROS 빌드, Cyclo UI 빌드를 별도로 확인했다. 이 README에 묶은 새 전체 Docker 빌드 절차 자체와
scope 분리 후 실기기 동작은 다시 검증해야 한다. README/커밋 작업 중 운영 컨테이너는 교체하지 않았다.

배포 후 두 Git SHA, `vcs export --exact`, 빌드 로그, `docker image inspect --format '{{.Id}}' IMAGE`,
SDK/보정 checksum 및 컨테이너 Mounts/Devices를 함께 보관한다.
`docker image save -o ai-worker-image.tar "$AI_IMAGE"`로 바이너리도 보관할 수 있다.
설정·데이터와 Cyclo 이미지/워크스페이스도 별도로 보관해야 하며 이미지 저장만으로 bind mount는 보존되지 않는다.
자격 증명이 섞일 수 있으므로 전체 환경변수나 Docker inspect 전체 내용을 공개 저장소에 올리지 않는다.
