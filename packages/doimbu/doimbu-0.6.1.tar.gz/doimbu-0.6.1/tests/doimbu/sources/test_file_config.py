import subprocess
from configparser import ConfigParser
from pathlib import Path

import pytest
from _pytest.fixtures import SubRequest
from pytest_mock.plugin import MockerFixture

from doimbu.paths import BUILDER_CONFIG_FILE
from doimbu.sources import file_config

from tests.paths import TEST_BUILDER_CONFIG_PATH, TEST_TEMP_DIR


@pytest.mark.usefixtures("cleanup_test_dir")
@pytest.mark.parametrize(
    'default_variant,tag_section_args,build_args,'
    'execution_mode_args,git_list_tag_cmd_return',
    [
        pytest.param(
            'nobel',  # default_variant
            {},  # tag_section_args
            {},  # build_args
            {},  # execution_mode_args
            b'1.0.1\n2.2.3\n3.1\nsomething_else\n',  # git_list_tag_cmd_return
            id='only required'),
        pytest.param(
            'ubi8',  # default_variant
            {},  # tag_section_args
            {
                'linux_username': 'joe',
                'git_username': '"joe average"',
                'git_user_email': 'average.joe@pirilimpimpim.org'
            },  # build_args
            {},  # execution_mode_args
            b'1.0.1\n2.2.3\n3.1\nsomething_else\n',  # git_list_tag_cmd_return
            id='build args'),
        pytest.param(
            'nobel',  # default_variant
            {
                'tag_namespace': 'redhat',
                'tag_repository': 'ubi9'
            },  # tag_section_args
            {},  # build_args
            {},  # execution_mode_args
            b'1.0.1\n2.2.3\n3.1\nsomething_else\n',  # git_list_tag_cmd_return
            id='tag section'),
        pytest.param(
            'nobel',  # default_variant
            {},  # tag_section_args
            {},  # build_args
            {
                'only_default_variant': True,
                'tag_omit_latest': True,
                'dry_run': True
            },  # execution_mode_args
            b'1.0.1\n2.2.3\n3.1\nsomething_else\n',  # git_list_tag_cmd_return
            id='execution-mode section'),
        pytest.param(
            'nobel',  # default_variant
            {'tag_namespace': 'redhat'},  # tag_section_args
            {'linux_username': 'joe'},  # build_args
            {'dry_run': True},  # execution_mode_args
            b'1.0.1\n2.2.3\n3.1\nsomething_else\n',  # git_list_tag_cmd_return
            id='multiple section')
    ]
)
def test_write_file_config(
        default_variant: str,
        tag_section_args: dict[str, str],
        build_args: dict[str, str] | None,
        execution_mode_args: dict[str, bool],
        git_list_tag_cmd_return: bytes,
        mocker: MockerFixture) -> None:
    mocker.patch(
        'doimbu.sources.git.subprocess.run',
        return_value=subprocess.CompletedProcess(
            [], 0, stdout=git_list_tag_cmd_return))

    file_config.write_file_config(
        config_path=TEST_BUILDER_CONFIG_PATH,
        default_variant=default_variant,
        build_args=build_args,
        **tag_section_args,
        **execution_mode_args)

    config = ConfigParser()
    config.read(TEST_BUILDER_CONFIG_PATH)

    assert 'doimbu' in config.sections()
    assert config['doimbu']['default_variant'] == default_variant

    config_sections_args_map = {
        'tag': tag_section_args,
        'build-args': build_args
    }
    for config_section, config_items in config_sections_args_map.items():
        if config_items:
            for config_item_key, config_item_value in config_items.items():
                assert (config[config_section][config_item_key]
                        == config_item_value)

    for key, value in execution_mode_args.items():
        assert config['execution-mode'].getboolean(key) == value


def generate_config_from_dict(sections: list[dict[str, any]]) -> ConfigParser:
    config = ConfigParser()

    for section in sections:
        config[section['section_name']] = section['section_items']

    return config


@pytest.fixture(
    params=[
        {
            'scenario_dir': 'ok_file',
            'file_config': [
                {
                    'section_name': 'doimbu',
                    'section_items': {
                        'default_variant': 'nobel'
                    }
                },
                {
                    'section_name': 'tag',
                    'section_items': {
                        'version': '1.2.0'
                    }
                }
            ],
            'git_list_tag_cmd_return': b'1.0.1\n2.2.3\n3.1\nsomething_else\n',
            'expected_config': [
                {
                    'section_name': 'doimbu',
                    'section_items': {
                        'default_variant': 'nobel'
                    }
                },
                {
                    'section_name': 'tag',
                    'section_items': {
                        'version': '1.2.0'
                    }
                }
            ]
        },
        {
            'scenario_dir': 'file_missing_mandatory_section',
            'file_config': [
                {
                    'section_name': 'tag',
                    'section_items': {
                        'version': '1.2.0',
                        'tag_namespace': 'redhat'
                    }
                }
            ],
            'git_list_tag_cmd_return': b'1.0.1\n2.2.3\n3.1\nsomething_else\n',
            'expected_config': [
                {
                    'section_name': 'doimbu',
                    'section_items': {
                        'default_variant': 'ubi'
                    }
                },
                {
                    'section_name': 'tag',
                    'section_items': {
                        'version': '3.1.0',
                        'tag_namespace': 'redhat'
                    }
                }
            ]
        },
        {
            'scenario_dir': 'file_missing_mandatory_item',
            'file_config': [
                {
                    'section_name': 'doimbu',
                    'section_items': {
                        'something': 'x'
                    }
                }
            ],
            'git_list_tag_cmd_return': b'1.0.1\n2.2.3\n3.1\nsomething_else\n',
            'expected_config': [
                {
                    'section_name': 'doimbu',
                    'section_items': {
                        'something': 'x',
                        'default_variant': 'ubi'

                    }
                },
                {
                    'section_name': 'tag',
                    'section_items': {
                        'version': '3.1.0'
                    }
                }
            ]
        },
        {
            'scenario_dir': 'missing_config_file',
            'file_config': None,
            'git_list_tag_cmd_return': b'1.0.1\n2.2.3\n3.1\nsomething_else\n',
            'expected_config': [
                {
                    'section_name': 'doimbu',
                    'section_items': {
                        'default_variant': 'ubi'
                    }
                },
                {
                    'section_name': 'tag',
                    'section_items': {
                        'version': '3.1.0'
                    }
                }
            ]
        },
    ],
    ids=[
        'config file ok',
        'config file missing mandatory section',
        'config file missing mandatory item',
        'missing config file'
    ]
)
def params_test_get_file_config(
        request: SubRequest,
        mocker: MockerFixture) -> dict[str, Path | ConfigParser]:

    base_test_dir = TEST_TEMP_DIR / 'test_get_file_config'
    test_config_dir = base_test_dir / request.param['scenario_dir']
    test_config_path = test_config_dir / BUILDER_CONFIG_FILE

    test_config_dir.mkdir(parents=True)

    if request.param['file_config']:
        config = generate_config_from_dict(request.param['file_config'])

        with test_config_path.open('w') as f:
            config.write(f)

    mocker.patch(
        'doimbu.sources.git.subprocess.run',
        return_value=subprocess.CompletedProcess(
            [], 0, stdout=request.param['git_list_tag_cmd_return']))

    expected_config = generate_config_from_dict(
        request.param['expected_config'])

    return {
        'config_path': test_config_path,
        'variants': ['ubi', 'nobel', 'bullseye'],
        'expected_file_config': expected_config
    }


@pytest.mark.usefixtures("cleanup_test_dir")
def test_get_file_config(
        params_test_get_file_config: dict[str, Path | ConfigParser]) -> None:
    config_file = file_config.get_file_config(
        params_test_get_file_config['config_path'],
        params_test_get_file_config['variants']
    )

    expected_config = params_test_get_file_config['expected_file_config']

    assert set(config_file.sections()) == set(expected_config.sections())

    for section in expected_config.sections():
        assert config_file.items(section) == expected_config.items(section)
