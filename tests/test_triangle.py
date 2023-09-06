from ..triangle import Triangle
import pytest

def test_triagnle_S():
    assert round(Triangle(5, 4, 6).S(), 1) == 9.9
    assert round(Triangle(16, 9, 23).S(), 1) == 53.7
    assert round(Triangle(109, 55, 66).S(), 1) == 1424.3

def test_triagnle_P():
    assert round(Triangle(5, 4, 6).P(), 1) == 15
    assert round(Triangle(16, 9, 23).P(), 1) == 48
    assert round(Triangle(109, 55, 66).P(), 1) == 230

def test_triagnle_wrong_parameter():
    with pytest.raises(ValueError):
        Triangle("12", 2, 3)

    with pytest.raises(ValueError):
        Triangle(3, 2, -3)

    with pytest.raises(ValueError):
        Triangle(3, -2, 3)

    with pytest.raises(ValueError):
        Triangle(1, 2, 6)
