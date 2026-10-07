from lib.high_value import *

def test_returns_first_value_first_if_higher():
    highvalue = HighValue(9, 3)
    assert highvalue.get_highest() == "First value is higher"

def test_returns_second_value_is_higher():
    highvalue = HighValue(3, 9)
    assert highvalue.get_highest() == "Second value is higher"

def test_values_when_equal():
    highvalue = HighValue(5, 5)
    assert highvalue.get_highest() == "Values are equal"


