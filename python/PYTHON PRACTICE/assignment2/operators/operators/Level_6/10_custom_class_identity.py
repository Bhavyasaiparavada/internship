# 10. Demonstrate identity comparison using custom class objects.
class Book:
    def __init__(self, name):
        self.name = name

b1 = Book('Python')
b2 = b1
print(b1 is b2)
