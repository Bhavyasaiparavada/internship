# Question 1: Create a Calculator class with methods that accept parameters and return calculation results.

class Calculator:
    def __init__(self):
        """Initialize calculator"""
        self.last_result = 0
    
    def add(self, a, b):
        """Add two numbers and return result"""
        result = a + b
        self.last_result = result
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers and return result"""
        result = a - b
        self.last_result = result
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers and return result"""
        result = a * b
        self.last_result = result
        return result
    
    def divide(self, a, b):
        """Divide two numbers and return result"""
        if b == 0:
            print("Error: Division by zero!")
            return None
        result = a / b
        self.last_result = result
        return result
    
    def power(self, base, exponent):
        """Calculate power and return result"""
        result = base ** exponent
        self.last_result = result
        return result
    
    def square_root(self, num):
        """Calculate square root and return result"""
        if num < 0:
            print("Error: Cannot calculate square root of negative number!")
            return None
        result = num ** 0.5
        self.last_result = result
        return result
    
    def modulus(self, a, b):
        """Calculate modulus and return result"""
        if b == 0:
            print("Error: Division by zero!")
            return None
        result = a % b
        self.last_result = result
        return result
    
    def get_last_result(self):
        """Get the last calculation result"""
        return self.last_result
    
    def display_calculation(self, operation, *args):
        """Display calculation details"""
        print(f"Operation: {operation}")
        print(f"Arguments: {args}")
        print(f"Result: {self.last_result}")
        print("-" * 40)


# Create calculator object and perform operations
print("CALCULATOR WITH PARAMETER METHODS\n")

calc = Calculator()

# Perform calculations
print("Arithmetic Operations:")
print(f"10 + 5 = {calc.add(10, 5)}")
print(f"20 - 8 = {calc.subtract(20, 8)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"25 / 5 = {calc.divide(25, 5)}")
print(f"2 ^ 8 = {calc.power(2, 8)}")
print(f"√16 = {calc.square_root(16)}")
print(f"17 % 5 = {calc.modulus(17, 5)}")
print()

# Display detailed calculations
print("DETAILED CALCULATIONS")
print("=" * 40)
calc.add(100, 50)
calc.display_calculation("Addition", 100, 50)

calc.multiply(12, 15)
calc.display_calculation("Multiplication", 12, 15)

calc.power(5, 3)
calc.display_calculation("Power", 5, 3)

calc.square_root(144)
calc.display_calculation("Square Root", 144)

# Chain calculations
print("\nChain Calculations:")
result1 = calc.add(10, 20)
print(f"Step 1: 10 + 20 = {result1}")

result2 = calc.multiply(result1, 2)
print(f"Step 2: {result1} * 2 = {result2}")

result3 = calc.divide(result2, 5)
print(f"Step 3: {result2} / 5 = {result3}")

print(f"\nFinal Result: {calc.get_last_result()}")
