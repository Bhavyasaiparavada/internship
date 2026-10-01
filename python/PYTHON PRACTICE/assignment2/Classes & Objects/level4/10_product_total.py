class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity


product = Product("Notebook", 50, 3)
print(product.name, "total cost:", product.total_cost())