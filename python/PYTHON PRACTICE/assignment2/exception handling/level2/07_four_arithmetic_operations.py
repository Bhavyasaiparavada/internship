try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
except ValueError:
    print("Please enter valid numbers.")
else:
    print("Addition:", first + second)
    print("Subtraction:", first - second)
    print("Multiplication:", first * second)
    try:
        print("Division:", first / second)
    except ZeroDivisionError:
        print("Division is not possible with zero as the second number.")