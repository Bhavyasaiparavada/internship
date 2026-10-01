class Product:
    category = "General"

    def __init__(self, name):
        self.name = name


products = [Product("Notebook"), Product("Water bottle")]
for product in products:
    print(product.name, product.category)