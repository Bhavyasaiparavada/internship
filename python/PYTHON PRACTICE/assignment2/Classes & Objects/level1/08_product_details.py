class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


product = Product("Notebook", 50, 4)
print(product.name, product.price, product.quantity)