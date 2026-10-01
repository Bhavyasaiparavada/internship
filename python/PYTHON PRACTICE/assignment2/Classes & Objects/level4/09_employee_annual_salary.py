class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12


employee = Employee("Mina", 40000)
print(employee.name, "annual salary:", employee.annual_salary())