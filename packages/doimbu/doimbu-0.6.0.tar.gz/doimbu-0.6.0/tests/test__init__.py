from doimbu import get_version

from tests.paths import TEST_PYPROJECT_TOML_PATH


def test_get_version() -> None:
    version = get_version(TEST_PYPROJECT_TOML_PATH)

    assert len(version.split('.')) == 3

    assert all((version_section.isdigit()
                for version_section in version.split('.')))
