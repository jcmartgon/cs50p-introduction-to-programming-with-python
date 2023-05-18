# Jesus Carlos Martinez Gonzalez
# 17/05/2023
# Refueling

from fuel import convert, gauge
from pytest import raises


# Proper fraction
def test_proper_fract():
    assert convert('1/2') == 50
    assert convert('4/5') == 80


# Improper fraction
def test_improper_fract():
    with raises(ValueError):
        convert('2/1')


# Zero Division
def test_zero_division():
    with raises(ZeroDivisionError):
        convert('5/0')


# Elements aren't ints
def test_not_nums():
    with raises(ValueError):
        convert('a/b')


# Tank is empty
def test_empty():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'


# Tank is full
def test_full():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'


# Tank isn't full but has got fuel
def test_prcnt():
    assert gauge(1.01) == '1.01%'
    assert gauge(50) == '50%'
    assert gauge(89.99) == '89.99%'