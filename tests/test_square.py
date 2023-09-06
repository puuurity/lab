from ..square import Square
import pytest

def test_square_S():
    assert Square(2).S() == 4
    assert Square(10).S() == 100
    assert Square(55).S() == 3025

def test_square_P():
    assert Square(2).P() == 8
    assert Square(10).P() == 40
    assert Square(55).P() == 220

def test_square_wrong_parameter():
    with pytest.raises(ValueError):
        Square(-1)

    with pytest.raises(ValueError):
        Square("25")
