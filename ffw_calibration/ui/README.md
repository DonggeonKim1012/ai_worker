# AI Worker calibration UI

This React UI connects to the `ffw_calibration` ROS service through rosbridge. The ROS launch file serves the production build at port 5173 and starts rosbridge at port 9090.

Build the UI before building the ROS package:

```bash
cd ffw_calibration/ui
npm ci
npm run build
```

Then build and source the ROS workspace, and launch:

```bash
ros2 launch ffw_calibration ffw_calibration.launch.py \
  homing_offsets_path:=/path/to/persistent/homing_offsets.yaml
```

Open `http://<robot-host>:5173` in a browser. `launch_ui:=false` starts only the ROS service and rosbridge. The Dockerfiles build the UI automatically when this package is present. The launch default for `homing_offsets_path` is the package's installed example; pass a writable persistent path for real calibration. The UI's head-joint list is informational; calibration actions currently cover the arm joints implemented by the service.
