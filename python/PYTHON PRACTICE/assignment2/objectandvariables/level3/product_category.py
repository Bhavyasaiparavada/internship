# Question 5: Create a Product class with a class variable category
# Create different product objects.

class Product:
    category = "Electronics"
    
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
    
    def display_product_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Category: {Product.category}")
        print(f"Price: ${self.price}")
        print("-" * 40)
    
    @classmethod
    def change_category(cls, new_category):
        cls.category = new_category
        print(f"Category changed to: {cls.category}")


# Create different product objects
product1 = Product("P001", "Laptop", 1200.00)
product2 = Product("P002", "Smartphone", 800.00)
product3 = Product("P003", "Tablet", 500.00)
product4 = Product("P004", "Headphones", 150.00)

# Display product information
print(f"Category: {Product.category}\n")
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()
product4.display_product_info()

# Change category for all products
print("\n--- Changing Category ---")
Product.change_category("Mobile Devices")

print("\n--- Updated Products ---")
product1.display_product_info()
product2.display_product_info()
