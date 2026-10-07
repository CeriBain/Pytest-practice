import pytest
from lib.present import *


def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."




def test_wrapping_already_wrapped():
    present = Present()
    present.wrap(28)
    with pytest.raises(Exception) as e:
        present.wrap(14)
    message = str(e.value)
    assert message == "A contents has already been wrapped."




def test_wrapping_already_wrapped_preserves_values():
    present = Present()
    present.wrap(50)
    with pytest.raises(Exception) as e:
        present.wrap(77)
    assert present.unwrap() == 50
        
