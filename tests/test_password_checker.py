import pytest 
from lib.password_checker import *

def test_returns_true_for_correct_length_password():
    password = PasswordChecker()
    result = password.check("hellooooo")
    assert result == True

def test_if_not_correct_length_equals_error():
    password = PasswordChecker()
    with pytest.raises(Exception) as error:
        password.check("shr")
    assert str(error.value) == "Invalid password, must be 8+ characters."
    
def test_empty_password_gives_error():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("")
    assert str(e.value) == "Invalid password, must be 8+ characters."


