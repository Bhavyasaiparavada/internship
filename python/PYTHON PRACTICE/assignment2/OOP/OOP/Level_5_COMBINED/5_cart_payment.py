class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PaymentGateway:
    def pay(self, amount):
        print("Paid:", amount)


class ShoppingCart:
    def __init__(self):
        self.products = [Product("Book", 10), Product("Pen", 2)]

    def checkout(self, gateway):
        total = sum(product.price for product in self.products)
        gateway.pay(total)


ShoppingCart().checkout(PaymentGateway())
