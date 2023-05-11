# Jesus Carlos Martinez Gonzalez
# 11/05/2023
# Outdated


# Turn a middle-endian date into an ISO-8601 one

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


def main():
    while True:
        date = input("Date: ").strip()
        date = valid_date(date)
        if date:
            print(date)
            break


def valid_date(date):
    """
    Gets a middle-endian date(month/day/year) and returns an ISO-8601(year-month-day) one

    Supports the following formats:
    - ##/##/####
    - #/#/####
    - ##/#/####
    - #/##/####
    - month #, year
    - month ##, year
    """
    try:
        month, day, year = date.split('/')
    except:
        try:
            month, day, year = date.split(' ')
        except:
            return 0
        if date.find(',') == -1:
            return 0

        # Day validation
        try:
            day = day.split(',')[0]
        except:
            return 0
        try:
            day = int(day)
        except:
            return 0
        if 1 <= day <= 31:

            # Day formatting
            if day < 10:
                day = '0' + str(day)
            else:
                day = str(day)
        else:
            return 0

        # Month validation
        try:
            month = months[month]
        except:
            return 0
        if 1 <= month <= 12:

            # Month formatting
            if month < 10:
                month = '0' + str(month)
            else:
                month = str(month)

            # Returns date
            return f"{year}-{month}-{day}"
        else:
            return 0

    # Day validation
    try:
        day = int(day)
    except:
        return 0
    if 1 <= day <= 31:

        # Day formatting
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
    else:
        return 0

    # Month validation
    try:
        month = int(month)
    except:
        return 0
    if 1 <= month <= 12:
        if month < 10:

            # Month formatting
            month = '0' + str(month)
        else:
            month = str(month)

        # Return date
        return f"{year}-{month}-{day}"
    else:
        return 0


if __name__ == '__main__':
    main()