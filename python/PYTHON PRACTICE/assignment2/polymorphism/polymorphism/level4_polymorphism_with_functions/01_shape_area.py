import math


class Rectangle:
    def area(self):
        return 5 * 3


class Circle:
    def area(self):
        return math.pi * 2 * 2


def show_area(shape):
    print("Area:", round(shape.area(), 2))


show_area(Rectangle())
show_area(Circle())