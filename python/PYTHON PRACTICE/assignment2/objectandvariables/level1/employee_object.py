class Employee:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department


employee = Employee("Arun Kumar", "EMP101", "Development")
print("Employee name:", employee.name)
print("Employee ID:", employee.employee_id)
print("Department:", employee.department)
