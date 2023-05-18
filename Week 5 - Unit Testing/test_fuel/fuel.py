# Jesus Carlos Martinez Gonzalez
# 17/05/2023
# Refueling

'''
Get a fraction representing fuel level from user and print back percentage
- Percentage is 1% or lower (print E)
- Percentage is 99% or higher (print F)
'''


def main():
    fuel = input("Fuel: ")
    percentage = convert(fuel)
    print(gauge(percentage))


def convert(fraction):
    """Gets a string in x/y format and returns it as a percentage value"""

    # String is properly formatted
    try:
        x, y = fraction.split('/')
    except ValueError:
        raise ValueError

    # Both elements are ints
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError

    # ZeroDivision
    if y == 0:
        raise ZeroDivisionError

    # Improper fraction
    if x > y:
        raise ValueError

    prcnt = x / y
    return round(prcnt * 100)


def gauge(percentage):
    """Returns fuel value to display"""

    # Empty
    if percentage <= 1:
        return 'E'

    # Full
    elif percentage >= 99:
        return 'F'

    # Percentage
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()