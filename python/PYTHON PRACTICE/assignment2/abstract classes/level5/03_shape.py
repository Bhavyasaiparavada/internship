from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def display_shape(self):
        return "This is a shape."


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


circle = Circle(3)
print(circle.display_shape())
print("Area:", circle.area())