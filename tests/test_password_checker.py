import pytest
from lib.password_checker import *

def test_does_class_initialise():
    passwordchecker = PasswordChecker()
    password = passwordchecker.check("cheeesses")
    assert password 

def test_if_password_is_valid():
    passwordchecker = PasswordChecker()
    actual = passwordchecker.check("cheeseeee")
    expected = True
    assert actual == expected

def test_if_password_is_invalid():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as err:
        passwordchecker.check("chees")
    error_message = str(err.value)
    assert error_message == "Invalid password, must be 8+ characters."
