# Guessing Game

## Problem Description

I’m thinking of a number between 1 and 100…

What is it?
In a file called game.py, implement a program that:

- Prompts the user for a level, If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and $n$, inclusive, using the random module.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
  - If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
  - If the guess is larger than that integer, the program should output Too large! and prompt the user again.
  - If the guess is the same as that integer, the program should output Just right! and exit.

## My solution

### Description

```python
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
```

## Output Expected

![OutputExpected](Resources/output_expected.png)

## Output Obtained

![As expected](Resources/output_obtained.png)

## Score

![All good](./Resources/score.png)

## Usage

1. Run 'python game.py' and follow the prompt.