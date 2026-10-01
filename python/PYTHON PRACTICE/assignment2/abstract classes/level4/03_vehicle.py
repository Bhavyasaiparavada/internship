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


for vehicle in [Car(), Bike()]:
    print(vehicle.start())