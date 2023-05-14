# Jesus Carlos Martinez Gonzalez
# 11/05/2023
# Emojize


# Request an emoji code from user and print it as an emoji

import emoji


def main():
    emj = input("Emoji: ")
    print(emoji.emojize(f'{emj}'))


if __name__ == '__main__':
    main()