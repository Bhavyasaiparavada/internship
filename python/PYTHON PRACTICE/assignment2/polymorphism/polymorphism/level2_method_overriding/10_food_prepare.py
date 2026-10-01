class Food:
    def prepare(self):
        print("Preparing food")


class Pizza(Food):
    def prepare(self):
        print("Bake the pizza")


class Burger(Food):
    def prepare(self):
        print("Cook the burger patty")


class Biryani(Food):
    def prepare(self):
        print("Cook rice with spices")


pizza = Pizza()
burger = Burger()
biryani = Biryani()
pizza.prepare()
burger.prepare()
biryani.prepare()