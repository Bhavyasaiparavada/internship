class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a switch")


car = Car()
bike = Bike()
bus = Bus()
car.start()
bike.start()
bus.start()