class InvalidProductError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, product, quantity):
        if not product.strip():
            raise InvalidProductError("Product name cannot be empty.")
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be positive.")
        self.items[product] = quantity


cart = ShoppingCart()
try:
    cart.add("Pencil", 3)
    print(cart.items)
except InvalidProductError as error:
    print(error)
except InvalidQuantityError as error:
    print(error)