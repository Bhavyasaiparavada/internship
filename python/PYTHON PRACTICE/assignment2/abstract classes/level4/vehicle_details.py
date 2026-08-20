from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        return f"{self.brand} {self.model} starts with a key."

    def stop(self):
        return f"{self.brand} {self.model} stops with its brakes."


class Bike(Vehicle):
    def start(self):
        return f"{self.brand} {self.model} starts with a self-start button."

    def stop(self):
        return f"{self.brand} {self.model} stops with its brakes."


vehicles = [Car("Toyota", "Corolla"), Bike("Honda", "Shine")]
for vehicle in vehicles:
    print(vehicle.start())
    print(vehicle.stop())
