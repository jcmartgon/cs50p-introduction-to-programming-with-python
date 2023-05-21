# Jesus Carlos Martinez Gonzalez
# 20/05/2023
# Regular, um, Expressions

from um import count


# A single 'um'
def test_solo():
    assert count("um") == 1


# 'um' lost in a text
def test_buried():
    assert count("I don't know, um, what to say") == 1


# Multiple 'um's, different cases
def test_multi():
    assert count("Um, thanks, um...") == 2


# Um as part of a word
def test_therein():
    assert count("umbrella") == 0