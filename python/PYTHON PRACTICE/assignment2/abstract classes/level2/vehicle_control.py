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
        return "Car starts with a key."

    def stop(self):
        return "Car stops using its brakes."


class Bike(Vehicle):
    def start(self):
        return "Bike starts with a self-start button."

    def stop(self):
        return "Bike stops using its brakes."


car = Car()
bike = Bike()
print(car.start())
print(car.stop())
print(bike.start())
print(bike.stop())
