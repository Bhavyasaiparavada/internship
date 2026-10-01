class DeliveryService:
    def deliver(self, address):
        print("Delivering order to", address)


class FoodOrder:
    def __init__(self, address):
        self.address = address

    def send_for_delivery(self, service):
        service.deliver(self.address)


FoodOrder("12 Main Street").send_for_delivery(DeliveryService())
