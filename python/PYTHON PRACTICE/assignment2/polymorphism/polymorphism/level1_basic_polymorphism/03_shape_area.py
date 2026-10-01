import math


class Rectangle:
    def area(self):
        return 5 * 3


class Circle:
    def area(self):
        return math.pi * 2 * 2


rectangle = Rectangle()
circle = Circle()
print("Rectangle area:", round(rectangle.area(), 2))
print("Circle area:", round(circle.area(), 2))