# Jesus Carlos Martinez Gonzalez
# 20/05/2023
# Regular, um, Expressions

# Prints amount of occurances of 'um' in user's input

import re


def main():
    print(count(input("Text: ")))


def count(s):
    """returns 'um' occurrances on s"""
    matches = re.findall(r'(?<!\w)um(?!\w)', s, flags=re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()