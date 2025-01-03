from contextlib import nullcontext as does_not_raise

import pytest
from _pytest.python_api import RaisesContext
from pydantic_core import ValidationError

from doimbu.version import parse_version, Version


@pytest.mark.parametrize(
    'version,expected_major,expected_minor,expected_patch',
    [
        pytest.param('1', 1,  0, 0, id='only major'),
        pytest.param('0.1', 0, 1, 0, id='major_minor'),
        pytest.param('3.2.1', 3, 2, 1, id='major_minor_patch'),
    ]
)
def test_parse_version(
        version: str,
        expected_major: int,
        expected_minor: int,
        expected_patch: int) -> None:
    assert parse_version(version) == (
        expected_major, expected_minor, expected_patch
    )


@pytest.mark.parametrize(
    'current_version,other_version,expected_ge_result',
    [
        pytest.param(
            Version(version='1.1.1'),
            Version(version='1.1.1'),
            True,
            id='equal'),
        pytest.param(
            Version(version='2.0.1'),
            Version(version='1.2.1'),
            True,
            id='bigger major'),
        pytest.param(
            Version(version='2.0.1'),
            Version(version='3.2.1'),
            False,
            id='smaller major'),
        pytest.param(
            Version(version='2.10.1'),
            Version(version='2.2.1'),
            True,
            id='bigger minor'),
        pytest.param(
            Version(version='2.0.1',),
            Version(version='2.2.1'),
            False,
            id='smaller minor'),
        pytest.param(
            Version(version='3.0.11'),
            Version(version='3.0.1'),
            True,
            id='bigger patch'),
        pytest.param(
            Version(version='3.0.1'),
            Version(version='3.0.2'),
            False,
            id='smaller patch')
    ])
def test_version_ge(
        current_version: Version,
        other_version: Version,
        expected_ge_result: bool) -> None:
    assert (current_version >= other_version) == expected_ge_result


@pytest.mark.parametrize(
    'version,expected_version,expected_exception',
    [
        pytest.param(
            '3.2.1', # version
            Version(version='3.2.1'),  # expected_version
            does_not_raise(),  # expected_exception
            id='3.2.1 - major minor patch'),
        pytest.param(
            '1.0.0',  # version
            Version(version='1.0.0'),  # expected_version
            does_not_raise(),  # expected_exception
            id='1.0.0 - major'),
        pytest.param(
            '1',  # version
            Version(version='1.0.0'),  # expected_version
            does_not_raise(),  # expected_exception
            id='1 - major compact'),
        pytest.param(
            '0.2.0',
            Version(version='0.2.0'),  # expected_version
            does_not_raise(),  # expected_exception
            id='0.2.0 - minor'),
        pytest.param(
            '0.2',  # version
            Version(version='0.2.0'),  # expected_version
            does_not_raise(),  # expected_exception
            id='0.2 - minor compact'),
        pytest.param(
            '1.2.3.4',  # version
            None,  # expected_version
            pytest.raises(ValidationError),  # expected_exception
            id='1.2.3.4 - too many sections'),
        pytest.param(
            '0.-3.0',  # version
            None,  # expected_version
            pytest.raises(ValidationError),  # expected_exception
            id='0.-3.0 - negative section'),
        pytest.param(
            '1.2.x',  # version
            None,  # expected_version
            pytest.raises(ValidationError),  # expected_exception
            id='1.2.x - not int section')
    ]
)
def test_version_validation(
        version: str,
        expected_version: Version | None,
        expected_exception: does_not_raise | RaisesContext) -> None:
    with expected_exception:
        assert Version(version=version) == expected_version