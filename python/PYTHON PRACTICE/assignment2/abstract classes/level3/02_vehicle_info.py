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
        return "Car started."

    def stop(self):
        return "Car stopped."


car = Car("Toyota", "Corolla")
print(car.brand, car.model, car.start(), car.stop())