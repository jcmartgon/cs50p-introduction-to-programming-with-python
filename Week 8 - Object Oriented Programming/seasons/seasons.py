# Jesus Carlos Martinez Gonzalez
# 24/05/2023
# Seasons of Love

# Prints the difference in minutes between two dates as english words

import re
import sys
import datetime
import inflect


def main():
    # Get valid birthdate from user
    bday = input("Date of Birth: ")
    bday = valid_date(bday)
    if not bday:
        sys.exit("Invalid date")

    # Today
    today = datetime.date.today()
    today = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)

    # Time difference between today and the user's birthday, in minutes
    min_dif = today - bday
    min_dif = int(min_dif.total_seconds() // 60)

    # Inflect object
    p = inflect.engine()

    print(p.number_to_words(min_dif).replace(" and ", " ").capitalize() + " minutes")


def valid_date(date):
    """Validates date"""

    # Validate format
    match = re.fullmatch(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", date)
    if not match:
        return False

    # Validate month and day
    try:
        dt = datetime.datetime(
            int(match.group("year")),
            int(match.group("month")),
            int(match.group("day")),
            0,
            0,
            0,
        )
    except ValueError:
        return False

    return dt


if __name__ == "__main__":
    main()
