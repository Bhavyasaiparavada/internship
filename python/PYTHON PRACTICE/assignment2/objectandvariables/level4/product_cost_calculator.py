# Question 10: Create a Product class with a method to calculate the total cost based on price and quantity.

class Product:
    def __init__(self, product_id, product_name, price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category = category
        self.quantity_in_stock = 0
    
    def calculate_total_cost(self, quantity):
        """Calculate total cost based on price and quantity"""
        if quantity < 0:
            print("Error: Quantity cannot be negative!")
            return 0
        total_cost = self.price * quantity
        return total_cost
    
    def calculate_total_cost_with_tax(self, quantity, tax_percentage=10):
        """Calculate total cost with tax"""
        subtotal = self.calculate_total_cost(quantity)
        tax = (subtotal * tax_percentage) / 100
        total = subtotal + tax
        return total, tax
    
    def calculate_total_inventory_value(self):
        """Calculate total value of inventory"""
        return self.price * self.quantity_in_stock
    
    def calculate_discount_price(self, quantity, discount_percentage=0):
        """Calculate price with discount"""
        subtotal = self.calculate_total_cost(quantity)
        discount = (subtotal * discount_percentage) / 100
        final_price = subtotal - discount
        return final_price, discount
    
    def add_to_inventory(self, quantity):
        """Add items to inventory"""
        self.quantity_in_stock += quantity
        print(f"✓ Added {quantity} units to inventory. Total stock: {self.quantity_in_stock}")
    
    def remove_from_inventory(self, quantity):
        """Remove items from inventory"""
        if quantity <= self.quantity_in_stock:
            self.quantity_in_stock -= quantity
            print(f"✓ Removed {quantity} units from inventory. Remaining stock: {self.quantity_in_stock}")
        else:
            print(f"Error: Not enough stock! (Available: {self.quantity_in_stock})")
    
    def display_product_info(self):
        print(f"\nProduct: {self.product_name}")
        print(f"ID: {self.product_id}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.price:,.2f}")
        print(f"Stock Available: {self.quantity_in_stock} units")
        print(f"Inventory Value: ${self.calculate_total_inventory_value():,.2f}")
        print("-" * 50)
    
    def display_cost_breakdown(self, quantity):
        print(f"\nProduct: {self.product_name}")
        print(f"Quantity: {quantity} units")
        print(f"Unit Price: ${self.price:,.2f}")
        print("-" * 50)
        
        # Basic cost
        basic_cost = self.calculate_total_cost(quantity)
        print(f"Subtotal (without tax): ${basic_cost:,.2f}")
        
        # Cost with tax
        cost_with_tax, tax = self.calculate_total_cost_with_tax(quantity, 10)
        print(f"Tax (10%): ${tax:,.2f}")
        print(f"Total (with tax): ${cost_with_tax:,.2f}")
        
        # Cost with discount
        cost_with_discount, discount = self.calculate_discount_price(quantity, 15)
        print(f"Discount (15%): ${discount:,.2f}")
        print(f"Final Price (with discount): ${cost_with_discount:,.2f}")
        print("-" * 50)


# Create product objects
product1 = Product("P001", "Laptop", 1200.00, "Electronics")
product2 = Product("P002", "Smartphone", 800.00, "Electronics")
product3 = Product("P003", "USB Cable", 15.00, "Accessories")
product4 = Product("P004", "Monitor", 350.00, "Electronics")
product5 = Product("P005", "Keyboard", 120.00, "Accessories")

# Add items to inventory
print("Adding products to inventory:\n")
product1.add_to_inventory(25)
product2.add_to_inventory(40)
product3.add_to_inventory(500)
product4.add_to_inventory(15)
product5.add_to_inventory(60)

# Display product information
print("\n" + "="*50)
print("PRODUCT INFORMATION")
print("="*50)
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()
product4.display_product_info()
product5.display_product_info()

# Calculate costs for different quantities
print("\n" + "="*50)
print("COST CALCULATIONS")
print("="*50)

product1.display_cost_breakdown(5)
print()
product2.display_cost_breakdown(10)
print()
product3.display_cost_breakdown(100)

# Individual cost calculations
print("\n" + "="*50)
print("QUICK CALCULATIONS")
print("="*50)
print(f"\n{product1.product_name}:")
print(f"  Cost for 3 units: ${product1.calculate_total_cost(3):,.2f}")
print(f"  Cost for 3 units (with tax): ${product1.calculate_total_cost_with_tax(3)[0]:,.2f}")
print(f"  Cost for 3 units (with 20% discount): ${product1.calculate_discount_price(3, 20)[0]:,.2f}")

print(f"\n{product2.product_name}:")
print(f"  Cost for 2 units: ${product2.calculate_total_cost(2):,.2f}")
print(f"  Cost for 2 units (with tax): ${product2.calculate_total_cost_with_tax(2)[0]:,.2f}")

print(f"\n{product3.product_name}:")
print(f"  Cost for 50 units: ${product3.calculate_total_cost(50):,.2f}")
print(f"  Cost for 50 units (with 25% discount): ${product3.calculate_discount_price(50, 25)[0]:,.2f}")

# Inventory operations
print("\n" + "="*50)
print("INVENTORY OPERATIONS")
print("="*50 + "\n")
product1.remove_from_inventory(5)
product1.add_to_inventory(10)
product1.display_product_info()
