from lib.check_codeword import *

def test_checking_for_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_checking_for_wrong():
    result = check_codeword("cheese")
    assert result == "WRONG!"

def test_checking_for_nearly():
    result = check_codeword("hare")
    assert result == "Close, but nope."