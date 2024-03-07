import pytest
from ukp_template_2 import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from ukp_template_2 import Fibonacci
    except ImportError:
        assert False

##### YOUR CODE HERE #####

##########################