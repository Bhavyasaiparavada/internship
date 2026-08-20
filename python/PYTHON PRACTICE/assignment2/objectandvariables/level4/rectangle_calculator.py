# Question 4: Create a Rectangle class with methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        area = self.length * self.width
        return area
    
    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter
    
    def display_info(self):
        print(f"Rectangle Dimensions:")
        print(f"Length: {self.length} units")
        print(f"Width: {self.width} units")
        print(f"Area: {self.calculate_area()} square units")
        print(f"Perimeter: {self.calculate_perimeter()} units")
        print("-" * 40)


# Create rectangle objects
rect1 = Rectangle(10, 5)
rect2 = Rectangle(15, 8)
rect3 = Rectangle(20, 12)
rect4 = Rectangle(7, 3)

print("Rectangle Calculations:\n")
rect1.display_info()
rect2.display_info()
rect3.display_info()
rect4.display_info()

# Individual calculations
print("Individual Calculations:")
print(f"\nRectangle 1 - Area: {rect1.calculate_area()}, Perimeter: {rect1.calculate_perimeter()}")
print(f"Rectangle 2 - Area: {rect2.calculate_area()}, Perimeter: {rect2.calculate_perimeter()}")
print(f"Rectangle 3 - Area: {rect3.calculate_area()}, Perimeter: {rect3.calculate_perimeter()}")
print(f"Rectangle 4 - Area: {rect4.calculate_area()}, Perimeter: {rect4.calculate_perimeter()}")
