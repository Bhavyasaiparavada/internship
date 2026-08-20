# Question 3: Create a Rectangle class with a method that accepts length and width and returns the area.

class Rectangle:
    def __init__(self, name="Rectangle"):
        """Initialize rectangle"""
        self.name = name
        self.rectangles = []
    
    def calculate_area(self, length, width):
        """
        Accept length and width and return the area
        Method accepts two parameters and returns area
        """
        if length <= 0 or width <= 0:
            print("Error: Length and width must be positive!")
            return None
        area = length * width
        return area
    
    def calculate_perimeter(self, length, width):
        """Calculate perimeter of rectangle"""
        if length <= 0 or width <= 0:
            print("Error: Length and width must be positive!")
            return None
        perimeter = 2 * (length + width)
        return perimeter
    
    def calculate_diagonal(self, length, width):
        """Calculate diagonal of rectangle"""
        if length <= 0 or width <= 0:
            print("Error: Length and width must be positive!")
            return None
        diagonal = (length**2 + width**2) ** 0.5
        return diagonal
    
    def is_square(self, length, width):
        """Check if rectangle is a square"""
        return length == width
    
    def add_rectangle(self, length, width):
        """Add rectangle to collection"""
        if length > 0 and width > 0:
            rect = {
                "length": length,
                "width": width,
                "area": self.calculate_area(length, width),
                "perimeter": self.calculate_perimeter(length, width)
            }
            self.rectangles.append(rect)
            print(f"✓ Rectangle added: {length} x {width}")
        else:
            print("Error: Invalid dimensions!")
    
    def display_rectangle_info(self, length, width):
        """Display complete rectangle information"""
        area = self.calculate_area(length, width)
        perimeter = self.calculate_perimeter(length, width)
        diagonal = self.calculate_diagonal(length, width)
        is_square = self.is_square(length, width)
        
        print(f"\n{'='*50}")
        print(f"Rectangle Information:")
        print(f"{'='*50}")
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Area: {area} sq units")
        print(f"Perimeter: {perimeter} units")
        print(f"Diagonal: {diagonal:.2f} units")
        print(f"Is Square: {'Yes' if is_square else 'No'}")
        print(f"{'='*50}\n")
    
    def display_all_rectangles(self):
        """Display all rectangles in collection"""
        print(f"\nAll Rectangles ({len(self.rectangles)} total):")
        print("-" * 60)
        for i, rect in enumerate(self.rectangles, 1):
            print(f"{i}. {rect['length']} x {rect['width']} | Area: {rect['area']} | Perimeter: {rect['perimeter']}")
        print()


# Create rectangle object
print("RECTANGLE AREA CALCULATOR\n")

rect_obj = Rectangle()

# Calculate areas for different rectangles
print("INDIVIDUAL CALCULATIONS")
print("=" * 50)

rect1_area = rect_obj.calculate_area(10, 5)
print(f"Rectangle 1 (10 x 5): Area = {rect1_area} sq units")

rect2_area = rect_obj.calculate_area(15, 8)
print(f"Rectangle 2 (15 x 8): Area = {rect2_area} sq units")

rect3_area = rect_obj.calculate_area(20, 20)
print(f"Rectangle 3 (20 x 20): Area = {rect3_area} sq units (Square)")

rect4_area = rect_obj.calculate_area(12, 7)
print(f"Rectangle 4 (12 x 7): Area = {rect4_area} sq units")

# Display detailed information
print("\n\nDETAILED INFORMATION")
print("=" * 50)
rect_obj.display_rectangle_info(10, 5)
rect_obj.display_rectangle_info(15, 8)
rect_obj.display_rectangle_info(20, 20)

# Add rectangles to collection
print("ADDING RECTANGLES TO COLLECTION")
print("=" * 50 + "\n")
rect_obj.add_rectangle(10, 5)
rect_obj.add_rectangle(15, 8)
rect_obj.add_rectangle(20, 20)
rect_obj.add_rectangle(12, 7)
rect_obj.add_rectangle(9, 6)

# Display all rectangles
rect_obj.display_all_rectangles()

# Calculate total area
print("COLLECTION STATISTICS")
print("=" * 50)
total_area = sum(r["area"] for r in rect_obj.rectangles)
total_perimeter = sum(r["perimeter"] for r in rect_obj.rectangles)
avg_area = total_area / len(rect_obj.rectangles) if rect_obj.rectangles else 0

print(f"Total Rectangles: {len(rect_obj.rectangles)}")
print(f"Total Area: {total_area} sq units")
print(f"Total Perimeter: {total_perimeter} units")
print(f"Average Area: {avg_area:.2f} sq units")
