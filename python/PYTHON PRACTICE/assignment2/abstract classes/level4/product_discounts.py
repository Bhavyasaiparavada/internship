from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass


class Electronics(Product):
    def calculate_discount(self):
        return self.price * 0.10


class Clothing(Product):
    def calculate_discount(self):
        return self.price * 0.20


products = [Electronics("Headphones", 2000), Clothing("Jacket", 3000)]
for product in products:
    discount = product.calculate_discount()
    print(product.product_name, "Discount: Rs.", discount)
    print("Final price: Rs.", product.price - discount)
