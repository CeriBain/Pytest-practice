from lib.check_codeword import *

def test_return_string_if_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."
    
def test_starting_char_is_h_but_isnt_horse():
    result = check_codeword("hair")
    assert result != "Correct! Come in."
    
def test_returns_wrong_if_not_close():
    result = check_codeword("dogfish")
    assert result == "WRONG!"
    
    
    
    
    