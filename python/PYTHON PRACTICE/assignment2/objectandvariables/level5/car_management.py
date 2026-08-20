# Question 4: Create a Car class using __init__() and methods start(), stop(), and display().

class Car:
    def __init__(self, brand, model, year, color, fuel_capacity):
        """Initialize car attributes"""
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel_capacity = fuel_capacity
        self.current_fuel = 0
        self.is_running = False
        self.mileage = 0
    
    def start(self):
        """Start the car engine"""
        if self.current_fuel > 0:
            if not self.is_running:
                self.is_running = True
                print(f"✓ {self.year} {self.brand} {self.model} engine started!")
            else:
                print("Engine is already running!")
        else:
            print("Error: No fuel! Cannot start the engine.")
    
    def stop(self):
        """Stop the car engine"""
        if self.is_running:
            self.is_running = False
            print(f"✓ {self.year} {self.brand} {self.model} engine stopped!")
        else:
            print("Engine is already stopped!")
    
    def display(self):
        """Display car information"""
        status = "Running" if self.is_running else "Stopped"
        print(f"\n{'='*50}")
        print(f"Car Details:")
        print(f"{'='*50}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Fuel Capacity: {self.fuel_capacity} liters")
        print(f"Current Fuel: {self.current_fuel} liters")
        print(f"Engine Status: {status}")
        print(f"Mileage: {self.mileage} km")
        print(f"{'='*50}\n")
    
    def add_fuel(self, amount):
        """Add fuel to the tank"""
        if self.current_fuel + amount <= self.fuel_capacity:
            self.current_fuel += amount
            print(f"✓ Added {amount} liters of fuel. Current fuel: {self.current_fuel} liters")
        else:
            print(f"Error: Tank overflow! Maximum capacity is {self.fuel_capacity} liters")
    
    def drive(self, distance):
        """Drive the car"""
        if self.is_running:
            fuel_needed = distance / 10  # Consumes 1 liter per 10 km
            if self.current_fuel >= fuel_needed:
                self.current_fuel -= fuel_needed
                self.mileage += distance
                print(f"✓ Drove {distance} km. Remaining fuel: {self.current_fuel:.1f} liters")
            else:
                print(f"Error: Not enough fuel to drive {distance} km!")
        else:
            print("Error: Start the engine first!")


# Create car objects using __init__()
print("CAR MANAGEMENT SYSTEM\n")

car1 = Car("Toyota", "Camry", 2023, "Black", 60)
car2 = Car("Honda", "Civic", 2022, "White", 50)
car3 = Car("BMW", "X5", 2023, "Red", 80)

# Display car information
car1.display()
car2.display()
car3.display()

# Operations on car1
print("CAR 1 OPERATIONS")
print("=" * 50)
car1.add_fuel(50)
car1.display()
car1.start()
car1.drive(100)
car1.drive(150)
car1.stop()
car1.display()

# Operations on car2
print("\nCAR 2 OPERATIONS")
print("=" * 50)
car2.add_fuel(40)
car2.start()
car2.drive(200)
car2.add_fuel(20)
car2.drive(150)
car2.stop()
car2.display()

# Operations on car3
print("\nCAR 3 OPERATIONS")
print("=" * 50)
car3.add_fuel(70)
car3.start()
car3.drive(300)
car3.stop()
car3.display()

# Try to drive without fuel
print("\nTRY TO START WITHOUT FUEL")
print("=" * 50)
car_empty = Car("Tesla", "Model 3", 2023, "Silver", 75)
car_empty.display()
car_empty.start()
