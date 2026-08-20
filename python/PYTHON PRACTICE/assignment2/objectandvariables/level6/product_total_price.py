# Question 5: Create a Product class with a method that accepts quantity and returns the total price.

class Product:
    def __init__(self, product_id, product_name, unit_price):
        """Initialize product"""
        self.product_id = product_id
        self.product_name = product_name
        self.unit_price = unit_price
    
    def calculate_total_price(self, quantity):
        """
        Accept quantity and return the total price
        Method accepts quantity as parameter and returns total cost
        """
        if quantity <= 0:
            print("Error: Quantity must be positive!")
            return 0
        
        total_price = self.unit_price * quantity
        return total_price
    
    def calculate_price_with_tax(self, quantity, tax_rate=10):
        """Calculate total price with tax"""
        total_price = self.calculate_total_price(quantity)
        tax = (total_price * tax_rate) / 100
        return total_price + tax
    
    def calculate_price_with_discount(self, quantity, discount_percentage=0):
        """Calculate total price with discount"""
        total_price = self.calculate_total_price(quantity)
        discount = (total_price * discount_percentage) / 100
        return total_price - discount
    
    def apply_bulk_discount(self, quantity):
        """Apply automatic bulk discount based on quantity"""
        if quantity >= 100:
            discount_rate = 15
        elif quantity >= 50:
            discount_rate = 10
        elif quantity >= 20:
            discount_rate = 5
        else:
            discount_rate = 0
        
        total_price = self.calculate_total_price(quantity)
        discount = (total_price * discount_rate) / 100
        final_price = total_price - discount
        
        return final_price, discount_rate, discount
    
    def display_price_breakdown(self, quantity, discount=0, tax=10):
        """Display detailed price breakdown"""
        subtotal = self.calculate_total_price(quantity)
        discount_amount = (subtotal * discount) / 100
        after_discount = subtotal - discount_amount
        tax_amount = (after_discount * tax) / 100
        total = after_discount + tax_amount
        
        print(f"\n{'='*60}")
        print(f"Price Breakdown - {self.product_name}")
        print(f"{'='*60}")
        print(f"Product ID: {self.product_id}")
        print(f"Unit Price: ${self.unit_price:,.2f}")
        print(f"Quantity: {quantity}")
        print(f"{'='*60}")
        print(f"Subtotal: ${subtotal:,.2f}")
        if discount > 0:
            print(f"Discount ({discount}%): -${discount_amount:,.2f}")
            print(f"After Discount: ${after_discount:,.2f}")
        print(f"Tax ({tax}%): ${tax_amount:,.2f}")
        print(f"{'='*60}")
        print(f"Total Price: ${total:,.2f}")
        print(f"{'='*60}\n")
    
    def display_bulk_pricing(self, quantities):
        """Display bulk pricing for different quantities"""
        print(f"\nBulk Pricing - {self.product_name}")
        print(f"{'='*70}")
        print(f"{'Quantity':<15} {'Unit Price':<15} {'Total Price':<15} {'Discount':<15} {'Final Price':<15}")
        print("-" * 70)
        
        for qty in quantities:
            final_price, discount_rate, discount = self.apply_bulk_discount(qty)
            total = self.calculate_total_price(qty)
            print(f"{qty:<15} ${self.unit_price:<14,.2f} ${total:<14,.2f} {discount_rate}%{'':<11} ${final_price:<14,.2f}")
        
        print(f"{'='*70}\n")


# Create product objects
print("PRODUCT PRICING CALCULATOR\n")

product1 = Product("P001", "Laptop", 1200.00)
product2 = Product("P002", "Smartphone", 800.00)
product3 = Product("P003", "USB Cable", 15.00)

# Calculate total price for different quantities
print("PRICE CALCULATIONS FOR PRODUCT 1")
print("=" * 60)

qty = 3
total = product1.calculate_total_price(qty)
print(f"Quantity: {qty}")
print(f"Unit Price: ${product1.unit_price:,.2f}")
print(f"Total Price: ${total:,.2f}\n")

qty = 5
total = product1.calculate_total_price(qty)
print(f"Quantity: {qty}")
print(f"Unit Price: ${product1.unit_price:,.2f}")
print(f"Total Price: ${total:,.2f}\n")

# Detailed price breakdown
print("\nDETAILED PRICE BREAKDOWN")
print("=" * 60)
product1.display_price_breakdown(2, discount=10, tax=10)
product2.display_price_breakdown(4, discount=15, tax=10)
product3.display_price_breakdown(100, discount=0, tax=10)

# Bulk pricing
print("\nBULK PRICING")
print("=" * 60)
quantities = [10, 20, 50, 100, 150]
product1.display_bulk_pricing(quantities)
product2.display_bulk_pricing(quantities)
product3.display_bulk_pricing([10, 50, 100, 500, 1000])

# Price comparison
print("\nPRICE COMPARISON")
print("=" * 60)
qty = 20
print(f"\nFor {qty} units of {product1.product_name}:")
price_no_discount = product1.calculate_total_price(qty)
price_with_discount = product1.calculate_price_with_discount(qty, 10)
price_bulk = product1.apply_bulk_discount(qty)[0]

print(f"Regular Price: ${price_no_discount:,.2f}")
print(f"With 10% Discount: ${price_with_discount:,.2f}")
print(f"With Bulk Discount: ${price_bulk:,.2f}")
print(f"Savings (Bulk): ${price_no_discount - price_bulk:,.2f}")
