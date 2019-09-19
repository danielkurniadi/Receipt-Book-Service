import os

# -------------------
#  PATH
# -------------------

PROJ_DIR = os.path.dirname(os.path.dirname(__file__))

# Testing
TEST_DIR = os.path.join(PROJ_DIR, 'tests/')
TEST_DATA_DIR = os.path.join(TEST_DIR, 'test_data/')
TEST_OUTPUT_DIR = os.path.join(TEST_DIR, 'test_output/')

TEST_IMG_DATA_DIR = os.path.join(TEST_DATA_DIR, 'img')
TEST_TEXT_DATA_DIR = os.path.join(TEST_DATA_DIR, 'text')

# Parser 
PARSER_YAML_PATH = os.path.join(PROJ_DIR, 'parser_config.yaml')
