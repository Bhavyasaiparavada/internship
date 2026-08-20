# Question 5: Create a Circle class with methods to calculate area and circumference.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area
    
    def calculate_circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference
    
    def display_info(self):
        print(f"Circle Information:")
        print(f"Radius: {self.radius} units")
        print(f"Area: {self.calculate_area():.2f} square units")
        print(f"Circumference: {self.calculate_circumference():.2f} units")
        print(f"Diameter: {2 * self.radius} units")
        print("-" * 40)
    
    def display_detailed_info(self):
        print(f"Circle with radius {self.radius}:")
        print(f"  Area: {self.calculate_area():.4f}")
        print(f"  Circumference: {self.calculate_circumference():.4f}")


# Create circle objects
circle1 = Circle(5)
circle2 = Circle(10)
circle3 = Circle(7.5)
circle4 = Circle(3)

print("Circle Calculations:\n")
circle1.display_info()
circle2.display_info()
circle3.display_info()
circle4.display_info()

# Detailed calculations
print("Detailed Calculations:")
circle1.display_detailed_info()
circle2.display_detailed_info()
circle3.display_detailed_info()
