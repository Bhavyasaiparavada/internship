# Question 9: Create a Laptop class using __init__() and a method to display complete specifications.

class Laptop:
    def __init__(self, brand, model, processor, ram, storage, graphics, display_size, weight, price):
        """Initialize laptop attributes"""
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram  # in GB
        self.storage = storage  # in GB
        self.graphics = graphics
        self.display_size = display_size  # in inches
        self.weight = weight  # in kg
        self.price = price
    
    def display_specifications(self):
        """Display complete laptop specifications"""
        print(f"\n{'='*60}")
        print(f"LAPTOP SPECIFICATIONS")
        print(f"{'='*60}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"{'='*60}")
        print(f"Processor: {self.processor}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")
        print(f"Graphics: {self.graphics}")
        print(f"Display: {self.display_size}\" inches")
        print(f"Weight: {self.weight} kg")
        print(f"Price: ${self.price:,.2f}")
        print(f"{'='*60}\n")
    
    def display_brief_specs(self):
        """Display brief specifications"""
        print(f"{self.brand} {self.model:20} | {self.processor:25} | RAM: {self.ram:3}GB | Storage: {self.storage:4}GB | ${self.price:>10,.0f}")
    
    def get_performance_tier(self):
        """Get performance tier based on specs"""
        score = (self.ram / 16) * 40 + (self.storage / 1000) * 30
        if score >= 60:
            return "High Performance"
        elif score >= 40:
            return "Mid Range"
        else:
            return "Budget"
    
    def calculate_value_for_money(self):
        """Calculate value for money score"""
        # Simple calculation based on specs
        performance_score = (self.ram + self.storage/100) * 100 / self.price
        return performance_score
    
    def is_gaming_laptop(self):
        """Check if it's a gaming laptop"""
        gaming_indicators = ["GTX", "RTX", "Radeon", "Gaming", "Omen", "ROG"]
        return any(indicator in self.graphics for indicator in gaming_indicators)
    
    def is_ultrabook(self):
        """Check if it's an ultrabook"""
        return self.weight < 1.5 and self.display_size <= 13.3
    
    def display_detailed_specs(self):
        """Display detailed specifications with analysis"""
        print(f"\n{'='*60}")
        print(f"DETAILED LAPTOP ANALYSIS")
        print(f"{'='*60}")
        self.display_specifications()
        print(f"Performance Tier: {self.get_performance_tier()}")
        print(f"Value for Money Score: {self.calculate_value_for_money():.2f}")
        if self.is_gaming_laptop():
            print(f"Type: Gaming Laptop ★")
        if self.is_ultrabook():
            print(f"Type: Ultrabook (Portable) ★")
        print(f"{'='*60}\n")


# Create laptop objects using __init__()
print("LAPTOP INVENTORY\n")

laptop1 = Laptop("Dell", "XPS 13", "Intel Core i7-13th Gen", 16, 512, "Intel Iris Xe", 13.3, 1.2, 1499.99)
laptop2 = Laptop("HP", "Pavilion 15", "AMD Ryzen 5 5600H", 8, 256, "AMD Radeon", 15.6, 1.8, 599.99)
laptop3 = Laptop("ASUS", "ROG Gaming", "Intel Core i9-12th Gen", 32, 1024, "NVIDIA RTX 3080", 15.6, 2.5, 2499.99)
laptop4 = Laptop("MacBook", "Air M1", "Apple M1 Chip", 8, 256, "Apple Graphics", 13.3, 1.29, 999.99)
laptop5 = Laptop("Lenovo", "ThinkPad X1", "Intel Core i5-12th Gen", 16, 512, "Intel Iris", 14.0, 1.3, 1199.99)
laptop6 = Laptop("Acer", "Aspire 5", "AMD Ryzen 7 5700U", 16, 512, "AMD Radeon", 15.6, 1.9, 799.99)

# Display detailed specifications
print("DETAILED SPECIFICATIONS")
print("=" * 60)
laptop1.display_detailed_specs()
laptop2.display_detailed_specs()
laptop3.display_detailed_specs()

# Display brief specs
print("\nLAPTOP COMPARISON")
print("=" * 60)
print(f"{'Brand & Model':<25} | {'Processor':<27} | {'RAM':<6} | {'Storage':<10} | {'Price':<12}")
print("-" * 95)
laptop1.display_brief_specs()
laptop2.display_brief_specs()
laptop3.display_brief_specs()
laptop4.display_brief_specs()
laptop5.display_brief_specs()
laptop6.display_brief_specs()

# Gaming vs Non-Gaming
print("\n\nLAPTOP CATEGORY ANALYSIS")
print("=" * 60)
all_laptops = [laptop1, laptop2, laptop3, laptop4, laptop5, laptop6]

print("Gaming Laptops:")
for laptop in all_laptops:
    if laptop.is_gaming_laptop():
        print(f"  - {laptop.brand} {laptop.model}")

print("\nUltrabooks (Portable):")
for laptop in all_laptops:
    if laptop.is_ultrabook():
        print(f"  - {laptop.brand} {laptop.model}")

print("\nPerformance Tier Breakdown:")
tiers = {}
for laptop in all_laptops:
    tier = laptop.get_performance_tier()
    tiers[tier] = tiers.get(tier, 0) + 1

for tier, count in sorted(tiers.items()):
    print(f"  {tier}: {count} laptop(s)")

# Best value for money
print("\n\nBEST VALUE FOR MONEY")
print("=" * 60)
best_value = max(all_laptops, key=lambda l: l.calculate_value_for_money())
print(f"{best_value.brand} {best_value.model}")
print(f"Value Score: {best_value.calculate_value_for_money():.2f}")
print(f"Price: ${best_value.price:,.2f}")
