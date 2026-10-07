from lib.string_builder import *

def test_adds_string():
    string = StringBuilder()
    string.add("snake")
    result = string.output()
    assert result == "snake"
    

def test_adding_a_string_sets_size_to_that_strings_size():
    string = StringBuilder()
    string.add("hello")
    assert string.size() == 5

def test_adding_multiple_strings_outputs_multiple():
    string = StringBuilder()
    string.add("hello")
    string.add("snake")
    string.add("rabbit")
    result = string.output()
    assert result == "hellosnakerabbit"


