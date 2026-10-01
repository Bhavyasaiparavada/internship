class Vehicle:
    def move(self):
        print("The vehicle is moving")


class Car(Vehicle):
    def honk(self):
        print("Beep beep!")


car = Car()
car.move()
car.honk()
