from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        return "Car starts with a key."


class Bike(Vehicle):
    def start(self):
        return "Bike starts with a self-start button."


print(Car().start())
print(Bike().start())
