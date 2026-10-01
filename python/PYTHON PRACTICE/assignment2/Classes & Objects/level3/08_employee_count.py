class Employee:
    company_name = "Bright Solutions"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1


employees = [Employee("Asha"), Employee("Ravi"), Employee("Mina")]
print("Company:", Employee.company_name)
print("Employees:", Employee.employee_count)