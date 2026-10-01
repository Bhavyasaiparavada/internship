class Car:
    def start(self):
        print("Car starts with a key")


class Bike:
    def start(self):
        print("Bike starts with a button")


class Bus:
    def start(self):
        print("Bus starts with a switch")


car = Car()
bike = Bike()
bus = Bus()
car.start()
bike.start()
bus.start()