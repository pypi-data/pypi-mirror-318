from pathlib import Path

from doimbu.sources import dir_structure

import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture(
    params=[
        {
            'scenario_dir': 'no_variants_dir',
            'variants_dir': None,
            'variants': []
        },
        {
            'scenario_dir': 'empty_variants_dir',
            'variants_dir': 'variants',
            'variants': []
        },
        {
            'scenario_dir': 'single_variant',
            'variants_dir': 'variants',
            'variants': ['nobel']
        },
        {
            'scenario_dir': 'multiple_variants',
            'variants_dir': 'variants',
            'variants': ['nobel', 'ubi8', 'bookworm']
        }
    ],
    ids=[
        'no variants dir',
        'empty variants dir',
        'single variant',
        'multiple variant'
    ]
)
def prepare_variants_test_dir(
        path_test_dir: Path,
        request: SubRequest) -> dict[str, Path | list[str]]:
    scenario_dir = path_test_dir / request.param['scenario_dir']
    scenario_dir.mkdir()

    if request.param['variants_dir']:
        variants_dir = scenario_dir / request.param['variants_dir']
        variants_dir.mkdir()

        for variant in request.param['variants']:
            variant_dir = variants_dir / variant
            variant_dir.mkdir()

    return {
        'scenario_dir': scenario_dir,
        'expected_variants': request.param['variants']
    }


@pytest.mark.usefixtures("cleanup_test_dir")
def test_get_variants_list(prepare_variants_test_dir: dict[str, any]) -> None:
    variants = dir_structure.get_variants_list(
        prepare_variants_test_dir['scenario_dir'])

    assert sorted(variants) == sorted(
        prepare_variants_test_dir['expected_variants'])