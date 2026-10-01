from abc import ABC, abstractmethod


class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self):
        pass


class StandardDelivery(Delivery):
    def calculate_charge(self):
        return 50


class ExpressDelivery(Delivery):
    def calculate_charge(self):
        return 100


for delivery in [StandardDelivery(), ExpressDelivery()]:
    print("Delivery charge:", delivery.calculate_charge())