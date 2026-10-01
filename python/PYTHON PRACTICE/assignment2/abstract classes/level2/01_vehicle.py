from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        return "Car started."

    def stop(self):
        return "Car stopped."


class Bike(Vehicle):
    def start(self):
        return "Bike started."

    def stop(self):
        return "Bike stopped."


print(Car().start(), Car().stop())
print(Bike().start(), Bike().stop())