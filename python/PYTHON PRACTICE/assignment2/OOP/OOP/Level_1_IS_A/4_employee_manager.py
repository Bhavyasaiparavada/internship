class Employee:
    def __init__(self, name):
        self.name = name


class Manager(Employee):
    def manage(self):
        print(self.name, "manages the team")


manager = Manager("Ravi")
manager.manage()
