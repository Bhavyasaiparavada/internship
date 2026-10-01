class Product:
    def __init__(self, price):
        self.price = price

    def total_price(self, quantity):
        return self.price * quantity


product = Product(25)
print("Total price:", product.total_price(4))