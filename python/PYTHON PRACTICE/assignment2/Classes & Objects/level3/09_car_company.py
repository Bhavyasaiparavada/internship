class Car:
    company = "Toyota"
    number_of_wheels = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price


car = Car("Corolla", 24000)
print(car.company, car.number_of_wheels, car.model, car.price)