from lib.gratitudes import *

def test_gratitudes_returns_empty_formatted_list_if_nothing_appended():
    gratitude = Gratitudes()
    result = gratitude.format()
    assert result == "Be grateful for: "



def test_appends_item_to_list():
    item = Gratitudes()
    item.add("happiness")
    result = item.format()
    assert result == "Be grateful for: happiness"



def test_returns_multiple_gratitiudes_in_the_list():
    item = Gratitudes()
    item.add("happiness")
    item.add("enjoyment")
    item.add("coding")
    result = item.format()
    assert result == "Be grateful for: happiness, enjoyment, coding"


def test_that_gratitiudes_is_a_list():
    item = Gratitudes()
    assert item.gratitudes == []



def test_duplicates_are_kept():
    item = Gratitudes()
    item.add("mouse")
    item.add("mouse")
    assert item.format() == "Be grateful for: mouse, mouse"

