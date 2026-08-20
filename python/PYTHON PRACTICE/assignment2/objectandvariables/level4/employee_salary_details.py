# Question 2: Create an Employee class with a method display_salary() to display employee salary.

class Employee:
    def __init__(self, emp_name, emp_id, position, salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.position = position
        self.salary = salary
    
    def display_salary(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:,.2f}")
        print("-" * 40)
    
    def display_info(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Position: {self.position}")
        print(f"Annual Salary: ${self.salary:,.2f}")


# Create employee objects and display salary
emp1 = Employee("John Doe", "E001", "Manager", 75000)
emp2 = Employee("Sarah Williams", "E002", "Developer", 65000)
emp3 = Employee("Mike Johnson", "E003", "Analyst", 55000)
emp4 = Employee("Emma Davis", "E004", "Designer", 60000)

print("Employee Salary Information:\n")
emp1.display_salary()
emp2.display_salary()
emp3.display_salary()
emp4.display_salary()
