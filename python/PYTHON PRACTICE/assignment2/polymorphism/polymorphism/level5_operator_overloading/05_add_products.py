class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price


product1 = Product("Pen", 10)
product2 = Product("Book", 50)
print("Combined price:", product1 + product2)