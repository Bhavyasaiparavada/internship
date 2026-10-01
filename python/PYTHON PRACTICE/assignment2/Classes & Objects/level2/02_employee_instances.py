class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary


employees = [
    Employee("Asha", "Sales", 35000),
    Employee("Ravi", "IT", 45000),
    Employee("Mina", "HR", 40000),
    Employee("Omar", "Finance", 42000),
    Employee("Lia", "Support", 32000),
]
for employee in employees:
    print(employee.name, employee.department, employee.salary)