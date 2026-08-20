class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price


laptops = [
    Laptop("Dell", "16 GB", "512 GB SSD", 72000),
    Laptop("HP", "8 GB", "512 GB SSD", 58000),
    Laptop("Lenovo", "16 GB", "1 TB SSD", 85000),
]

for laptop in laptops:
    print("Brand:", laptop.brand)
    print("RAM:", laptop.ram)
    print("Storage:", laptop.storage)
    print("Price: Rs.", laptop.price)
    print()
