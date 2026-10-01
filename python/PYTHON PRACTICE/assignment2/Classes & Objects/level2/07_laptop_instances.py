class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price


laptops = [Laptop("Dell", "8 GB", "256 GB", 50000), Laptop("HP", "16 GB", "512 GB", 75000), Laptop("Lenovo", "8 GB", "1 TB", 60000)]
for laptop in laptops:
    print(laptop.brand, laptop.ram, laptop.storage, laptop.price)