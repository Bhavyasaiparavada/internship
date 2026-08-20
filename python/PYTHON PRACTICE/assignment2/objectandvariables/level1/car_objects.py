class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


cars = [
    Car("Toyota", "Corolla", "White"),
    Car("Honda", "City", "Red"),
    Car("Ford", "Mustang", "Blue"),
]

for car in cars:
    print(car.brand, car.model, "-", car.color)
