class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary


employees = [
    Employee("Aarav Sharma", "Development", 65000),
    Employee("Ishita Rao", "Human Resources", 58000),
    Employee("Kabir Mehta", "Marketing", 62000),
    Employee("Nisha Verma", "Finance", 70000),
    Employee("Vikram Das", "Design", 60000),
]

for employee in employees:
    print("Name:", employee.name)
    print("Department:", employee.department)
    print("Salary: Rs.", employee.salary)
    print()
