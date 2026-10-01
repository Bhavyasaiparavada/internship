try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = first / second
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("A number cannot be divided by zero.")
else:
    print("Result:", result)