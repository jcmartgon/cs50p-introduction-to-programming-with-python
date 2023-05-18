# Jesus Carlos Martinez Gonzalez
# 16/05/2023
# Testing my Twitter

# Test cases for twttr.py

from twttr import shorten


# Test lowercase vowel replacement
def test_lower():
    assert shorten('hello') == 'hll'


# Test uppercase vowel replacement
def test_upper():
    assert shorten('HELLO') == 'HLL'


# Test numbers omition
def test_number():
    assert shorten('50') == '50'


# Test punctuation omition
def test_punct():
    assert shorten('!._?') == '!._?'