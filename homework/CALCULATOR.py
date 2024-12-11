def addition(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def square(x):
    return x * x


def power(base, exp):
    return pow(base, exp)


def main():
    while True:
        print("1. add \n 2. subtract \n 3. multiply \n 4. divide \n 5. square \n 6. power \n 7. EXIT")
        option = int(input("Enter an option: "))
        if option == 1:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(addition(num1, num2))

        elif option == 2:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(subtract(num1, num2))

        elif option == 3:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(multiplication(num1, num2))

        elif option == 4:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(division(num1, num2))

        elif option == 5:
            num1 = int(input("Enter a first number: "))
            print(square(num1))

        elif option == 6:
            num1 = int(input("Enter the base: "))
            num2 = int(input("Enter the power: "))
            print(power(num1, num2))

        elif option == 7:
            break


if __name__ == "__main__":
    main()
