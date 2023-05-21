# Jesus Carlos Martinez Gonzalez
# 20/05/2023
# Working 9 to 5

from working import convert, fix_time, valid_time
from pytest import raises


# Hour out of range
def test_invalid_hour():
    assert valid_time('-1', '00') == False
    assert valid_time('13', '00') == False


def test_invalid_hour_2():
    with raises(ValueError):
        convert("13 AM to 5 PM")


# Minutes our of range
def test_invalid_mins():
    assert valid_time('00', '-1') == False
    assert valid_time('00', '60') == False


def test_invalid_mins_2():
    with raises(ValueError):
        convert("9 AM to 4:60 PM")


# Valid time
def test_valid_time():
    assert valid_time('00', '00') == True
    assert valid_time('12', '59') == True


# Time reformatting
def test_fix_time():
    assert fix_time('12', '00', 'AM') == '00:00'
    assert fix_time('11', '59', 'AM') == '11:59'
    assert fix_time('12', '00', 'PM') == '12:00'
    assert fix_time('11', '59', 'PM') == '23:59'
    assert fix_time('9', '00', 'AM') == '09:00'


# Wrong input format
def test_wrong_format():
    with raises(ValueError):
        convert('From 9 AM to 5 PM')


def test_wrong_format_2():
    with raises(ValueError):
        convert('9 AM - 5 PM')


# Proper usage
def test_proper():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 PM to 5 AM') == '21:00 to 05:00'