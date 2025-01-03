from argparse import Namespace
from configparser import ConfigParser
from pathlib import Path

import pytest

from doimbu import builder
from doimbu.builder import BuilderConfig
from doimbu.sources import file_config
from doimbu.version import Version


@pytest.mark.parametrize(
    'build_config,variants,expected_build_plan',
    [
        pytest.param(
            BuilderConfig(
                version='1.1.0',
                default_variant='nobel',
                tag_repository='mongodb-community-server'),  # build_config
            ['nobel'],  # variants
            [
                'docker image build -t mongodb-community-server:1.1.0-nobel'
                ' -t mongodb-community-server variants/nobel/.'
            ],  # expected_build_plan
            id='single variant | minimal BuildConfig'
        ),
        pytest.param(
            BuilderConfig(
                version='1.1.0',
                default_variant='nobel',
                tag_repository='mongodb-community-server'),  # build_config
            ['bullseye', 'nobel', 'ubi8'],  # variants
            [
                'docker image build -t mongodb-community-server:1.1.0-bullseye'
                ' variants/bullseye/.',
                'docker image build -t mongodb-community-server:1.1.0-nobel'
                ' -t mongodb-community-server variants/nobel/.',
                'docker image build -t mongodb-community-server:1.1.0-ubi8'
                ' variants/ubi8/.'
            ],  # expected_build_plan
            id='3 variants | minimal BuildConfig'
        ),
        pytest.param(
            BuilderConfig(
                version='1.1.0',
                default_variant='nobel',
                tag_namespace='mongodb',
                tag_repository='mongodb-community-server',
                build_args={
                    'git_username': 'some git user',
                    'git_user_email': 'someone@somecompany.com'
                },
                only_default_variant=True,
                tag_omit_latest=True,
                dry_run=True),  # build_config
            ['bullseye', 'nobel'],  # variants
            [
                'docker image build -t mongodb/mongodb-community-server'
                ':1.1.0-nobel --build-arg git_username="some git user"'
                ' --build-arg git_user_email="someone@somecompany.com"'
                ' variants/nobel/.'
            ],  # expected_build_plan
            id='2 variants | complete BuildConfig'
        )
    ]
)
def test_generate_build_plan(
        build_config: builder.BuilderConfig,
        variants: list[str],
        expected_build_plan: list[str]) -> None:
    assert (builder.generate_build_plan(build_config, variants)
            == expected_build_plan)


@pytest.mark.parametrize(
    'project_root_path,config_file,args,expected_builder_config',
    [
        pytest.param(
            Path('/path/to/image/bed_machine'),  # project_root_path
            file_config.create_file_config(
                'ubi8',
                Version(version='3.1.0'),
                'mongodb',
                'mongodb-community-server',
                {
                    'username': 'thomas thompson',
                    'user_email': 'thomas.thompson@mongodb.com',
                },
                True,
                True,
                True),  # config_file
            Namespace(
                default_variant=None,
                tag_namespace=None,
                tag_repository=None,
                build_args=None,
                only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),  # args
            builder.BuilderConfig(
                version='3.1.0',
                default_variant='ubi8',
                tag_namespace='mongodb',
                tag_repository='mongodb-community-server',
                build_args={
                    'username': 'thomas thompson',
                    'user_email': 'thomas.thompson@mongodb.com'
                },
                only_default_variant=True,
                tag_omit_latest=True,
                dry_run=True),  # expected_builder_config
            id='no params / full config file'),
        pytest.param(
            Path('/path/to/image/bed_machine'),  # project_root_path
            file_config.create_file_config(
                'ubi8',
                version=Version(version='3.1.0')),  # config_file
            Namespace(
                default_variant=None,
                tag_namespace=None,
                tag_repository=None,
                build_args=None,
                only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),  # args
            builder.BuilderConfig(
                version='3.1.0',
                default_variant='ubi8',
                tag_repository='bed_machine'),  # expected_builder_config
            id='no params / only mandatory config file'),
        pytest.param(
            Path('/path/to/image/bed_machine'),  # project_root_path
            file_config.create_file_config(
                'ubi8',
                version=Version(version='3.1.0'),
                only_default_variant=True),  # config_file
            Namespace(
                default_variant='nobel',
                tag_namespace=None,
                tag_repository=None,
                build_args=None,
                only_default_variant=False,
                tag_omit_latest=False,
                dry_run=False),  # args  # args
            builder.BuilderConfig(
                version='3.1.0',
                default_variant='nobel',
                tag_repository='bed_machine',
                only_default_variant=True),  # expected_builder_config
            id='partial params / partial config file'),
        pytest.param(
            Path('/path/to/image/bed_machine'),  # project_root_path
            file_config.create_file_config(
                'ubi8',
                version=Version(version='3.1.0'),
                tag_namespace='mongodb',
                tag_repository='mongodb-community-server'),  # config_file
            Namespace(
                default_variant='nobel',
                tag_namespace='mongodb',
                tag_repository='mongodb-enterprise-server',
                build_args={
                    'linux_username': 'some_linux_username',
                },
                only_default_variant=True,
                tag_omit_latest=True,
                dry_run=True),  # args
            builder.BuilderConfig(
                version='3.1.0',
                default_variant='nobel',
                tag_namespace='mongodb',
                tag_repository='mongodb-enterprise-server',
                build_args={
                    'linux_username': 'some_linux_username',
                },
                only_default_variant=True,
                tag_omit_latest=True,
                dry_run=True
            ),  # expected_builder_config
            id='all params / all config file')
    ]
)
def test_get_builder_config(
        project_root_path: Path,
        config_file: ConfigParser,
        args: Namespace,
        expected_builder_config: builder.BuilderConfig | None) -> None:

    if expected_builder_config:
        assert (builder.get_builder_config(
            project_root_path, config_file, args) == expected_builder_config)
    else:
        with pytest.raises(KeyError, match=r"doimbu"):
            builder.get_builder_config(project_root_path, config_file, args)
