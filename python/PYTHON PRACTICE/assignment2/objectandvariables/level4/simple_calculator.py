# Question 3: Create a Calculator class with methods for addition, subtraction, multiplication, and division.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def addition(self):
        result = self.num1 + self.num2
        print(f"{self.num1} + {self.num2} = {result}")
        return result
    
    def subtraction(self):
        result = self.num1 - self.num2
        print(f"{self.num1} - {self.num2} = {result}")
        return result
    
    def multiplication(self):
        result = self.num1 * self.num2
        print(f"{self.num1} * {self.num2} = {result}")
        return result
    
    def division(self):
        if self.num2 == 0:
            print("Error: Division by zero is not allowed!")
            return None
        result = self.num1 / self.num2
        print(f"{self.num1} / {self.num2} = {result:.2f}")
        return result
    
    def display_operations(self):
        print(f"Calculator Operations with {self.num1} and {self.num2}:")
        print("-" * 40)
        self.addition()
        self.subtraction()
        self.multiplication()
        self.division()
        print()


# Create calculator objects and perform operations
calc1 = Calculator(20, 5)
calc1.display_operations()

calc2 = Calculator(15, 3)
calc2.display_operations()

calc3 = Calculator(100, 25)
print(f"Calculator Operations with {calc3.num1} and {calc3.num2}:")
print("-" * 40)
calc3.addition()
calc3.subtraction()
calc3.multiplication()
calc3.division()
