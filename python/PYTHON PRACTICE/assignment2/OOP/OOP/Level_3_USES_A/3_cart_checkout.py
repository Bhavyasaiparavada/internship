class PaymentGateway:
    def pay(self, amount):
        print("Payment approved:", amount)


class ShoppingCart:
    def __init__(self):
        self.total = 25

    def checkout(self, gateway):
        gateway.pay(self.total)


ShoppingCart().checkout(PaymentGateway())
