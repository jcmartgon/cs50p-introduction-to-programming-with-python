# Jesus Carlos Martinez Gonzalez
# 16/05/2023
# Back to the Bank


from bank import value


# Hello as greeting
def test_hello():
    assert value('Hello, David') == 0


# hi as greeting
def test_h_():
    assert value('hi, David') == 20


# sup as greeting
def test_no_h_():
    assert value('sup, David') == 100