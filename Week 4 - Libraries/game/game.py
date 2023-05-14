# Jesus Carlos Martinez Gonzalez
# 11/05/2023
# Guessing Game

'''
- Promt the user for a positive integer 'n'
- Generate a random number between 1 and n
- Ask the user for a guess until they guess n, giving them hints based on their guess' size
'''

from random import randint


def main():

    # Get a valid n from user
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        if n >= 1:
            break

    # Generate random int between 1 and n (inclusive)
    rndm = randint(1, n)

    # Have the user guess n
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        if guess < 1:
            continue
        if guess < rndm:
            print("Too small!")
        elif guess > rndm:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == '__main__':
    main()