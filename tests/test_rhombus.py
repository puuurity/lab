from ..rhombus import Rhombus
import pytest

def test_rhombus_S():
    assert Rhombus(15, 2).S() == 30
    assert Rhombus(45, 7).S() == 315
    assert Rhombus(18, 5).S() == 90

def test_rhombus_P():
    assert Rhombus(15, 2).P() == 60
    assert Rhombus(45, 7).P() == 180
    assert Rhombus(18, 5).P() == 72

def test_rhombus_wrong_parameter():
    with pytest.raises(ValueError):
        Rhombus(1, -1)

    with pytest.raises(ValueError):
        Rhombus("24", 24)
