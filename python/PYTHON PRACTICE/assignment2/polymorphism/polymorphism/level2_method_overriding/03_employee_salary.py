class Employee:
    def calculate_salary(self):
        return 20000


class Manager(Employee):
    def calculate_salary(self):
        return 50000


class Developer(Employee):
    def calculate_salary(self):
        return 40000


manager = Manager()
developer = Developer()
print("Manager salary:", manager.calculate_salary())
print("Developer salary:", developer.calculate_salary())