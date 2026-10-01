class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print(self.name, "earns", self.salary)


employee = Employee("Ravi", 45000)
employee.display_salary()