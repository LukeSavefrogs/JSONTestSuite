from enum import Enum, auto

class TestResults(Enum):
    """ Enum containing all the possible results of a test. """
    
    CRASH = auto()
    """ Parsing crashed.
    
    Thise is the most serious issue, since parsing an uncontrolled
    input may put the whole process at risk. 
    """

    SHOULD_HAVE_PASSED = auto()
    """ Parsing should have succeeded but failed. 
    
    This error is also very dangerous, because an uncontrolled input 
    may prevent the parser to parse a whole document.
    """
    
    SHOULD_HAVE_FAILED = auto()
    """ Parsing should have failed but succeeded.
    
    This may indicate a JSON "extension" that can be parsed.
    Everything will work fine, until the parser is replaced with 
    another parser which does not parse the same "extensions"...
    """

    IMPLEMENTATION_FAIL = auto()
    IMPLEMENTATION_PASS = auto()
    
    TIMEOUT = auto()
    """ Parsing timed out. """
