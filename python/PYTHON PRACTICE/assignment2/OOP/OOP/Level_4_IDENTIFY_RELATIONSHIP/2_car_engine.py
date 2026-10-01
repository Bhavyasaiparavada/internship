class Engine:
    pass


class Car:
    def __init__(self):
        self.engine = Engine()


print("HAS-A: Car has an Engine")
print(isinstance(Car().engine, Engine))
