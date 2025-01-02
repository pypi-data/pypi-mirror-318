import subprocess
from pathlib import Path

import pytest


from tests.paths import TEST_TEMP_DIR


def clean_path(path: Path) -> None:
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        for dir_content_path in path.iterdir():
            clean_path(dir_content_path)
        path.rmdir()

@pytest.fixture(scope='module')
def path_test_dir() -> Path:
    return TEST_TEMP_DIR


@pytest.fixture(scope='module')
def cleanup_test_dir(path_test_dir: Path) -> None:
    clean_path(path_test_dir)

    path_test_dir.mkdir()
