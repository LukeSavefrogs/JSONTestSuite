import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
PARSERS_DIR = os.path.join(BASE_DIR, "parsers")
TEST_CASES_DIR_PATH = os.path.join(BASE_DIR, "test_parsing")
LOGS_DIR_PATH = os.path.join(BASE_DIR, "results")
LOG_FILENAME = "logs.txt"
LOG_FILE_PATH = os.path.join(LOGS_DIR_PATH, LOG_FILENAME)

INVALID_BINARY_FORMAT = 8
BAD_CPU_TYPE = 86