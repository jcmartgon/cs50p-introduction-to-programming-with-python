# Jesus Carlos Martinez Gonzalez
# 19/05/2023
# NUMB3RS

from numb3rs import validate


# Too few bytes
def test_few_bytes():
    assert validate('0.0.0') == False


# Too many bytes
def test_many_bytes():
    assert validate('0.0.0.0.0') == False


# 4 bytes with the wrong format
def test_wrong_format():
    assert validate('0_0_0_0') == False
    assert validate('0/0/0/0') == False
    assert validate('0,0,0,0') == False
    assert validate('0. 0. 0. 0') == False


# Any of the bytes is out of range
def test_out_range():
    assert validate('-1.0.0.0') == False
    assert validate('0.-1.0.0') == False
    assert validate('0.0.-1.0') == False
    assert validate('0.0.0.-1') == False

    assert validate('256.0.0.0') == False
    assert validate('0.256.0.0') == False
    assert validate('0.0.256.0') == False
    assert validate('0.0.0.256') == False


# Valid IP
def test_valid_ip():
    assert validate('0.0.0.0') == True
    assert validate('255.255.255.255') == True