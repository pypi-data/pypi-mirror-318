from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent
DOCKER_IMAGE_VARIANTS_DIR = ROOT_DIR / 'variants'
LOG_PATH = Path(__file__).parent.parent / 'build_output.log'
BUILDER_CONFIG_FILE = 'doimbu.ini'
BUILDER_CONFIG_PATH = ROOT_DIR / BUILDER_CONFIG_FILE