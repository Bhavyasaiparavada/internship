class Employee:
    company_name = "Bright Solutions"

    def __init__(self, name):
        self.name = name


employees = [Employee("Asha"), Employee("Ravi"), Employee("Mina")]
for employee in employees:
    print(employee.name, employee.company_name)