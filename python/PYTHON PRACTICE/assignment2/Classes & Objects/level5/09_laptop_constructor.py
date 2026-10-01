class Laptop:
    def __init__(self, brand, model, ram, storage, processor, price):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.storage = storage
        self.processor = processor
        self.price = price

    def display(self):
        print(self.brand, self.model, self.ram, self.storage, self.processor, self.price)


laptop = Laptop("Dell", "Inspiron", "16 GB", "512 GB", "Core i5", 70000)
laptop.display()