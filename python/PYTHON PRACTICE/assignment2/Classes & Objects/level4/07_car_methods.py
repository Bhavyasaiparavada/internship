class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def display_details(self):
        print(self.brand, self.model)


car = Car("Toyota", "Corolla")
car.display_details()
car.start()
car.stop()