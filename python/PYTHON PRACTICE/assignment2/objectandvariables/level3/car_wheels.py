# Question 3: Create a Car class with a class variable number_of_wheels
# Display it using different objects.

class Car:
    number_of_wheels = 4
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Wheels: {Car.number_of_wheels}")
    
    def display_wheels_only(self):
        return self.number_of_wheels


# Create different car objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("BMW", "X5")
car4 = Car("Tesla", "Model 3")

# Display info using different objects
print("Car Information:")
car1.display_info()
car2.display_info()
car3.display_info()
car4.display_info()

# Display number of wheels using class variable
print(f"\nNumber of wheels (from class): {Car.number_of_wheels}")
print(f"Number of wheels (from car1 object): {car1.number_of_wheels}")
print(f"Number of wheels (from car2 object): {car2.number_of_wheels}")
