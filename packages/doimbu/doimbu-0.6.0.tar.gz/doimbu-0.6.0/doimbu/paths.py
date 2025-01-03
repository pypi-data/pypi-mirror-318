from pathlib import Path


EXECUTION_DIR = Path().cwd()

BUILDER_CONFIG_FILE = 'doimbu.ini'
BUILDER_CONFIG_PATH = EXECUTION_DIR / BUILDER_CONFIG_FILE
DOCKER_IMAGE_VARIANTS_DIR = EXECUTION_DIR / 'variants'
LOG_PATH = EXECUTION_DIR / 'build_output.log'

ROOT_DIR = Path(__file__).parent.parent

PYPROJECT_TOML_PATH = ROOT_DIR / 'pyproject.toml'
