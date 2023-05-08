# Jesus Carlos Martinez Gonzalez
# 08/05/2023
# Einstein


# Get mass from user and output energy based on Einstein's relativity's theory
# E = mc^2

def main():
    c = 300000000
    mass = int(input("Mass: "))
    print(mass * pow(c, 2))


main()