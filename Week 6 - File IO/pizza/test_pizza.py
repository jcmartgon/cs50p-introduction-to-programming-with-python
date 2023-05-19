# Jesus Carlos Martinez Gonzalez
# 18/05/2023
# Pizza Py

from pizza import valid_csv_file, csv_to_table
from pytest import raises


# Too few arguments
def test_few_args():
    with raises(SystemExit):
        valid_csv_file(['pizza.py'])


# Too many arguments
def test_many_args():
    with raises(SystemExit):
        valid_csv_file(['pizza.py', 'one', 'two'])


# Inexistent file
def test_file_not_found():
    with raises(SystemExit):
        valid_csv_file(['pizza.py', 'missing.py'])


# Not a python file
def test_not_py():
    with raises(SystemExit):
        valid_csv_file(['pizza.py', 'regular.txt'])


# Proper usage
def test_proper_usage():
    assert valid_csv_file(['pizza.py', 'regular.csv']) == 'regular.csv'


# Turns a csv into an ASCII table
def test_csv_to_table():
    assert csv_to_table('regular.csv') == '''+-----------------+---------+---------+
| Regular Pizza   | Small   | Large   |
+=================+=========+=========+
| Cheese          | $13.50  | $18.95  |
+-----------------+---------+---------+
| 1 topping       | $14.75  | $20.95  |
+-----------------+---------+---------+
| 2 toppings      | $15.95  | $22.95  |
+-----------------+---------+---------+
| 3 toppings      | $16.95  | $24.95  |
+-----------------+---------+---------+
| Special         | $18.50  | $26.95  |
+-----------------+---------+---------+'''