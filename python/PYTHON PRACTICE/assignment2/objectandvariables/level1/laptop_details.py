class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price


laptop = Laptop("Dell", "16 GB", "Intel Core i7", 85000)
print("Brand:", laptop.brand)
print("RAM:", laptop.ram)
print("Processor:", laptop.processor)
print("Price: Rs.", laptop.price)
