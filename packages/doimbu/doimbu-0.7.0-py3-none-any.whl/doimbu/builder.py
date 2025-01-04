import subprocess
from argparse import Namespace
from configparser import ConfigParser
from pathlib import Path

from pydantic import BaseModel, ConfigDict

from doimbu.paths import BUILDER_CONFIG_PATH, EXECUTION_DIR
from doimbu.sources.file_config import get_file_config
from doimbu.sources.dir_structure import get_variants_list


class BuilderConfig(BaseModel):
    version: str
    default_variant: str
    tag_namespace: str | None = None
    tag_repository: str
    build_args: dict[str, str] | None = None
    # Change default behavior flags
    only_default_variant: bool = False
    tag_omit_latest: bool = False
    dry_run: bool = False

    model_config = ConfigDict(frozen=True)

def generate_build_plan(
        build_config: BuilderConfig, variants: list[str]) -> list[str]:
    build_plan = []

    if build_config.only_default_variant:
        variants = [build_config.default_variant]

    for variant in variants:
        command = 'docker image build'

        command += ' -t '
        if build_config.tag_namespace:
            command += f'{build_config.tag_namespace}/'
        command += build_config.tag_repository
        command += f':{build_config.version}-{variant}'

        # TODO: prevent setting as latest if version < latest git tag
        if (variant == build_config.default_variant
                and not build_config.tag_omit_latest):
            command += ' -t '
            if build_config.tag_namespace:
                command += f'{build_config.tag_namespace}/'
            command += build_config.tag_repository

        if build_config.build_args:
            for build_arg_key, build_arg_value in (
                    build_config.build_args.items()):
                command += f' --build-arg {build_arg_key}="{build_arg_value}"'

        command += f' variants/{variant}/.'

        build_plan.append(command)

    return build_plan


def get_builder_config(
        project_root_path: Path,
        config_file: ConfigParser,
        args: Namespace) -> BuilderConfig:
    config = {
        'tag_repository': project_root_path.stem
    }

    for section in config_file.sections():
        if section != 'build-args':
            config.update(config_file[section])

    if config_file.has_section('build-args'):
        config['build_args'] = config_file['build-args']

    informed_args = {key: value for key, value in vars(args).items() if value}

    config.update(informed_args)

    return BuilderConfig(**config)


def build(args: Namespace) -> None:
    print('doimbu - Docker Image Builder\n')

    variants = get_variants_list(EXECUTION_DIR)
    if not variants:
        print('no variants dir found')
        print('create a variant dir following the pattern:')
        print('  [CURRENT_DIR]/variants/[YOUR_VARIANT]/Dockerfile')
        return None

    config_file = get_file_config(BUILDER_CONFIG_PATH, variants)

    build_config = get_builder_config(EXECUTION_DIR, config_file, args)

    build_plan = generate_build_plan(build_config, variants)

    print('build plan:')
    for command in build_plan:
        print(command)

    if args.dry_run:
        print('\ndry run - skipping execution')
    else:
        print('\nexecuting builds..')
        for command in build_plan:
            subprocess.run(command, shell=True)
        print('builds completed')
