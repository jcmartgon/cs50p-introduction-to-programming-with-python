# Jesus Carlos Martinez Gonzalez
# 09/05/2023
# Math Interpreter


# Simulate a simple calculator (+, -, *, /)

def main():
    op = input("Input: ")

    x, y, z = op.split(' ')

    match y:
        case '+':
            print(f'{(float(x) + float(z)):.1f}')
        case '-':
            print(f'{(float(x) - float(z)):.1f}')
        case '*':
            print(f'{(float(x) * float(z)):.1f}')
        case '/':
            print(f'{(float(x) / float(z)):.1f}')


main()