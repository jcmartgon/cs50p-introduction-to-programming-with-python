# Jesus Carlos Martinez Gonzalez
# 10/05/2023
# Just setting up my twttr


# Remove vowels from text

def main():
    text = input("Text: ")
    vowels = ['a', 'e', 'i', 'o', 'u']

    new = ""
    for char in text:
        if char.lower() not in vowels:
            new += char
    print(new)


if __name__ == "__main__":
    main()