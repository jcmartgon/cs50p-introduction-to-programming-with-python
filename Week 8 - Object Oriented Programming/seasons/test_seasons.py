# Jesus Carlos Martinez Gonzalez
# 24/05/2023
# Seasons of Love

from seasons import valid_date
import datetime


def test_wrong_format():
    assert valid_date("05-15-2000") == False
    assert valid_date("2000/05/15") == False
    assert valid_date("2000.05.15") == False
    assert valid_date("2000-5-15") == False
    assert valid_date("2000-05-5") == False


def test_invalid_month():
    assert valid_date("2000-00-15") == False
    assert valid_date("2000-13-15") == False


def test_invalid_day():
    assert valid_date("2000-05-0") == False
    assert valid_date("2000-05-32") == False


def test_valid_date():
    assert valid_date("2000-05-15") == datetime.datetime(2000, 5, 15, 0, 0, 0)