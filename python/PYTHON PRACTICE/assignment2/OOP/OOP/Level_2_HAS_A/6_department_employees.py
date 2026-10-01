class Employee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self):
        self.employees = [Employee("Asha"), Employee("Ravi")]


department = Department()
for employee in department.employees:
    print(employee.name)
