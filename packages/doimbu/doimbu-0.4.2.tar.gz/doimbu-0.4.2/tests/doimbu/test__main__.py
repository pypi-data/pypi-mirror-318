import pytest
from argparse import Namespace
from pytest_mock.plugin import MockerFixture

from doimbu.__main__ import parse_args


@pytest.mark.parametrize(
    'args,expected_namespace',
    [
        pytest.param(
            [],  # args
            Namespace(
                default_variant=None,
                tag_namespace=None,
                tag_repository=None,
                build_args=None,
                only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),  # expected_namespace (parsed args)
            id='No args'),
        pytest.param(
            ['-d', 'nobel'],  # args
            Namespace(
                default_variant='nobel',
                tag_namespace=None,
                tag_repository=None,
                build_args=None,
                only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),  # expected_namespace (parsed args)
            id='default-variant short'),
        pytest.param(
            ['--default-variant', 'nobel'],  # args
            Namespace(
                default_variant='nobel',
                tag_namespace=None,
                tag_repository=None,
                build_args=None,
                only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),  # expected_namespace (parsed args)
            id='default-variant long'),
        pytest.param(
            ['--tag-namespace', 'some-org'],
            Namespace(
                default_variant=None,
                tag_namespace='some-org',
                tag_repository=None,
                build_args=None,
                only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),
            id='tag-namespace'),
        pytest.param(
            ['--tag-repository', 'some-repo'],
            Namespace(
                default_variant=None,
                tag_namespace=None,
                tag_repository='some-repo',
                build_args=None,
                only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),
            id='tag-repository'),
        pytest.param(
            ['-d', 'ubi8', '-n', 'other-org', '-r', 'other-repo'],
            Namespace(
                default_variant='ubi8',
                tag_namespace='other-org',
                tag_repository='other-repo',
                build_args=None,
                only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),
            id='multiple params'),
        pytest.param(
            ['--build-arg', 'linux_username=some_linux_username'],
            Namespace(
                default_variant=None,
                tag_namespace=None,
                tag_repository=None,
                build_args={
                    'linux_username': 'some_linux_username',
                },only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),
            id='build-arg'),
        pytest.param(
            [
                '--build-arg', 'linux_username=some_linux_username',
                '--build-arg', 'git_user_email=someone@somecompany.com'
            ],
            Namespace(
                default_variant=None,
                tag_namespace=None,
                tag_repository=None,
                build_args={
                    'linux_username': 'some_linux_username',
                    'git_user_email': 'someone@somecompany.com'
                },only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),
            id='multiple build-args'),
        pytest.param(
            ['--build-arg', 'git_username="some git user"'],
            Namespace(
                default_variant=None,
                tag_namespace=None,
                tag_repository=None,
                build_args={
                    'git_username': 'some git user',
                },only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),
            id='build-arg with space'),

        pytest.param(
            ['--only-default-variant'],
            Namespace(
                default_variant=None,
                tag_namespace=None,
                tag_repository=None,
                build_args=None,
                only_default_variant=True,
                tag_omit_latest=False,
                dry_run=False),
            id='only-default-variant'),
        pytest.param(
            ['--tag-omit-latest'], Namespace(
                default_variant=None,
                tag_namespace=None,
                tag_repository=None,
                build_args=None,
                only_default_variant=False,
                tag_omit_latest=True,
                dry_run=False),
            id='tag-omit-latest'),
        pytest.param(
            ['--dry-run'],
            Namespace(
                default_variant=None,
                tag_namespace=None,
                tag_repository=None,
                build_args=None,
                only_default_variant=False,
                tag_omit_latest=False,
                dry_run=True),
            id='dry-run'),
    ])
def test_parse_args(
        mocker: MockerFixture,
        args: list[str],
        expected_namespace: Namespace) -> None:
    if not args:
        mocker.patch(
            'doimbu.__main__.argparse._sys.argv',
            return_value=['doimbu.__main__.py'])

    assert parse_args(*args) == expected_namespace