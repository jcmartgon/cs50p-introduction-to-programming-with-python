# Jesus Carlos Martinez Gonzalez
# 20/05/2023
# Watch on Youtube

# Turn a 12-hour formatted shift into a 24-hour formatted one

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """Prints s back as a 24-hour formatted string"""
    matches = re.fullmatch(
        r"(?P<start_h>\d?\d)(?::(?P<start_m>\d\d) | )(?P<start_md>AM|PM) to (?P<end_h>\d?\d)(?::(?P<end_m>\d\d) | )(?P<end_md>AM|PM)", s)

    # Wrong input format
    if not matches:
        raise ValueError("Wrong input format")

    # Assigns match groups to local variables
    start_h = matches.group('start_h')
    start_m = matches.group('start_m')
    start_md = matches.group('start_md')

    # Adds minutes if missing
    if start_m == None:
        start_m = '00'

    end_h = matches.group('end_h')
    end_m = matches.group('end_m')
    end_md = matches.group('end_md')

    # Adds minutes if missing
    if end_m == None:
        end_m = '00'

    # Validates time range
    if not valid_time(start_h, start_m):
        raise ValueError("Start time is not valid.")
    if not valid_time(end_h, end_m):
        raise ValueError("End time is not valid.")

    return f"{fix_time(start_h, start_m, start_md)} to {fix_time(end_h, end_m, end_md)}"


def valid_time(h, m):
    """Validates both the hour and minutes range"""
    if int(h) not in range(13) or int(m) not in range(60):
        return False
    return True


def fix_time(hour, mins, md):
    """Turns hour from 12-hours format to 24-hours"""
    hour = int(hour)

    # After mid-day but not 12 PM
    if md == 'PM' and hour != 12:
        hour = hour + 12

    if hour < 10:
        hour = f'0{str(hour)}'
    elif hour == 12 and md == 'AM':
        hour = '00'
    else:
        hour = str(hour)
    return f'{hour}:{mins}'


if __name__ == "__main__":
    main()