from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def display_info(self):
        return "This is a vehicle."


class Car(Vehicle):
    def start(self):
        return "Car started."


car = Car()
print(car.display_info())
print(car.start())