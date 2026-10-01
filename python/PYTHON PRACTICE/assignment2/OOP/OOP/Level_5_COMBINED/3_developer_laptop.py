class Employee:
    def __init__(self, name):
        self.name = name


class Laptop:
    def __init__(self, model):
        self.model = model


class Developer(Employee):
    def __init__(self, name, laptop):
        super().__init__(name)
        self.laptop = laptop


developer = Developer("Ravi", Laptop("Model X"))
print(developer.name, "uses", developer.laptop.model)
