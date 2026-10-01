from abc import ABC, abstractmethod


class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self):
        pass

    @abstractmethod
    def deliver(self):
        pass


class StandardDelivery(Delivery):
    def calculate_charge(self):
        return 50

    def deliver(self):
        return "Standard delivery selected."


class ExpressDelivery(Delivery):
    def calculate_charge(self):
        return 100

    def deliver(self):
        return "Express delivery selected."


for option in [StandardDelivery(), ExpressDelivery()]:
    print(option.deliver(), "Charge:", option.calculate_charge())