from lib.add_five import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result ==8
    

def test_returns_10_for_5():
    result = add_five(5)
    assert result == 10
    
    