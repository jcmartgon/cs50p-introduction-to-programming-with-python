# Jesus Carlos Martinez Gonzalez
# 19/05/2023
# NUMB3RS

'''
Validate an IPv4 address (kinda)

IP must follow the format: #.#.#.#
Where # must be between 0 and 255 (inclusive)
'''

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """Validates a given IP"""

    # Validates format
    if matches := re.fullmatch(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', ip):

        # Validates range of each byte on the address
        for match in matches.groups():
            if int(match) not in range(256):
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()