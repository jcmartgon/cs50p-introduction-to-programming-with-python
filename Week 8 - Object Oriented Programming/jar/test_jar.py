# Jesus Carlos Martinez Gonzalez
# 24/05/2023
# Cookie Jar

from jar import Jar
from pytest import raises


# No arguments
def test_no_arg():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


# Non-numeric capacity
def test_wrong_arg0():
    with raises(ValueError):
        jar = Jar("test")


# Non-positive capacity
def test_wron_arg1():
    with raises(ValueError):
        jar = Jar(0)


# Proper usage
def test_arg():
    jar = Jar(5)
    assert jar.capacity == 5


# Add cookies
def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5


# Take cookies
def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2


# Print cookies
def test_str(capsys):
    jar = Jar(5)
    jar.deposit(3)
    print(jar)
    capture = capsys.readouterr()
    assert capture.out == "🍪🍪🍪\n"