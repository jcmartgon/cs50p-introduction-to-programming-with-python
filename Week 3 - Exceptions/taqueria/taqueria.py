# Jesus Carlos Martinez Gonzalez
# 11/05/2023
# Felipe's Taqueria


# Ask user for their order and print total cost

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0.0
    while (True):
        try:
            item = input("Item: ")
            item = item.title()  # Sets item to titlecase
            if item in menu:
                total += menu[item]
                print(f'${total:.2f}')

        # If user types ctrl + d
        except EOFError:
            print()
            break


if __name__ == "__main__":
    main()