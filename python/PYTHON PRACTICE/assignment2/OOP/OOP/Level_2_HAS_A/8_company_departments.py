class Department:
    def __init__(self, name):
        self.name = name


class Company:
    def __init__(self):
        self.departments = [Department("Sales"), Department("IT")]


company = Company()
for department in company.departments:
    print(department.name)
