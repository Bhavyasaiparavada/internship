class Employee:
    def __init__(self, name):
        self.name = name


class Company:
    def __init__(self):
        self.employees = [Employee("Asha"), Employee("Ravi")]


print("HAS-A: Company has Employees")
print([employee.name for employee in Company().employees])
