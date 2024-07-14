
def calculator():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1/2/3/4): "))
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == 1:
        print(n1, "+", n2, "=", n1 + n2)

    elif choice == 2:
        print(n1, "-", n2, "=", n1 - n2)

    elif choice == 3:
        print(n1, "*", n2, "=", n1 * n2)

    elif choice == 4:
        if n2 != 0:
            print(n1, "/", n2, "=", n1 / n2)
        else:
            print("Error! ")
    else:
        print("Invalid choice.")

calculator()

