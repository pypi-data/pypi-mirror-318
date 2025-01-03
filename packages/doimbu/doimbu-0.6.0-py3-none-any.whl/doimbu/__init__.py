import tomllib
from pathlib import Path

from doimbu.paths import PYPROJECT_TOML_PATH


def get_version(pyproject_toml_path: Path) -> str:
    with pyproject_toml_path.open(mode='rb') as f:
        return tomllib.load(f)["tool"]["poetry"]["version"]


__version__ = get_version(PYPROJECT_TOML_PATH)
