class Shape:
    def describe(self):
        print("This is a shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(5, 3)
rectangle.describe()
print("Area:", rectangle.area())
