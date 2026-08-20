# Question 10: Create a Temperature class with methods to convert Celsius to Fahrenheit and Fahrenheit to Celsius.

class Temperature:
    def __init__(self, value=0, unit="C"):
        """Initialize temperature"""
        self.value = value
        self.unit = unit.upper()
    
    def celsius_to_fahrenheit(self, celsius):
        """
        Convert Celsius to Fahrenheit
        Method accepts Celsius value and returns Fahrenheit
        """
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    def fahrenheit_to_celsius(self, fahrenheit):
        """
        Convert Fahrenheit to Celsius
        Method accepts Fahrenheit value and returns Celsius
        """
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    
    def celsius_to_kelvin(self, celsius):
        """Convert Celsius to Kelvin"""
        kelvin = celsius + 273.15
        return kelvin
    
    def kelvin_to_celsius(self, kelvin):
        """Convert Kelvin to Celsius"""
        celsius = kelvin - 273.15
        return celsius
    
    def fahrenheit_to_kelvin(self, fahrenheit):
        """Convert Fahrenheit to Kelvin"""
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        kelvin = self.celsius_to_kelvin(celsius)
        return kelvin
    
    def kelvin_to_fahrenheit(self, kelvin):
        """Convert Kelvin to Fahrenheit"""
        celsius = self.kelvin_to_celsius(kelvin)
        fahrenheit = self.celsius_to_fahrenheit(celsius)
        return fahrenheit
    
    def convert(self, value, from_unit, to_unit):
        """Convert between any two units"""
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()
        
        # Convert to Celsius first
        if from_unit == "C":
            celsius = value
        elif from_unit == "F":
            celsius = self.fahrenheit_to_celsius(value)
        elif from_unit == "K":
            celsius = self.kelvin_to_celsius(value)
        else:
            print("Error: Invalid unit!")
            return None
        
        # Convert from Celsius to target unit
        if to_unit == "C":
            return celsius
        elif to_unit == "F":
            return self.celsius_to_fahrenheit(celsius)
        elif to_unit == "K":
            return self.celsius_to_kelvin(celsius)
        else:
            print("Error: Invalid unit!")
            return None
    
    def display_conversion(self, value, from_unit, to_unit):
        """Display temperature conversion"""
        result = self.convert(value, from_unit, to_unit)
        if result is not None:
            print(f"{value}°{from_unit} = {result:.2f}°{to_unit}")
    
    def display_all_conversions(self, value, from_unit):
        """Display conversions to all units"""
        from_unit = from_unit.upper()
        
        print(f"\n{'='*60}")
        print(f"TEMPERATURE CONVERSIONS FROM {value}°{from_unit}")
        print(f"{'='*60}")
        
        # Convert to Celsius first
        if from_unit == "C":
            celsius = value
        elif from_unit == "F":
            celsius = self.fahrenheit_to_celsius(value)
        elif from_unit == "K":
            celsius = self.kelvin_to_celsius(value)
        else:
            print("Error: Invalid unit!")
            return
        
        # Display conversions
        print(f"Celsius: {celsius:.2f}°C")
        print(f"Fahrenheit: {self.celsius_to_fahrenheit(celsius):.2f}°F")
        print(f"Kelvin: {self.celsius_to_kelvin(celsius):.2f}K")
        print(f"{'='*60}\n")
    
    def get_temperature_category(self, celsius):
        """Get temperature category"""
        if celsius < -50:
            return "Extremely Cold"
        elif celsius < 0:
            return "Freezing"
        elif celsius < 15:
            return "Cold"
        elif celsius < 25:
            return "Mild"
        elif celsius < 35:
            return "Warm"
        elif celsius < 50:
            return "Hot"
        else:
            return "Extremely Hot"


# Create temperature object
print("TEMPERATURE CONVERTER\n")

temp = Temperature()

# Celsius to Fahrenheit conversions
print("CELSIUS TO FAHRENHEIT CONVERSION")
print("=" * 60)

celsius_values = [0, 10, 20, 25, 30, 37, 100]
for c in celsius_values:
    f = temp.celsius_to_fahrenheit(c)
    print(f"{c}°C = {f:.2f}°F")

print()

# Fahrenheit to Celsius conversions
print("\nFAHRENHEIT TO CELSIUS CONVERSION")
print("=" * 60)

fahrenheit_values = [32, 50, 68, 77, 86, 98.6, 212]
for f in fahrenheit_values:
    c = temp.fahrenheit_to_celsius(f)
    print(f"{f}°F = {c:.2f}°C")

print()

# All conversions from different units
print("\n\nALL UNIT CONVERSIONS")
print("=" * 60)

temp.display_all_conversions(0, "C")
temp.display_all_conversions(32, "F")
temp.display_all_conversions(273.15, "K")

# Temperature categories
print("TEMPERATURE CATEGORIES")
print("=" * 60)

test_temps = [-60, -10, 5, 15, 25, 35, 45, 60]
for celsius in test_temps:
    category = temp.get_temperature_category(celsius)
    fahrenheit = temp.celsius_to_fahrenheit(celsius)
    kelvin = temp.celsius_to_kelvin(celsius)
    print(f"{celsius:4}°C ({fahrenheit:6.1f}°F) - {category}")

print()

# Conversion table
print("\n\nCONVERSION TABLE")
print("=" * 60)
print(f"{'Celsius':<15} {'Fahrenheit':<15} {'Kelvin':<15} {'Category':<20}")
print("-" * 65)

conversion_temps = [-40, -20, 0, 20, 25, 37, 50, 100]
for c in conversion_temps:
    f = temp.celsius_to_fahrenheit(c)
    k = temp.celsius_to_kelvin(c)
    category = temp.get_temperature_category(c)
    print(f"{c:<15} {f:<15.2f} {k:<15.2f} {category:<20}")

print()

# Common temperature conversions
print("\n\nCOMMON TEMPERATURES")
print("=" * 60)

common_temps = {
    "Water Freezes": 0,
    "Room Temperature": 20,
    "Body Temperature": 37,
    "Water Boils": 100,
    "Absolute Zero": -273.15
}

print(f"{'Description':<25} {'Celsius':<15} {'Fahrenheit':<15} {'Kelvin':<15}")
print("-" * 70)

for desc, celsius in common_temps.items():
    fahrenheit = temp.celsius_to_fahrenheit(celsius)
    kelvin = temp.celsius_to_kelvin(celsius)
    print(f"{desc:<25} {celsius:<15.2f} {fahrenheit:<15.2f} {kelvin:<15.2f}")

print()

# Interactive conversion
print("\n\nCUSTOM CONVERSIONS")
print("=" * 60)

conversions = [
    (25, "C", "F"),
    (98.6, "F", "C"),
    (300, "K", "C"),
    (100, "C", "K"),
    (32, "F", "K")
]

for value, from_unit, to_unit in conversions:
    temp.display_conversion(value, from_unit, to_unit)
