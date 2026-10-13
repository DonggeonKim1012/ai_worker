from pathlib import Path
import tempfile
from unittest.mock import patch
import pytest
from ffw_teleop.hand_preset_model import PresetCatalog, normalize_trigger

CONFIG = Path(__file__).resolve().parents[2] / 'ffw_bringup/config/ffw_lg2_mini_leader/hand_preset_interpolator.yaml'

@pytest.fixture
def catalog(tmp_path):
    return PresetCatalog(tmp_path / 'presets.json', CONFIG)


def test_presets_have_independent_open_and_closed_targets(catalog):
    for side in ('left', 'right'):
        for number in range(7):
            assert catalog.positions(side, number, 1) == pytest.approx(catalog.config[f'{side}_preset_{number}'])
            assert catalog.positions(side, number, 0) == catalog.config.get(
                f'{side}_open_pose_{number}', catalog.config[f'{side}_open_pose'])


def test_custom_persistence_and_delete_restore(catalog):
    catalog.apply('custom/save', dict(name='Custom', curls=[0, .25, .5, .75, 1]))
    restored = PresetCatalog(catalog.path, CONFIG)
    assert restored.positions('left', 100, 1) == catalog.positions('left', 100, 1)
    restored.apply('set', dict(side='both', preset_id=100))
    with pytest.raises(ValueError):
        restored.apply('manage/delete', dict(preset_id=100))
    restored.apply('set', dict(side='both', preset_id=5))
    restored.apply('manage/delete', dict(preset_id=100))
    assert 100 not in restored.presets
    restored.apply('manage/restore', dict(preset_id=100))
    assert 100 in restored.presets


@pytest.mark.parametrize('curls', [[0]*4, [float('nan')]*5, [1.1]*5, [True]*5])
def test_invalid_custom_presets_do_not_mutate_catalog(catalog, curls):
    before = catalog.status()
    with pytest.raises(ValueError):
        catalog.apply('custom/save', dict(name='bad', curls=curls))
    assert catalog.status() == before


def test_failed_write_rolls_back(catalog):
    with patch.object(catalog, 'persist', side_effect=OSError('full')):
        with pytest.raises(OSError):
            catalog.apply('custom/save', dict(name='Custom', curls=[.5]*5))
    assert 100 not in catalog.presets


def test_trigger_clamping_and_invalid_input():
    assert normalize_trigger(-2, -.1, 1.1) == 0
    assert normalize_trigger(2, -.1, 1.1) == 1
    assert normalize_trigger(.5, -.1, 1.1) == pytest.approx(.5)
    with pytest.raises(ValueError):
        normalize_trigger(float('nan'), -.1, 1.1)
