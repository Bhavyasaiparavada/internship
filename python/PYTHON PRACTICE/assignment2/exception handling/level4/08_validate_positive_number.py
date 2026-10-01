try:
    number = float(input("Enter a positive number: "))
    if number <= 0:
        raise ValueError("Number must be greater than zero.")
    print("Number accepted:", number)
except ValueError as error:
    print("Invalid number:", error)