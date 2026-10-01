from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass


class Book(Product):
    def calculate_discount(self):
        return self.price * 0.10


book = Book("Python Basics", 1000)
print(book.product_name, "Discount:", book.calculate_discount())