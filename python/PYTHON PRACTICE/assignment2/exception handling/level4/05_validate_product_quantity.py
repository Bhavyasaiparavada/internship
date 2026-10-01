try:
    quantity = int(input("Enter product quantity: "))
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    print("Quantity:", quantity)
except ValueError as error:
    print("Invalid quantity:", error)