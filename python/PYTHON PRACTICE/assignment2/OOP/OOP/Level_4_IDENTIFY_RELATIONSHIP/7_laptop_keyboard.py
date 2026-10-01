class Keyboard:
    pass


class Laptop:
    def __init__(self):
        self.keyboard = Keyboard()


print("HAS-A: Laptop has a Keyboard")
print(isinstance(Laptop().keyboard, Keyboard))
