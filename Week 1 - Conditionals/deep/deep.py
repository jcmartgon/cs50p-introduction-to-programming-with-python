# Jesus Carlos Martinez Gonzalez
# 09/05/2023
# Deep Thought


# Validate the user's answer

def main():
    ans = input("What's the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    if ans == '42' or ans == 'forty-two' or ans == 'forty two':
        print('Yes')
    else:
        print('No')


main()