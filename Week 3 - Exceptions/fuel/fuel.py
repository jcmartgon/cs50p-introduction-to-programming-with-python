# Jesus Carlos Martinez Gonzalez
# 11/05/2023
# Fuel Gauge

'''
Get a fraction representing fuel level from user and print back percentage
- Percentage is 1% or lower (print E)
- Percentage is 99% or higher (print F)
'''


def main():
    fuel = frac_to_dec("Fuel: ")
    fuel = round(fuel * 100)

    # Print appropriate value
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")


def frac_to_dec(prompt):
    """Ask user for a fraction and return it as decimal"""
    while True:
        frac = input(prompt)
        try:
            x, y = frac.split('/')
        except:
            print("ERROR: Please enter a fraction (x/y)")
        else:
            try:
                x = int(x)
                y = int(y)
            except ValueError:
                print("ERROR: Fraction elements must be integers")
            else:
                if x > y:
                    print("ERROR: Numerator must not be larger than denominator")
                    continue
                try:
                    return x / y
                except ZeroDivisionError:
                    print("ERROR: Denominator can't be 0")


if __name__ == "__main__":
    main()