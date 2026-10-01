from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        return "Car started."


class Bike(Vehicle):
    def start(self):
        return "Bike started."


print(Car().start())
print(Bike().start())