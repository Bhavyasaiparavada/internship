class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id


employee = Employee("Asha", 101)
print(employee.name, employee.employee_id)