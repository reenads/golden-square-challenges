from lib.greet import *

def test_greet():
    result = greet("Rita")
    assert result == "Hello, Rita"