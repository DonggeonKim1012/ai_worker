# Context: a fresh deployment directory containing ai_ws/src and hardware/.
# The user's checked-out ai_worker is COPIED, never replaced with upstream jazzy.
FROM robotis/ros@sha256:8aad9a98d27d881c4aa36a0cd753781eaaa33c0b573c709e31f498af66d9b250
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_INDEX_URL=https://pypi.org/simple
ENV PIP_EXTRA_INDEX_URL=""
ENV LD_LIBRARY_PATH=/usr/lib/aarch64-linux-gnu/nvidia:/usr/local/cuda/lib64:${LD_LIBRARY_PATH}
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential cmake git curl ca-certificates libssl-dev libusb-1.0-0-dev \
    pkg-config libgtk-3-dev libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev \
    python3-dev python3-pip python3-venv python3-colcon-common-extensions \
    python3-rosdep python3-vcstool lsb-release zstd sudo apt-transport-https \
    udev ffmpeg xz-utils ros-jazzy-rmw-zenoh-cpp ros-jazzy-map-msgs
RUN git clone https://github.com/IntelRealSense/librealsense.git /sdk-src/librealsense && \
    git -C /sdk-src/librealsense checkout --detach 1e34346894be975e8e594fab22f8b31a89a710bb && \
    git -C /sdk-src/librealsense submodule update --init --recursive && \
    cmake -S /sdk-src/librealsense -B /sdk-build/librealsense \
      -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local \
      -DBUILD_GRAPHICAL_EXAMPLES=OFF -DBUILD_EXAMPLES=OFF \
      -DBUILD_PYTHON_BINDINGS=ON -DFORCE_RSUSB_BACKEND=ON -DBUILD_WITH_CUDA=ON \
      -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPython_EXECUTABLE=/usr/bin/python3 \
      -DCMAKE_CUDA_ARCHITECTURES=87 && \
    cmake --build /sdk-build/librealsense --parallel 2 && \
    cmake --install /sdk-build/librealsense && ldconfig
# The vendor URL can change. Fail instead of silently installing a newer SDK.
RUN curl -fL --retry 3 https://download.stereolabs.com/zedsdk/5.0/l4t36.4/jetsons \
      -o /tmp/ZED_SDK_Linux.run && \
    echo '7558cf855e654392ff593db287b8aff02516491643973300c310b2fe20a6ad27  /tmp/ZED_SDK_Linux.run' | sha256sum -c - && \
    bash /tmp/ZED_SDK_Linux.run silent skip_drivers && ldconfig
ARG ZED_SERIAL
RUN test -n "${ZED_SERIAL}" && [[ "${ZED_SERIAL}" =~ ^[0-9]+$ ]] && \
    mkdir -p /usr/local/zed/settings && \
    curl -fL --retry 3 "https://calib.stereolabs.com/?SN=${ZED_SERIAL}" \
      -o "/usr/local/zed/settings/SN${ZED_SERIAL}.conf" && \
    test -s "/usr/local/zed/settings/SN${ZED_SERIAL}.conf"
COPY ai_ws/src /full/ros_ws/src
WORKDIR /full/ros_ws
RUN (test -f /etc/ros/rosdep/sources.list.d/20-default.list || rosdep init) && \
    rosdep update --rosdistro jazzy && \
    source /opt/ros/jazzy/setup.bash && \
    paths=(src/ai_worker/* src/dynamixel_hardware_interface src/dynamixel_interfaces \
      src/DynamixelSDK/ros/dynamixel_sdk src/robotis_interfaces \
      src/robotis_hand/robotis_hand_description src/realsense-ros/realsense2_camera \
      src/realsense-ros/realsense2_description src/realsense-ros/realsense2_camera_msgs \
      src/dual_laser_merger src/Lakibeam_ROS2_Driver) && \
    mapfile -t zed_paths < <(colcon --log-base /tmp/zed-discovery list \
      --base-paths src/zed-ros2-wrapper --paths-only) && \
    paths+=("${zed_paths[@]}") && \
    rosdep install --from-paths "${paths[@]}" --ignore-src --rosdistro jazzy \
      --skip-keys librealsense2 -y && \
    test ! -e build && test ! -e install && test ! -e log && \
    CMAKE_BUILD_PARALLEL_LEVEL=2 MAKEFLAGS=-j2 colcon build --paths "${paths[@]}" \
      --parallel-workers 2 --event-handlers console_cohesion+ \
      --cmake-args -DCMAKE_BUILD_TYPE=Release
COPY hardware/rs_serial.yaml /full/ros_ws/install/ffw_bringup/share/ffw_bringup/config/common/rs_serial.yaml
COPY ai_ws/src/ai_worker/docker/lg2-sh5/ros-shell.sh /usr/local/bin/lg2-sh5-ros
WORKDIR /workspace
# No robot nodes, initialization poses or teleoperation start automatically.
ENTRYPOINT ["/bin/sleep"]
CMD ["infinity"]
