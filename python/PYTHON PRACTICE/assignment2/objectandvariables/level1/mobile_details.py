class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


mobile = Mobile("Samsung", "Galaxy S24", 75000)
print("Brand:", mobile.brand)
print("Model:", mobile.model)
print("Price: Rs.", mobile.price)
