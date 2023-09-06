from ..rectangle import Rectange
import pytest

def test_rectangle_S():
    assert Rectange(2, 10).S() == 20
    assert Rectange(10, 15).S() == 150
    assert Rectange(1, 3).S() == 3

def test_rectangle_P():
    assert Rectange(2, 10).P() == 24
    assert Rectange(10, 15).P() == 50
    assert Rectange(1, 3).P() == 8

def test_rectangle_wrong_parameter():
    with pytest.raises(ValueError):
        Rectange(1, -1)

    with pytest.raises(ValueError):
        Rectange("24", 24)
