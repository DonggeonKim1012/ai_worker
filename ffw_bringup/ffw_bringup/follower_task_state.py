"""Publish the follower's selected initialization path, without commanding motion."""
import copy
import hashlib
import json
import math
from pathlib import Path
import yaml


class InitialPoseLoader(yaml.SafeLoader):
    """ROS parameter YAML can repeat the wildcard namespace for separate nodes."""


def _mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        value = loader.construct_object(value_node, deep=True)
        if key in result:
            if key == '/**' and isinstance(value, dict) and isinstance(result[key], dict):
                if set(result[key]) & set(value):
                    raise ValueError('Duplicate initialization node')
                result[key].update(value)
            else:
                raise ValueError(f'Duplicate initialization key: {key}')
        else:
            result[key] = value
    return result


InitialPoseLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def read_initial_pose(path):
    return yaml.load(Path(path).read_text(), Loader=InitialPoseLoader)


def task_initial_pose(config_root, task_name):
    root = Path(config_root).resolve()
    if not task_name or not task_name.replace('_', '').isalnum():
        raise ValueError('Invalid task_name')
    task_path = root / 'tasks' / (task_name + '.yaml')
    if not task_path.is_file():
        raise FileNotFoundError(task_path)
    task = yaml.safe_load(task_path.read_text())
    spec = task['initial_pose']
    base = (root / spec['base_file']).resolve()
    if not base.is_relative_to(root):
        raise ValueError('Initialization base must be inside config')
    document = copy.deepcopy(read_initial_pose(base))
    for node, overrides in spec['overrides'].items():
        params = document['/**'][node]['ros__parameters']
        for step, values in overrides.items():
            if step not in params['step_names'] or len(values) != len(params['joint_names']):
                raise ValueError('Invalid initialization override')
            if not all(type(v) in (int, float) and math.isfinite(v) for v in values):
                raise ValueError('Non-finite initialization target')
            params[step] = list(values)
    return document


def profile_message(path, task_name):
    path = Path(path)
    document = read_initial_pose(path)['/**']
    groups = {}
    for group in ('arm_l', 'arm_r'):
        params = document[group + '_joint_trajectory_executor']['ros__parameters']
        groups[group] = {k: params[k] for k in ('joint_names', 'action_topic', 'position_tolerance')}
        groups[group]['steps'] = [{'name': step, 'positions': params[step]}
                                  for step in params['step_names']]
    return {'task_name': task_name, 'profile_file': str(path),
            'profile_sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'groups': groups}


def reverse_arm_plan(message, expected_groups):
    """Validate the advertised path and reverse every waypoint without deduping."""
    groups = message['groups']
    if set(groups) != {'arm_l', 'arm_r'}:
        raise ValueError('Bringdown profile must contain exactly both arms')
    step_names = None
    for group, params in groups.items():
        expected = expected_groups[group]
        if params['joint_names'] != expected['names'] or params['action_topic'] != expected['topic']:
            raise ValueError('Initialization joint names/action topic mismatch')
        steps = params['steps']
        names = [step['name'] for step in steps]
        if not names or len(set(names)) != len(names):
            raise ValueError('Initialization steps must be nonempty and unique')
        if step_names is not None and names != step_names:
            raise ValueError('Left/right arm initialization steps must match')
        step_names = names
        for step in steps:
            values = step['positions']
            if len(values) != len(expected['names']) or not all(
                    type(v) in (int, float) and math.isfinite(v) for v in values):
                raise ValueError('Invalid initialization waypoint')
    phases = [(step_names[i], {g: list(groups[g]['steps'][i]['positions']) for g in groups})
              for i in reversed(range(len(step_names)))]
    phases.append(('arms_down', {g: [0.0] * len(expected_groups[g]['names']) for g in groups}))
    return phases


def main(args=None):
    import rclpy
    from rclpy.node import Node
    from rclpy.qos import QoSProfile, DurabilityPolicy
    from std_msgs.msg import String
    rclpy.init(args=args)
    node = Node('follower_task_state')
    task = node.declare_parameter('task_name', '').value
    path = node.declare_parameter('initial_pose_file', '').value
    message = profile_message(path, task)
    qos = QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL)
    profile_pub = node.create_publisher(String, '/ffw/init_profile', qos)
    task_pub = node.create_publisher(String, '/ffw/task_name', qos)
    def publish():
        profile_pub.publish(String(data=json.dumps(message)))
        task_pub.publish(String(data=task))
    node.create_timer(.5, publish)
    publish()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
