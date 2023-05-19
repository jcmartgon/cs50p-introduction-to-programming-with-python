# Jesus Carlos Martinez Gonzalez
# 18/05/2023
# Lines of Code

# Count lines of code (LOC) in a file

import sys
import os


def main():
    f = valid_py_file(sys.argv)

    print(count_loc(f))


def valid_py_file(argv):
    """Validates a python file passed as a command-line argument"""

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

    # Validates file is a python one
    if f.split('.')[-1] != 'py':
        sys.exit("Not a Python file")

    # Valid python file
    return f


def count_loc(s):
    """Counts LOC in a file"""
    locs = 0

    with open(s, 'r') as file:
        for row in file:
            row = row.lstrip()

            # If its not an empty line
            if len(row) != 0:

                # If its not a comment (docstrings allowed)
                if not row.startswith('#'):
                    locs += 1
    return locs


if __name__ == '__main__':
    main()