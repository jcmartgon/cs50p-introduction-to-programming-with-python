# Jesus Carlos Martinez Gonzalez
# 09/05/2023
# Bank


# Grade user's greeting

def main():
    greeting = input("Greeting: ").strip().lower()[0:5]

    if greeting == "hello":
        score = 0
    elif greeting[0] == "h":
        score = 20
    else:
        score = 100

    print(f'${score}')


main()