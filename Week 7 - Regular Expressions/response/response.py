# Jesus Carlos Martinez Gonzalez
# 20/05/2023
# Response Validation

# Validates user's email

import validators


def main():
    if validators.email(input("What's your email address? ")):
        print('Valid')
    else:
        print('Invalid')


if __name__ == "__main__":
    main()