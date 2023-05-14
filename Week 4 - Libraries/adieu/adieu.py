# Jesus Carlos Martinez Gonzalez
# 11/05/2023
# Adieu, Adieu

# Gramatically correct farewell

import inflect


def main():

    p = inflect.engine()

    # Get names from user
    names = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            break
        names.append(name)

    # Turn the list into a gramatically correct string
    names_list = p.join(names)

    print(f"Adieu, adieu, to {names_list}")


if __name__ == '__main__':
    main()