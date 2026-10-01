class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price


laptop = Laptop("Dell", "16 GB", "Core i5", 70000)
print(laptop.brand, laptop.ram, laptop.processor, laptop.price)