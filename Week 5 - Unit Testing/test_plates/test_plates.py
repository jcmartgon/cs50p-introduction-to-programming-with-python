# Jesus Carlos Martinez Gonzalez
# 17/05/2023
# Re-requesting a Vanity Plate

from plates import is_valid


# String too short
def test_short():
    assert is_valid('a') == False


# String too large
def test_long():
    assert is_valid('abcdefg') == False


# Proper string size
def test_good_size():
    assert is_valid('abcdef') == True


# Numbers amongst the first two characters
def test_first_two_numbers():
    assert is_valid('123456') == False


# Letters after numbers
def test_mixed():
    assert is_valid('ab12ef') == False


# Numbers only after letters
def test_letters_first():
    assert is_valid('ab1234') == True
    assert is_valid('abcde1') == True


# 0 is the first number to appear
def test_0_first():
    assert is_valid('abcd01') == False


# Punctuation
def test_punct():
    assert is_valid('ab,.!?') == False
    assert is_valid('abc12!') == False