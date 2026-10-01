class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        return self.length * self.width == other.length * other.width


rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(2, 10)
print(rectangle1 == rectangle2)