class Vehicle:
    def move(self):
        print("Vehicle moving")


class Engine:
    def start(self):
        print("Engine started")


class Car(Vehicle):
    def __init__(self):
        self.engine = Engine()


car = Car()
car.move()
car.engine.start()
