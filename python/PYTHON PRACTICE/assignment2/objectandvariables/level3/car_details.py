# Question 9: Create a Car class with class variables company and number_of_wheels,
# and instance variables model and price.

class CarDetail:
    company = "Global Motors"
    number_of_wheels = 4
    
    def __init__(self, model, price, color):
        self.model = model
        self.price = price
        self.color = color
    
    def display_car_info(self):
        print(f"Company: {CarDetail.company}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")
        print(f"Color: {self.color}")
        print(f"Wheels: {CarDetail.number_of_wheels}")
        print("-" * 40)
    
    def get_price(self):
        return self.price
    
    def get_model(self):
        return self.model
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
    
    @classmethod
    def get_class_info(cls):
        print(f"Company: {cls.company}, Number of Wheels: {cls.number_of_wheels}")


# Create car objects with instance variables
print("Car Inventory:\n")

car1 = CarDetail("Sedan X1", 35000, "Black")
car1.display_car_info()

car2 = CarDetail("SUV Pro", 55000, "White")
car2.display_car_info()

car3 = CarDetail("Coupe Sport", 45000, "Red")
car3.display_car_info()

car4 = CarDetail("Hatchback Eco", 25000, "Blue")
car4.display_car_info()

car5 = CarDetail("Pickup Truck", 50000, "Silver")
car5.display_car_info()

# Display class information
print("\n--- Class Information ---")
CarDetail.get_class_info()

# Extract instance variables
print("\n--- Car Details ---")
print(f"Car 1: Model = {car1.get_model()}, Price = ${car1.get_price()}")
print(f"Car 2: Model = {car2.get_model()}, Price = ${car2.get_price()}")
print(f"Car 3: Model = {car3.get_model()}, Price = ${car3.get_price()}")

# Change company name for all cars
print("\n--- Changing Company Name ---")
CarDetail.change_company("Premium Automobiles Ltd.")

print("\n--- Updated Car Info ---")
car1.display_car_info()
car2.display_car_info()
