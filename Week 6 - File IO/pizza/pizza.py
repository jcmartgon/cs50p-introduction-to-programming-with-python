# Jesus Carlos Martinez Gonzalez
# 18/05/2023
# Pizza Py

# Prints a pizza menu(csv) as ASCII art

import sys
import os

import csv
from tabulate import tabulate


def main():
    f = valid_csv_file(sys.argv)

    print(csv_to_table(f))


def valid_csv_file(argv):
    """Validates a csv file passed as a command-line argument"""

    # Validates proper amount of command-line arguments (2)
    args = len(argv)
    if args < 2:
        sys.exit("Too few command-line arguments")
    if args > 2:
        sys.exit("Too many command-line arguments")

    f = argv[1]

    # Validates file exists
    if not os.path.isfile(f):
        sys.exit("File does not exist")

    # Validates file extension
    if f.split('.')[-1] != 'csv':
        sys.exit(f"Not a .csv file")

    # Valid file
    return f


def csv_to_table(f):
    """Takes a csv file and returns it as an ASCII table"""
    with open(f, 'r') as file:
        reader = csv.reader(file)

        return tabulate(reader, headers='firstrow', tablefmt="grid")


if __name__ == '__main__':
    main()