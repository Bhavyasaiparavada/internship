try:
    numerator = float(input("Enter a numerator: "))
    denominator = float(input("Enter a denominator: "))
    print("Result:", numerator / denominator)
except ValueError:
    print("The input must be numeric.")
except TypeError:
    print("The values must have compatible types.")
except ZeroDivisionError:
    print("A number cannot be divided by zero.")