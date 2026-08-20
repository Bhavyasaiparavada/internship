# Question 7: Create a Car class with methods start(), stop(), and display_details().

class Car:
    def __init__(self, brand, model, year, color, fuel_level=100):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel_level = fuel_level
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            if self.fuel_level > 0:
                self.is_running = True
                print(f"✓ {self.year} {self.brand} {self.model} engine started!")
            else:
                print(f"Error: No fuel to start the engine!")
        else:
            print(f"Engine is already running!")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"✓ {self.year} {self.brand} {self.model} engine stopped!")
        else:
            print(f"Engine is already stopped!")
    
    def display_details(self):
        status = "Running" if self.is_running else "Stopped"
        print(f"\n{'='*50}")
        print(f"Car Details:")
        print(f"{'='*50}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Fuel Level: {self.fuel_level}%")
        print(f"Engine Status: {status}")
        print(f"{'='*50}")
    
    def add_fuel(self, amount):
        if amount > 0:
            self.fuel_level = min(100, self.fuel_level + amount)
            print(f"✓ Added {amount}% fuel. Current fuel level: {self.fuel_level}%")
        else:
            print("Error: Fuel amount must be positive!")
    
    def drive(self, distance):
        if self.is_running:
            fuel_consumed = distance * 0.5  # 0.5% per unit distance
            if self.fuel_level >= fuel_consumed:
                self.fuel_level -= fuel_consumed
                print(f"✓ Drove {distance} units. Fuel remaining: {self.fuel_level:.1f}%")
            else:
                print(f"Error: Not enough fuel! (Need {fuel_consumed}%, Available: {self.fuel_level}%)")
        else:
            print("Error: Start the engine first!")


# Create car objects
car1 = Car("Toyota", "Camry", 2023, "Black", 80)
car2 = Car("Honda", "Civic", 2022, "White", 60)
car3 = Car("BMW", "X5", 2023, "Red", 100)

# Display car details
car1.display_details()
car2.display_details()
car3.display_details()

# Perform operations on car1
print("\n--- Car 1 Operations ---")
car1.start()
car1.drive(50)
car1.display_details()
car1.stop()
print()

# Perform operations on car2
print("--- Car 2 Operations ---")
car2.start()
car2.drive(30)
car2.add_fuel(30)
car2.drive(40)
car2.stop()
car2.display_details()
print()

# Try to drive with low fuel
print("--- Car 3 Operations ---")
car3.start()
car3.drive(100)
car3.display_details()
