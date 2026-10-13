"""Validated SH5 preset catalog, independent of ROS and hardware."""
import copy
import json
import math
import os
from pathlib import Path
import tempfile
import time

import yaml


def load_config(filename=None):
    if filename is None:
        from ament_index_python.packages import get_package_share_directory
        filename = Path(get_package_share_directory('ffw_bringup')) / 'config/ffw_lg2_mini_leader/hand_preset_interpolator.yaml'
    return yaml.safe_load(Path(filename).read_text())['hand_preset_interpolator']['ros__parameters']


def normalize_trigger(value, lower, upper):
    if not all(math.isfinite(v) for v in (value, lower, upper)) or lower == upper:
        raise ValueError('Trigger value and distinct endpoints must be finite')
    return min(1.0, max(0.0, (value - lower) / (upper - lower)))


def curls_valid(values):
    if not isinstance(values, list) or len(values) != 5 or any(
            type(v) not in (int, float) or not math.isfinite(v) or not 0 <= v <= 1
            for v in values):
        raise ValueError('curls must contain five finite numbers between 0 and 1')
    return values


class PresetCatalog:
    def __init__(self, filename, config_file=None):
        self.config = load_config(config_file)
        self.path = Path(filename)
        self.template = int(self.config['custom_template_preset_id'])
        self.active = {s: int(self.config[f'{s}_preset_id']) for s in ('left', 'right')}
        self.presets = {}
        self.deleted = {}
        for number in self.config['preset_ids']:
            for side in self.active:
                names = self.config[f'{side}_joint_names']
                if len(names) != 20 or len(set(names)) != 20:
                    raise ValueError('Each hand must have 20 unique joint names')
                for key in (f'{side}_preset_{number}', f'{side}_open_pose'):
                    values = self.config[key]
                    if len(values) != 20 or any(not math.isfinite(v) for v in values):
                        raise ValueError(f'Invalid pose: {key}')
                opened = self.config.get(f'{side}_open_pose_{number}', self.config[f'{side}_open_pose'])
                if len(opened) != 20 or any(not math.isfinite(v) for v in opened):
                    raise ValueError('Invalid preset open pose')
            self.presets[number] = dict(id=number, name=self.config[f'preset_{number}_name'],
                description=self.config[f'preset_{number}_description'],
                visual=self.config[f'preset_{number}_visual'], builtin=True, pose=number, note='')
        if self.path.exists():
            saved = json.loads(self.path.read_text())
            for preset in saved['presets']:
                number = preset['id']
                if type(number) is not int or number in self.presets or number < self.config['custom_preset_id_min']:
                    raise ValueError('Invalid saved custom preset ID')
                curls_valid(preset['curls'])
                preset['pose'] = self.template
                preset['builtin'] = False
                self.presets[number] = preset
            for number, metadata in saved.get('metadata', {}).items():
                number = int(number)
                if number in self.presets:
                    self.presets[number].update({k: str(v) for k, v in metadata.items()
                                                if k in ('name', 'description', 'note')})
        if any(number not in self.presets for number in self.active.values()):
            raise ValueError('Default preset does not exist')

    def positions(self, side, number, amount):
        if side not in self.active or not math.isfinite(amount) or not 0 <= amount <= 1:
            raise ValueError('Invalid hand or interpolation amount')
        preset = self.presets[number]
        profile = preset['pose']
        opened = self.config.get(f'{side}_open_pose_{profile}', self.config[f'{side}_open_pose'])
        closed = self.config[f'{side}_preset_{profile}']
        curls = preset.get('curls', [1.0] * 5)
        return [a + (b - a) * amount * curls[i // 4] for i, (a, b) in enumerate(zip(opened, closed))]

    def persist(self):
        document = dict(presets=[p for p in self.presets.values() if not p['builtin']],
            metadata={str(n): {k: p[k] for k in ('name', 'description', 'note')}
                      for n, p in self.presets.items() if p['builtin']})
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', dir=self.path.parent, delete=False) as stream:
                temporary = stream.name
                json.dump(document, stream, allow_nan=False)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, self.path)
        finally:
            if temporary and os.path.exists(temporary):
                os.unlink(temporary)

    def apply(self, action, values):
        previous = copy.deepcopy((self.presets, self.active, self.deleted))
        try:
            if action == 'set':
                side, number = values['side'], values['preset_id']
                if side not in ('left', 'right', 'both') or type(number) is not int or number not in self.presets:
                    raise ValueError('Unknown hand or preset')
                for hand in self.active if side == 'both' else (side,):
                    self.active[hand] = number
                return
            if action == 'custom/save':
                curls = curls_valid(values['curls'])
                if not isinstance(values['name'], str) or not values['name'].strip():
                    raise ValueError('Preset name is required')
                number = max([self.config['custom_preset_id_min'] - 1, *self.presets, *self.deleted]) + 1
                self.presets[number] = dict(id=number, name=values['name'],
                    description=values.get('description', ''), note='', visual='custom',
                    builtin=False, pose=self.template, curls=list(curls))
            elif action == 'manage/update':
                preset = self.presets[values['preset_id']]
                for key in ('name', 'description', 'note'):
                    if key in values:
                        if not isinstance(values[key], str) or (key == 'name' and not values[key].strip()):
                            raise ValueError('Invalid metadata')
                        preset[key] = values[key]
            elif action == 'manage/delete':
                number = values['preset_id']
                if self.presets[number]['builtin'] or number in self.active.values():
                    raise ValueError('Cannot delete a built-in or selected preset')
                self.deleted[number] = (self.presets.pop(number), time.monotonic())
            elif action == 'manage/restore':
                number = values['preset_id']
                preset, deleted_at = self.deleted[number]
                if time.monotonic() - deleted_at > self.config['preset_delete_undo_sec']:
                    raise ValueError('Restore window expired')
                self.presets[number] = preset
                del self.deleted[number]
            else:
                raise ValueError('Unknown action')
            self.persist()
        except Exception:
            self.presets, self.active, self.deleted = previous
            raise

    def status(self):
        return dict(active=dict(self.active), presets=copy.deepcopy(list(self.presets.values())),
                    deleted=[number for number, (_, stamp) in self.deleted.items()
                             if time.monotonic() - stamp <= self.config['preset_delete_undo_sec']])
