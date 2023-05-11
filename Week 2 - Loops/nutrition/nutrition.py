# Jesus Carlos Martinez Gonzalez
# 10/05/2023
# Nutrition Facts


# Print calories of fruit, based on FDA's data
# Data: https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version

fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydrew": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80
}


def main():
    fruit = input("Fruit: ").title()
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")


if __name__ == "__main__":
    main()