# Jesus Carlos Martinez Gonzalez
# 10/05/2023
# Coke Machine


# Simulate a coke vending machine
# Only accepts 5, 10, and 25 cents

def main():
    cost = 50

    # As long as the cost hasn't been covered...
    while cost > 0:
        coin = int(input("Insert Coin: "))

        # Ignore wrong amounts
        if coin not in [5, 10, 25]:
            coin = 0
            
        cost -= coin
        if cost > 0:
            print(f"Amount Due: {cost}")
    print(f"Change Owed: {cost * -1}")


if __name__ == "__main__":
    main()