import pytest
from lib.present import *


def test_we_wrap_and_then_unwrap_a_present():
    present = Present()
    present.wrap(3)
    assert present.unwrap() == 3

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."
#is a present already wrapped?

def test_present_already_wrapped():
    present = Present()
    present.wrap(5)
    with pytest.raises(Exception) as err:
        present.wrap(5)
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

def test_wrapped_present_remains_wrapped():
    present = Present()
    present.wrap(5)
    with pytest.raises(Exception) as err:
        present.wrap(55)
    assert present.unwrap() == 5


#is a present unwrapped?