class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = [Product("Pen", 2), Product("Book", 5)]


cart = ShoppingCart()
for product in cart.products:
    print(product.name, product.price)
