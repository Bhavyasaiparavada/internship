def calculate_price(price, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    return price * quantity


try:
    price = float(input("Enter price per item: "))
    quantity = int(input("Enter quantity: "))
    print("Total price:", calculate_price(price, quantity))
except ValueError as error:
    print("Invalid input:", error)