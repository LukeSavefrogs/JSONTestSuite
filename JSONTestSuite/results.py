from enum import Enum, auto

class TestResults(Enum):
    """ Enum containing all the possible results of a test. """
    SHOULD_HAVE_FAILED = auto()
    SHOULD_HAVE_PASSED = auto()
    CRASH = auto()
    IMPLEMENTATION_FAIL = auto()
    IMPLEMENTATION_PASS = auto()
    TIMEOUT = auto()
