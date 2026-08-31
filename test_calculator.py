import pytest

from calculator import calculate


def test_add():
    assert calculate(2, "+", 3) == 5


def test_subtract():
    assert calculate(5, "-", 3) == 2


def test_multiply():
    assert calculate(4, "*", 3) == 12


def test_divide():
    assert calculate(9, "/", 3) == 3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(1, "/", 0)


def test_unknown_operation():
    with pytest.raises(ValueError):
        calculate(1, "%", 2)
