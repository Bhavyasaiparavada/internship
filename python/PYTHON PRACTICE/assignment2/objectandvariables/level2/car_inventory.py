class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price


cars = [
    Car("Toyota", "Camry", 2022, 2850000),
    Car("Honda", "City", 2023, 1650000),
    Car("Hyundai", "Creta", 2024, 1950000),
]

for car in cars:
    print("Brand:", car.brand)
    print("Model:", car.model)
    print("Year:", car.year)
    print("Price: Rs.", car.price)
    print()
