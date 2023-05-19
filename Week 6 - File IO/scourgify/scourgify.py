# Jesus Carlos Martinez Gonzalez
# 18/05/2023
# Scourgify

# Cleans an input csv file into an output one

import sys
import os

import csv


def main():
    # Validates proper amount of command-line arguments (3)
    args = len(sys.argv)
    if args < 3:
        sys.exit("Too few command-line arguments")
    if args > 3:
        sys.exit("Too many command-line arguments")

    # Validate csv file
    f = valid_csv_file(sys.argv)

    scourgify(f, sys.argv[2])


def valid_csv_file(argv):
    """Validates a csv file passed as a command-line argument"""
    f = argv[1]

    # Validates file exists
    if not os.path.isfile(f):
        sys.exit("File does not exist")

    # Validates file extension
    if f.split('.')[-1] != 'csv':
        sys.exit(f"Not a .csv file")

    # Valid file
    return f


def scourgify(before, after):
    """Cleans up a csv file"""

    # Storage
    students = []

    # Origin file
    with open(before, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row['name'].replace('"', '').split(',')
            first = first.strip()
            students.append({'first': first, 'last': last, 'house': row['house']})

    # Destination file
    with open(after, 'w') as file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Re-formats before into after
        writer.writeheader()
        for student in students:
            writer.writerow({'first': student['first'], 'last': student['last'], 'house': student['house']})


if __name__ == '__main__':
    main()