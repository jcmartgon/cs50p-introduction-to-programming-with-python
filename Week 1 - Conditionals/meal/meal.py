# Jesus Carlos Martinez Gonzalez
# 09/05/2023
# Meal Time


# Inform the user whether its breakfast, lunch, or dinner time

def main():
    time = input("Time: ")

    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    """Convers time into an appropriate float value"""

    #Separate the hour and minutes elements from time
    hour, mins = time.split(':')
    hour = float(hour)

    # Is time in the 12-hour format?
    twelve_h = mins.find(' ')
    if twelve_h != -1:

        # Is it am or pm?
        ampm = mins[twelve_h + 1:]
        mins = mins[0:twelve_h]

        # If its pm and the hour isn't 12, add 12 to it
        if ampm == 'p.m.' and hour != 12.0:
            hour += 12

    # Re-scales minutes to fit between 0 and 1
    mins = float(mins) / 60
    return (hour + mins)


if __name__ == "__main__":
    main()