from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        return math.pi * 2 * 2


class Rectangle(Shape):
    def area(self):
        return 5 * 3


class Triangle(Shape):
    def area(self):
        return 0.5 * 4 * 3


circle = Circle()
rectangle = Rectangle()
triangle = Triangle()
print("Circle area:", round(circle.area(), 2))
print("Rectangle area:", round(rectangle.area(), 2))
print("Triangle area:", round(triangle.area(), 2))