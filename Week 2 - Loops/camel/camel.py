# Jesus Carlos Martinez Gonzalez
# 10/05/2023
# CamelCase


# Convert a text from camel case into snake case

def main():
    text = input("Text: ")
    print(snake_case(text))


def snake_case(text):
    """Returns text as snake case"""

    # Copy of text to return
    new = ""

    # Iterate over text, if char is uppercase,
    # append it as undercase following an underscore,
    # otherwise just append it
    for char in text:
        if char.isupper():
            new += f'_{char.lower()}'
        else:
            new += char
    return new


main()