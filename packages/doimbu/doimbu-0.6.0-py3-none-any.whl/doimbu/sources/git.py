import subprocess

from pydantic import ValidationError

from doimbu.version import DOCKER_IMAGE_FIRST_VERSION, Version


GIT_FETCH_AND_LIST_TAGS_CMD = (
    'git fetch --tags & git tag --sort=version:refname')


def get_latest_git_version_tag() -> Version:
    """Get the latest git version tag.

    - Fetches all tags from remote
    - Retrieve an ordered list of tags from git that contains version
    and non-version tags.

    :return: return the latest tag that matches the version pattern
        (major.minor.patch - where minor and patch are optional)
    """
    completed_process = subprocess.run(
        GIT_FETCH_AND_LIST_TAGS_CMD, shell=True, capture_output=True)

    stdout = completed_process.stdout.decode()

    if stdout:
        versions = stdout.split('\n')

        for version in reversed(versions):
            try:
                return Version(version=version)
            except ValidationError:
                pass

    return Version(version=DOCKER_IMAGE_FIRST_VERSION)