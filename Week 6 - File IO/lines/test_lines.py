# Jesus Carlos Martinez Gonzalez
# 18/05/2023
# Lines of Code

from lines import valid_py_file, count_loc
from pytest import raises


# Too few arguments
def test_few_args():
    with raises(SystemExit):
        valid_py_file(['lines.py'])


# Too many arguments
def test_many_args():
    with raises(SystemExit):
        valid_py_file(['lines.py', 'one', 'two'])


# Inexistent file
def test_file_not_found():
    with raises(SystemExit):
        valid_py_file(['lines.py', 'missing.py'])


# Not a python file
def test_not_py():
    with raises(SystemExit):
        valid_py_file(['lines.py', 'dummy.txt'])


# Proper usage
def test_proper_usage():
    assert valid_py_file(['lines.py', 'dummy.py']) == 'dummy.py'


# Counts LOC on a valid file
def test_counts_loc():
    assert count_loc('dummy.py') == 11
