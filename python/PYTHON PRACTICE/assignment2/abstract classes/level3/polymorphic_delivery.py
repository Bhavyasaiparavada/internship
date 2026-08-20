from abc import ABC, abstractmethod


class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self, distance):
        pass


class StandardDelivery(Delivery):
    def calculate_charge(self, distance):
        return distance * 10


class ExpressDelivery(Delivery):
    def calculate_charge(self, distance):
        return distance * 20


class SameDayDelivery(Delivery):
    def calculate_charge(self, distance):
        return distance * 30


delivery_services = [StandardDelivery(), ExpressDelivery(), SameDayDelivery()]
for delivery in delivery_services:
    print("Delivery charge: Rs.", delivery.calculate_charge(5))
