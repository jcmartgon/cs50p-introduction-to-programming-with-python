# Jesus Carlos Martinez Gonzalez
# 18/05/2023
# Lines of Code

# Dummy file


def main():
    inpt = input("Test: ")

    print(useless(inpt))


def useless(s):
    """Returns s as is"""
    copy = ''
    for char in s:
        copy += char
    return s


if __name__ == "__main__":
    main()