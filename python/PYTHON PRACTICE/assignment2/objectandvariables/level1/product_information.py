class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity


product = Product("Wireless Mouse", 1200, 2)
print("Product:", product.product_name)
print("Price: Rs.", product.price)
print("Quantity:", product.quantity)
print("Total: Rs.", product.price * product.quantity)
