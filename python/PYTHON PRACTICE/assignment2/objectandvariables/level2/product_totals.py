class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


products = [
    Product("Wireless Mouse", 1200, 2),
    Product("Keyboard", 1800, 1),
    Product("USB Cable", 350, 4),
]

for product in products:
    print("Product:", product.name)
    print("Price: Rs.", product.price)
    print("Quantity:", product.quantity)
    print("Total price: Rs.", product.total_price())
    print()
