from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Pizza(Food):
    def prepare(self):
        return "Pizza is prepared with toppings and cheese."


class Burger(Food):
    def prepare(self):
        return "Burger is prepared with a patty and vegetables."


print(Pizza().prepare())
print(Burger().prepare())
