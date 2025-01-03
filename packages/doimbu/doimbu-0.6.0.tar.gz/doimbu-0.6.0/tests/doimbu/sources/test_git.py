import subprocess

import pytest
from pytest_mock.plugin import MockerFixture

from doimbu.sources import git
from doimbu.version import Version


@pytest.mark.parametrize(
    'git_list_tag_cmd_return,expected_version',
    [
        pytest.param(
            b'',  # git_list_tag_cmd_return
            Version(version='0.1.0'),  # expected_version
            id='no tag'),
        pytest.param(
            b'1.0\n',  # git_list_tag_cmd_return
            Version(version='1.0.0'),  # expected_version
            id='one good tag - 1.0'),
        pytest.param(
            b'1.0.1\n2.2.3\n3.1\n',  # git_list_tag_cmd_return
            Version(version='3.1.0'),  # expected_version
            id='one good tag - 3.1.0'),
        pytest.param(
            b'1.0.1\n2.2.3\n3.1\nsomething_else\n',  # git_list_tag_cmd_return
            Version(version='3.1.0'),  # expected_version
            id='multiple tags with latest non version tag - somthing else'),
        pytest.param(
            b'something_else\n',  # git_list_tag_cmd_return
            Version(version='0.1.0'),  # expected_version
            id=' non-version tag - somthing else'),
    ]
)
def test_get_latest_git_version_tag(
        git_list_tag_cmd_return: bytes,
        expected_version: Version,
        mocker: MockerFixture) -> None:
    mocker.patch(
        'doimbu.sources.git.subprocess.run',
        return_value=subprocess.CompletedProcess(
            [], 0, stdout=git_list_tag_cmd_return))

    latest_git_version = git.get_latest_git_version_tag()

    assert latest_git_version == expected_version