#!/usr/bin/env bash
# Run RViz beside Xvfb so its graphics memory is in the same IPC namespace.
# No robot bringup or movement goals are started by this script.
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
nav_dir="$(cd -- "${script_dir}/.." && pwd)"
repo_dir="$(cd -- "${nav_dir}/.." && pwd)"
desktop_container="${SH5_RVIZ_DESKTOP_CONTAINER:-novnc-server}"
robot_container="${SH5_ROBOT_CONTAINER:-ai_worker}"
for container in "${desktop_container}" "${robot_container}"; do
  test "$(docker inspect --format '{{.State.Running}}' "${container}")" = true
done
if ! docker exec "${desktop_container}" sh -c 'test -f /opt/ros/jazzy/lib/librmw_zenoh_cpp.so && test -d /opt/ros/jazzy/share/nav2_rviz_plugins'; then
  docker exec "${desktop_container}" bash -lc 'apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ros-jazzy-rmw-zenoh-cpp ros-jazzy-nav2-rviz-plugins'
fi
docker exec "${desktop_container}" mkdir -p /opt/sh5_visualization/share/ament_index/resource_index/packages /opt/sh5_visualization/share/ffw_description /opt/sh5_visualization/share/realsense2_description
docker cp "${repo_dir}/ffw_description/." "${desktop_container}:/opt/sh5_visualization/share/ffw_description"
docker cp "${nav_dir}/rviz/sh5_navigation_debug.rviz" "${desktop_container}:/opt/sh5_visualization/sh5_navigation_debug.rviz"
rviz_temp_dir="$(mktemp -d)"
trap 'rm -rf -- "${rviz_temp_dir}"' EXIT
docker cp -L "${robot_container}:/root/ros2_ws/src/realsense-ros/realsense2_description" "${rviz_temp_dir}/realsense2_description"
docker cp "${rviz_temp_dir}/realsense2_description/." "${desktop_container}:/opt/sh5_visualization/share/realsense2_description"
docker exec "${desktop_container}" bash -lc '
  for package in ffw_description realsense2_description; do
    touch "/opt/sh5_visualization/share/ament_index/resource_index/packages/${package}"
    mkdir -p "/root/ros2_ws/install/${package}/share"
    # The published robot_description also contains absolute file:// mesh paths.
    if [ ! -e "/root/ros2_ws/install/${package}/share/${package}" ]; then
      ln -s "/opt/sh5_visualization/share/${package}" "/root/ros2_ws/install/${package}/share/${package}"
    fi
  done'
if ! docker exec "${desktop_container}" pgrep -f '^rviz2 -d /opt/sh5_visualization/sh5_navigation_debug.rviz$' >/dev/null; then
  docker exec -d -e DISPLAY=:99 -e ROS_DOMAIN_ID="${ROS_DOMAIN_ID:-30}" -e RMW_IMPLEMENTATION=rmw_zenoh_cpp -e LIBGL_ALWAYS_SOFTWARE=1 "${desktop_container}" bash -lc 'source /opt/ros/jazzy/setup.bash; export AMENT_PREFIX_PATH=/opt/sh5_visualization:$AMENT_PREFIX_PATH; exec rviz2 -d /opt/sh5_visualization/sh5_navigation_debug.rviz > /tmp/sh5_rviz.log 2>&1'
fi
printf 'SH5 RViz is open in the existing noVNC desktop (port 8090).\n'
