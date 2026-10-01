from abc import ABC, abstractmethod


class Delivery(ABC):
    @abstractmethod
    def calculate_delivery_charge(self):
        pass


class StandardDelivery(Delivery):
    def calculate_delivery_charge(self):
        return 50


class ExpressDelivery(Delivery):
    def calculate_delivery_charge(self):
        return 100


standard_delivery = StandardDelivery()
express_delivery = ExpressDelivery()
print("Standard delivery charge:", standard_delivery.calculate_delivery_charge())
print("Express delivery charge:", express_delivery.calculate_delivery_charge())