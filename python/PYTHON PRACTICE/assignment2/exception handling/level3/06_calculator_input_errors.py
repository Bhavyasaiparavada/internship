try:
    first = float(input("Enter the first number: "))
    operator = input("Enter an operation (+, -, *, /): ")
    second = float(input("Enter the second number: "))

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        result = first / second
    else:
        raise ValueError("Unknown operation.")
except ValueError as error:
    print("Input error:", error)
except ZeroDivisionError:
    print("A number cannot be divided by zero.")
else:
    print("Result:", result)