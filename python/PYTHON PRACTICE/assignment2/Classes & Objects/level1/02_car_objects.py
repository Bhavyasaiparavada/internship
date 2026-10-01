class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


cars = [Car("Toyota", "Red"), Car("Honda", "Blue"), Car("Ford", "Black")]
for car in cars:
    print(car.brand, car.color)