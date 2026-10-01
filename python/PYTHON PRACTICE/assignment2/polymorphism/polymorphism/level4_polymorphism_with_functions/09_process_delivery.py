class HomeDelivery:
    def deliver(self):
        print("Delivering to a home")


class StorePickup:
    def deliver(self):
        print("Preparing an order for store pickup")


def process_delivery(delivery):
    delivery.deliver()


process_delivery(HomeDelivery())
process_delivery(StorePickup())