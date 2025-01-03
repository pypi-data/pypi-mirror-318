from configparser import ConfigParser
from pathlib import Path

from doimbu.version import Version
from doimbu.sources.git import get_latest_git_version_tag


def create_file_config(
        default_variant: str,
        version: Version | None = None,
        tag_namespace: str | None = None,
        tag_repository: str | None = None,
        build_args: dict[str, str] | None = None,
        only_default_variant: bool = False,
        tag_omit_latest: bool = False,
        dry_run: bool = False) -> ConfigParser:
    """Create the configurations that will be saved on the file system.

    It's a different concept from the BuilderConfig class.
    The BuilderConfig class represents the runtime configuration, that merges
    the configuration present on the file config(created by this function),
    command line parameters, git tags and file system directory structure
    (variants).
    """
    config = ConfigParser()

    _add_mandatory_config_items(
        config, default_variant=default_variant, version=version)

    tag_section = {
        'tag_namespace': tag_namespace,
        'tag_repository': tag_repository
    }
    tag_section = {key: value for key, value in tag_section.items()
                   if value is not None}
    if tag_section:
        config['tag'].update(tag_section)

    if build_args is not None:
        config['build-args'] = build_args

    if any({only_default_variant, tag_omit_latest, dry_run}):
        execution_mode_section = {
            'only_default_variant': only_default_variant,
            'tag_omit_latest': tag_omit_latest,
            'dry_run': dry_run
        }
        execution_mode_section = {
            key: str(value) for key, value in execution_mode_section.items()
            if value is not None
        }
        if execution_mode_section:
            config['execution-mode'] = execution_mode_section

    return config


def _has_mandatory_config_items(config: ConfigParser) -> bool:
    has_default_variant = False
    if config.has_section('doimbu'):
        has_default_variant = (
                config['doimbu'].get('default_variant') is not None)

    has_tag_version = False
    if config.has_section('tag'):
        has_tag_version = config['tag'].get('version') is not None

    return all({has_default_variant, has_tag_version})


def _add_mandatory_config_items(
        config: ConfigParser,
        default_variant: str,
        version: Version | None = None) -> None:
    if not config.has_section('doimbu'):
        config.add_section('doimbu')

    config['doimbu'].update({'default_variant': default_variant})

    if not config.has_section('tag'):
        config.add_section('tag')

    version = version if version else get_latest_git_version_tag()

    config['tag'].update({'version': version.version})


def get_file_config(config_path: Path, variants: list[str]) -> ConfigParser:
    if not config_path.is_file():
        write_file_config(config_path, default_variant=variants[0])

    config = ConfigParser()
    config.read(config_path)

    if not _has_mandatory_config_items(config):
        _add_mandatory_config_items(config, default_variant=variants[0])

    return config


def write_file_config(
        config_path: Path,
        default_variant: str,
        version: Version | None = None,
        tag_namespace: str | None = None,
        tag_repository: str | None = None,
        build_args: dict[str, str] | None = None,
        only_default_variant: bool = False,
        tag_omit_latest: bool = False,
        dry_run: bool = False) -> None:
    config = create_file_config(
        default_variant,
        version,
        tag_namespace,
        tag_repository,
        build_args,
        only_default_variant,
        tag_omit_latest,
        dry_run)

    with config_path.open('w') as f:
        config.write(f)
