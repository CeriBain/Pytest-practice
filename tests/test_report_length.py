from lib.report_length import *

def test_return_correct_length():
    result = report_length("mouse")
    assert result == "This string was 5 characters long."
    
def test_return_0_for_0_length_string():
    result = report_length("")
    assert result == "This string was 0 characters long."
    
def test_spaces_count():
    result = report_length("   ")
    assert result == "This string was 3 characters long."
