# Jesus Carlos Martinez Gonzalez
# 16/05/2023
# Back to the Bank

# Score user's greeting


def main():
    greeting = input("Greeting: ")

    print(f'${value(greeting)}')


def value(greeting):
    """ Return a score based on greeting"""
    greeting = greeting.strip().lower()[0:5]

    if greeting == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    return 100


if __name__ == "__main__":
    main()