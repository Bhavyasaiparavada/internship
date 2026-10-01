class PaymentService:
    def pay(self, amount):
        print("Payment received:", amount)


class Order:
    def pay(self, service):
        service.pay(30)


print("USES-A: Order uses a PaymentService")
Order().pay(PaymentService())
