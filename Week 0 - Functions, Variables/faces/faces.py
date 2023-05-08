# Jesus Carlos Martinez Gonzalez
# 08/05/2023
# Faces


# Convert ':)' and ':(' into emojis on a given text

def main():
    text = input("Type anything: ")
    print(convert(text))


def convert(text):
    return text.replace(':)', '🙂').replace(':(', '🙁')


main()