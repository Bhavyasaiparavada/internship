class InsufficientStockError(Exception):
    pass


stock = 8
try:
    quantity = int(input("How many items would you like? "))
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    if quantity > stock:
        raise InsufficientStockError("There is not enough stock.")
    print("Items left:", stock - quantity)
except ValueError as error:
    print("Invalid quantity:", error)
except InsufficientStockError as error:
    print(error)