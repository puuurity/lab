from ..circle import Circle
import pytest

def test_circle_S():
    assert round(Circle(15).S(), 1) == 706.9
    assert round(Circle(1).S(), 1) == 3.1
    assert round(Circle(5).S(), 1) == 78.5

def test_circle_C():
    assert round(Circle(15).C(), 1) == 94.2
    assert round(Circle(1).C(), 1) == 6.3
    assert round(Circle(5).C(), 1) == 31.4

def test_circle_wrong_parameter():
    with pytest.raises(ValueError):
        Circle(-1)

    with pytest.raises(ValueError):
        Circle("24")
