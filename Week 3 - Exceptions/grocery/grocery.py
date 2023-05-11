# Jesus Carlos Martinez Gonzalez
# 11/05/2023
# Grocery List


'''
Get grocery items from user
Print the list ordered alphabetically by keys and uppercased like:

Quantity Item
'''


def main():
    list = {}

    # Get item(s) from user
    while True:
        try:
            item = input()
        except EOFError:
            print()
            break
        else:
            if item in list:
                list[item] += 1
            else:
                list[item] = 1

    # Sort the dictionary 'list' alphabeticaly by key
    list = sort_dict_keys(list)

    # Print items
    for item in list:
        print(f"{list[item]} {item.upper()}")


def sort_dict_keys(dict):
    """Sorts a dictionary by keys"""
    keys = list(dict.keys())
    keys.sort()
    sorted_dict = {i: dict[i] for i in keys}
    return sorted_dict


if __name__ == "__main__":
    main()