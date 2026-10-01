try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    print("Result:", first / second)
except ZeroDivisionError:
    print("A number cannot be divided by zero.")