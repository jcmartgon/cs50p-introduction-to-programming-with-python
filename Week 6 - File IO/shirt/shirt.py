# Jesus Carlos Martinez Gonzalez
# 18/05/2023
# CS50 P-Shirt

# Modifies an input image into an output one

import sys
import os

import csv

from PIL import Image, ImageOps


def main():
    # Validates proper amount of command-line arguments (3)
    args = len(sys.argv)
    if args < 3:
        sys.exit("ERROR: Too few command-line arguments")
    if args > 3:
        sys.exit("ERROR: Too many command-line arguments")

    # Validate image files
    input, output = valid_img_files(sys.argv)

    shirtify(input, output)


def valid_img_files(argv):
    """Validates both image files"""
    input = argv[1]
    output = argv[2]

    # Validates input exists
    if not os.path.isfile(input):
        sys.exit("ERROR: Input file does not exist")

    # Validates file extensions
    ext1 = input.split('.')[-1].lower()
    ext2 = output.split('.')[-1].lower()

    if ext1 not in ['jpg', 'jpeg', 'png']:
        sys.exit("ERROR: Input file is not an image")
    if ext2 not in ['jpg', 'jpeg', 'png']:
        sys.exit("ERROR: Output file's format is not a valid image one")
    if ext1 != ext2:
        sys.exit("ERROR: Image formats aren't compatible, must be the same")

    # Valid files
    return input, output


def shirtify(input, output):
    """Superimposes a shirt on input and saves it at output"""
    with Image.open(input) as base:
        shirt = Image.open('shirt.png')
        size = shirt.size

        image = ImageOps.fit(base, size)
        image.paste(shirt, shirt)
        image.save(output)


if __name__ == '__main__':
    main()