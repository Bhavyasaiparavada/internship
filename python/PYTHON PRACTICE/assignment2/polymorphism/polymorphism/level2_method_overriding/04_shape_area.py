import math


class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def area(self):
        return 5 * 3


class Circle(Shape):
    def area(self):
        return math.pi * 2 * 2


class Triangle(Shape):
    def area(self):
        return 0.5 * 4 * 3


rectangle = Rectangle()
circle = Circle()
triangle = Triangle()
print("Rectangle area:", round(rectangle.area(), 2))
print("Circle area:", round(circle.area(), 2))
print("Triangle area:", round(triangle.area(), 2))