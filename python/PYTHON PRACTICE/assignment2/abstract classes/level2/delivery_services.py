from abc import ABC, abstractmethod


class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self, distance):
        pass

    @abstractmethod
    def deliver(self, package):
        pass


class StandardDelivery(Delivery):
    def calculate_charge(self, distance):
        return distance * 10

    def deliver(self, package):
        return f"{package} will be delivered by standard delivery."


class ExpressDelivery(Delivery):
    def calculate_charge(self, distance):
        return distance * 20

    def deliver(self, package):
        return f"{package} will be delivered by express delivery."


for delivery in (StandardDelivery(), ExpressDelivery()):
    print("Delivery charge:", delivery.calculate_charge(5))
    print(delivery.deliver("Package 101"))
