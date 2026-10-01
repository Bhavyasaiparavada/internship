class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def work(self):
        print(self.name, "writes code")


class Tester(Employee):
    def work(self):
        print(self.name, "tests software")


class Manager(Employee):
    def work(self):
        print(self.name, "manages a team")


for employee in (Developer("Asha"), Tester("Ravi"), Manager("Mina")):
    employee.work()
