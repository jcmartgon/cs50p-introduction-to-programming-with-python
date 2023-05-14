# Jesus Carlos Martinez Gonzalez
# 12/05/2023
# Little Professor

# Math teacher for kids!

from random import randint


def main():
    score = 0

    n = get_level()

    # Plays the match (10 rounds)
    for i in range(10):
        op1, op2, result = generate_addition(n)

        score += play_round(op1, op2, result)

    print(f'{score}')


def get_level():
    """Returns an int between 1 and 3 (inclusive)"""
    while True:
        # Gets int
        try:
            n = int(input("Level: "))
        except ValueError:
            continue

        # Makes sure its a valid int
        if n in [1, 2, 3]:
            break

    return n


def generate_integer(level):
    """Returns an integer of 'level' digits"""

    if level not in [1, 2, 3]:
        raise ValueError("ERROR: Level must be either 1, 2, or 3.")

    # 1-digit integer
    if level == 1:
        return randint(0, 9)

    # 2-digit integer
    if level == 2:
        return randint(10, 99)

    # 3-digit integer
    return randint(100, 999)


def generate_addition(level):
    """
    Generates 2 'level'-digit integers
    Returns them and the result of their addition
    """
    op1 = generate_integer(level)
    op2 = generate_integer(level)
    result = op1 + op2
    return op1, op2, result


def play_round(op1, op2, result):
    """
    1 round of the match
    3 chances
    """

    chances = 3

    while True:

        # Get an int as a guess
        try:
            guess = int(input(f"{op1} + {op2} = "))
        except:
            continue

        # Correct guess
        if guess == result:
            return 1

        # Incorrect guess
        print("EEE")
        chances -= 1

        # Ran out of chances
        if chances == 0:
            print(result)
            return 0


if __name__ == "__main__":
    main()