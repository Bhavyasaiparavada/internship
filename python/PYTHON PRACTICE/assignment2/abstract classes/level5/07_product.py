from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass

    def display_product(self):
        return self.name + " costs " + str(self.price)


class Book(Product):
    def calculate_discount(self):
        return self.price * 0.10


book = Book("Python Basics", 1000)
print(book.display_product())
print("Discount:", book.calculate_discount())