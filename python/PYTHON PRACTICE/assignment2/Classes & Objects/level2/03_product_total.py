class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


products = [Product("Pen", 10, 5), Product("Book", 100, 2), Product("Bag", 800, 1)]
for product in products:
    print(product.name, "Total:", product.price * product.quantity)