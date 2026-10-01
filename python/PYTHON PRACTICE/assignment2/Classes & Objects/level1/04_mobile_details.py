class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


mobile = Mobile("Samsung", "Galaxy A", 25000)
print(mobile.brand, mobile.model, mobile.price)