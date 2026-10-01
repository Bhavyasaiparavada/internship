class PaymentGateway:
    def pay(self, amount):
        print("Paid:", amount)


class ShoppingCart:
    def checkout(self, gateway):
        gateway.pay(20)


print("USES-A: ShoppingCart uses a PaymentGateway")
ShoppingCart().checkout(PaymentGateway())
