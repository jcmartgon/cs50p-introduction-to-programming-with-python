# Jesus Carlos Martinez Gonzalez
# 16/05/2023
# Testing my Twitter

# Testing-oriented remake of twttr.py (week2)


def main():
    text = input("Text: ")
    print(shorten(text))


def shorten(word):
    """Receives a string 'word' and returns it without vowels"""
    vowels = ['a', 'e', 'i', 'o', 'u']

    new = ""
    for char in word:
        if char.lower() not in vowels:
            new += char
    return new


if __name__ == "__main__":
    main()