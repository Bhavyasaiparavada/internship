try:
    numerator = float(input("Enter a numerator: "))
    denominator = float(input("Enter a denominator: "))
    print("Result:", numerator / denominator)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("A number cannot be divided by zero.")