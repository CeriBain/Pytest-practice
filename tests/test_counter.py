from lib.counter import *

def test_adds_5_to_count():
    count = Counter()
    count.add(5)
    result = count.report()
    assert result == "Counted to 5 so far."

def test_add_10_to_count():
    count = Counter()
    count.add(10)
    result = count.report()
    assert result == "Counted to 10 so far."
    
def test_add_0_to_count():
    count = Counter()
    count.add(0)
    result = count.report()
    assert result == "Counted to 0 so far."
    
    
    
    
