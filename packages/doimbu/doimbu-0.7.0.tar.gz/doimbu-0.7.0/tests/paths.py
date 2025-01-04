from pathlib import Path
from doimbu.paths import BUILDER_CONFIG_FILE


ROOT_DIR = Path(__file__).parent.parent
TEST_ROOT_DIR = ROOT_DIR / 'tests'
TEST_TEMP_DIR = TEST_ROOT_DIR / 'temp'
TEST_BUILDER_CONFIG_PATH = TEST_TEMP_DIR / BUILDER_CONFIG_FILE
