class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append([name, price, quantity])

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                return

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product[1] * product[2]
        return total


cart = ShoppingCart()
cart.add_product("Book", 100, 2)
cart.add_product("Pen", 10, 3)
cart.remove_product("Pen")
print("Cart total:", cart.calculate_total())