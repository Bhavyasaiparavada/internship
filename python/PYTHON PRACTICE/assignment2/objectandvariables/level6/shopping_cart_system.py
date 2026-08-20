# Question 9: Create a ShoppingCart class with methods to add products, remove products, and calculate the total.

class ShoppingCart:
    def __init__(self, customer_name=""):
        """Initialize shopping cart"""
        self.customer_name = customer_name
        self.items = []
    
    def add_product(self, product_name, price, quantity):
        """
        Add product to cart
        Method accepts product details and adds to cart
        """
        if price <= 0 or quantity <= 0:
            print("Error: Price and quantity must be positive!")
            return False
        
        # Check if product already exists
        for item in self.items:
            if item["name"].lower() == product_name.lower():
                item["quantity"] += quantity
                print(f"✓ Updated {product_name}: Quantity now {item['quantity']}")
                return True
        
        # Add new product
        product = {
            "name": product_name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(product)
        print(f"✓ Added {product_name} to cart (Qty: {quantity})")
        return True
    
    def remove_product(self, product_name):
        """
        Remove product from cart
        Method accepts product name and removes it
        """
        for i, item in enumerate(self.items):
            if item["name"].lower() == product_name.lower():
                removed = self.items.pop(i)
                print(f"✓ Removed {removed['name']} from cart")
                return True
        
        print(f"Error: {product_name} not found in cart")
        return False
    
    def update_quantity(self, product_name, new_quantity):
        """Update quantity of a product"""
        if new_quantity <= 0:
            return self.remove_product(product_name)
        
        for item in self.items:
            if item["name"].lower() == product_name.lower():
                old_qty = item["quantity"]
                item["quantity"] = new_quantity
                print(f"✓ Updated {product_name}: {old_qty} → {new_quantity}")
                return True
        
        print(f"Error: {product_name} not found in cart")
        return False
    
    def calculate_subtotal(self):
        """Calculate subtotal without tax"""
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def calculate_tax(self, tax_rate=10):
        """Calculate tax amount"""
        subtotal = self.calculate_subtotal()
        return (subtotal * tax_rate) / 100
    
    def calculate_total(self, tax_rate=10):
        """
        Calculate total price
        Method calculates cart total with tax
        """
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(tax_rate)
        return subtotal + tax
    
    def apply_discount(self, discount_percentage):
        """Apply discount to entire cart"""
        subtotal = self.calculate_subtotal()
        discount = (subtotal * discount_percentage) / 100
        return subtotal - discount
    
    def display_cart(self):
        """Display cart contents"""
        print(f"\n{'='*70}")
        print(f"SHOPPING CART - {self.customer_name}")
        print(f"{'='*70}")
        
        if len(self.items) == 0:
            print("Cart is empty!")
        else:
            print(f"{'Product Name':<25} {'Price':<12} {'Quantity':<10} {'Subtotal':<15}")
            print("-" * 70)
            
            for item in self.items:
                subtotal = item["price"] * item["quantity"]
                print(f"{item['name']:<25} ${item['price']:<11,.2f} {item['quantity']:<10} ${subtotal:<14,.2f}")
            
            print("-" * 70)
            print(f"Total Items: {sum(item['quantity'] for item in self.items)}")
        
        print(f"{'='*70}\n")
    
    def display_bill(self, tax_rate=10, discount_percentage=0):
        """Display complete bill"""
        self.display_cart()
        
        subtotal = self.calculate_subtotal()
        discount_amount = (subtotal * discount_percentage) / 100
        after_discount = subtotal - discount_amount
        tax = (after_discount * tax_rate) / 100
        total = after_discount + tax
        
        print(f"{'='*70}")
        print(f"BILLING DETAILS")
        print(f"{'='*70}")
        print(f"Subtotal: ${subtotal:>15,.2f}")
        if discount_percentage > 0:
            print(f"Discount ({discount_percentage}%): ${discount_amount:>10,.2f}")
            print(f"After Discount: ${after_discount:>13,.2f}")
        print(f"Tax ({tax_rate}%): ${tax:>19,.2f}")
        print(f"{'='*70}")
        print(f"TOTAL: ${total:>24,.2f}")
        print(f"{'='*70}\n")
    
    def get_item_count(self):
        """Get total number of items in cart"""
        return len(self.items)
    
    def clear_cart(self):
        """Clear all items from cart"""
        self.items = []
        print("✓ Cart cleared")


# Create shopping cart
print("SHOPPING CART SYSTEM\n")

cart = ShoppingCart("John Smith")

# Add products
print("ADDING PRODUCTS TO CART")
print("=" * 70 + "\n")

cart.add_product("Laptop", 1200.00, 1)
cart.add_product("Mouse", 45.00, 2)
cart.add_product("Keyboard", 120.00, 1)
cart.add_product("Monitor", 350.00, 1)
cart.add_product("USB Cable", 15.00, 3)

print()

# Display cart
cart.display_cart()

# Calculate totals
print("CART SUMMARY")
print("=" * 70)
print(f"Number of Items: {cart.get_item_count()}")
print(f"Subtotal: ${cart.calculate_subtotal():,.2f}")
print(f"Tax (10%): ${cart.calculate_tax(10):,.2f}")
print(f"Total: ${cart.calculate_total(10):,.2f}")
print()

# Update quantity
print("\nUPDATING QUANTITIES")
print("=" * 70 + "\n")
cart.update_quantity("Mouse", 3)
cart.update_quantity("USB Cable", 5)

print()

# Display updated cart
cart.display_cart()

# Remove product
print("REMOVING PRODUCTS")
print("=" * 70 + "\n")
cart.remove_product("Monitor")

print()

# Display bill with tax and discount
print("\nBILL WITH TAX AND DISCOUNT")
print("=" * 70)
cart.display_bill(tax_rate=10, discount_percentage=5)

# Create another cart
print("\n\nANOTHER SHOPPING SESSION")
print("=" * 70 + "\n")

cart2 = ShoppingCart("Sarah Johnson")

# Add products
cart2.add_product("Book", 25.00, 2)
cart2.add_product("Pen", 5.00, 10)
cart2.add_product("Notebook", 15.00, 3)

print()

# Display bill
cart2.display_bill(tax_rate=8, discount_percentage=0)

# Final summary
print("PAYMENT SUMMARY")
print("=" * 70)
total_cart1 = cart.calculate_total(10)
total_cart2 = cart2.calculate_total(8)
print(f"Cart 1 Total: ${total_cart1:,.2f}")
print(f"Cart 2 Total: ${total_cart2:,.2f}")
print(f"Combined Total: ${total_cart1 + total_cart2:,.2f}")
