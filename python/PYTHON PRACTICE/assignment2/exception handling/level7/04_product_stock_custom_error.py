class InsufficientStockError(Exception):
    pass


class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell(self, quantity):
        if quantity > self.stock:
            raise InsufficientStockError("Not enough stock available.")
        self.stock -= quantity


product = Product("Notebook", 5)
try:
    product.sell(2)
    print("Stock remaining:", product.stock)
except InsufficientStockError as error:
    print(error)