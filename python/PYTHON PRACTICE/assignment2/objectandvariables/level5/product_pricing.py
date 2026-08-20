# Question 6: Create a Product class using __init__() and a method to calculate the total price.

class Product:
    def __init__(self, product_id, product_name, unit_price, quantity_in_stock, category):
        """Initialize product attributes"""
        self.product_id = product_id
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity_in_stock = quantity_in_stock
        self.category = category
    
    def calculate_total_price(self, quantity):
        """Calculate total price for given quantity"""
        if quantity <= 0:
            print("Error: Quantity must be positive!")
            return 0
        if quantity > self.quantity_in_stock:
            print(f"Error: Not enough stock! Available: {self.quantity_in_stock}")
            return 0
        return self.unit_price * quantity
    
    def calculate_total_inventory_value(self):
        """Calculate total inventory value"""
        return self.unit_price * self.quantity_in_stock
    
    def apply_discount(self, quantity, discount_percentage):
        """Calculate price with discount"""
        total_price = self.calculate_total_price(quantity)
        if total_price > 0:
            discount_amount = (total_price * discount_percentage) / 100
            final_price = total_price - discount_amount
            return final_price, discount_amount
        return 0, 0
    
    def display_product_info(self):
        """Display product information"""
        print(f"\n{'='*50}")
        print(f"Product Information:")
        print(f"{'='*50}")
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Category: {self.category}")
        print(f"Unit Price: ${self.unit_price:,.2f}")
        print(f"Quantity in Stock: {self.quantity_in_stock}")
        print(f"Total Inventory Value: ${self.calculate_total_inventory_value():,.2f}")
        print(f"{'='*50}\n")
    
    def purchase(self, quantity):
        """Purchase product"""
        total = self.calculate_total_price(quantity)
        if total > 0:
            self.quantity_in_stock -= quantity
            print(f"✓ Purchase successful!")
            print(f"  Product: {self.product_name}")
            print(f"  Quantity: {quantity}")
            print(f"  Unit Price: ${self.unit_price:,.2f}")
            print(f"  Total Price: ${total:,.2f}")
            print(f"  Remaining Stock: {self.quantity_in_stock}\n")
    
    def add_stock(self, quantity):
        """Add stock to inventory"""
        self.quantity_in_stock += quantity
        print(f"✓ Stock added: {quantity} units of {self.product_name}")
        print(f"  New Stock: {self.quantity_in_stock}\n")


# Create product objects using __init__()
print("PRODUCT MANAGEMENT SYSTEM\n")

product1 = Product("P001", "Laptop", 1200.00, 25, "Electronics")
product2 = Product("P002", "Smartphone", 800.00, 40, "Electronics")
product3 = Product("P003", "USB Cable", 15.00, 500, "Accessories")
product4 = Product("P004", "Monitor", 350.00, 15, "Electronics")
product5 = Product("P005", "Keyboard", 120.00, 60, "Accessories")

# Display product information
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()

# Calculate total price for different quantities
print("PRICE CALCULATIONS")
print("=" * 50)

print(f"\n{product1.product_name}:")
qty = 3
total = product1.calculate_total_price(qty)
print(f"  Quantity: {qty}")
print(f"  Total Price: ${total:,.2f}")
final_price, discount = product1.apply_discount(qty, 10)
print(f"  Price with 10% discount: ${final_price:,.2f} (Discount: ${discount:,.2f})")

print(f"\n{product2.product_name}:")
qty = 2
total = product2.calculate_total_price(qty)
print(f"  Quantity: {qty}")
print(f"  Total Price: ${total:,.2f}")
final_price, discount = product2.apply_discount(qty, 15)
print(f"  Price with 15% discount: ${final_price:,.2f} (Discount: ${discount:,.2f})")

print(f"\n{product3.product_name}:")
qty = 100
total = product3.calculate_total_price(qty)
print(f"  Quantity: {qty}")
print(f"  Total Price: ${total:,.2f}")
final_price, discount = product3.apply_discount(qty, 5)
print(f"  Price with 5% discount: ${final_price:,.2f} (Discount: ${discount:,.2f})")

# Purchase products
print("\n\nPURCHASES")
print("=" * 50 + "\n")
product1.purchase(2)
product2.purchase(3)
product3.purchase(50)
product4.purchase(1)

# Add stock
print("ADD STOCK")
print("=" * 50 + "\n")
product1.add_stock(10)
product2.add_stock(5)

# Display final inventory
print("\nFINAL INVENTORY")
print("=" * 50)
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()
