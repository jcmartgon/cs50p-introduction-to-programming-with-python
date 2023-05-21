# Jesus Carlos Martinez Gonzalez
# 19/05/2023
# Watch on Youtube

# Extract the youtube url from an HTML iframe element and return a shorter version of it

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """Extract youtube url from 's' and returns it shortened"""
    if url := re.search(r'src="https?:\/\/(?:www.)?youtube.com\/embed\/(.+?)"', s):
        return f'https://youtu.be/{url.groups(1)[0]}'


if __name__ == "__main__":
    main()