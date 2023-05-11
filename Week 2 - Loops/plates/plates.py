# Jesus Carlos Martinez Gonzalez
# 10/05/2023
# Vanity Plates


'''
Vanity plates validator

Rules:

- Length must be between 2 and 6 characters
- Only letters and numbers allowed
- First 2 letters must be letters
- The first number to appear can't be a 0
- No letter may appear after a number
'''


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Validates s according to the rules above
    """
    nums = False  # Numbers flag
    if 2 <= len(s) <= 6:  # Length validation
        for char in s:
            if not char.isalnum():  # Only letters and numbers allowed
                return False
            if char.isalpha() and nums:  # No letters after numbers
                return False
            if not nums and char == '0':  # A 0 can't be the first number to appear
                return False
            if char.isdigit():  # A number has appeared
                nums = True
        return True
    return False


if __name__ == "__main__":
    main()