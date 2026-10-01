class ShoppingCart:
    def __init__(self, items=None):
        self.items = items or []

    def __add__(self, other):
        return ShoppingCart(self.items + other.items)


cart1 = ShoppingCart(["Pen", "Book"])
cart2 = ShoppingCart(["Bag"])
combined_cart = cart1 + cart2
print("Items:", combined_cart.items)