class Product:
    def __init__(self, name):
        self.name = name


class PaymentService:
    def pay(self):
        print("Order paid")


class DeliveryService:
    def deliver(self):
        print("Order sent for delivery")


class OnlineOrder:
    def __init__(self):
        self.products = [Product("Book"), Product("Pen")]

    def complete(self, payment, delivery):
        payment.pay()
        delivery.deliver()


order = OnlineOrder()
print("Products:", ", ".join(product.name for product in order.products))
order.complete(PaymentService(), DeliveryService())
