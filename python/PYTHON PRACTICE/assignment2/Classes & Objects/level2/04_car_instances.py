class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price


cars = [Car("Toyota", "Corolla", 2022, 24000), Car("Honda", "Civic", 2023, 26000), Car("Ford", "Focus", 2021, 22000)]
for car in cars:
    print(car.brand, car.model, car.year, car.price)