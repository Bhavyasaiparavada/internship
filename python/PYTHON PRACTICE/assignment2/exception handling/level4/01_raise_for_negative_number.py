try:
    number = float(input("Enter a number: "))
    if number < 0:
        raise ValueError("The number cannot be negative.")
    print("Number:", number)
except ValueError as error:
    print("Invalid number:", error)