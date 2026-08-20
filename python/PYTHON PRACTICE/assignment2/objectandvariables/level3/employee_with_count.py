# Question 8: Create an Employee class with class variables company_name and employee_count.

class EmployeeManagement:
    company_name = "Innovation Solutions"
    employee_count = 0
    
    def __init__(self, emp_name, emp_id, position, salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.position = position
        self.salary = salary
        EmployeeManagement.employee_count += 1
    
    def display_employee_info(self):
        print(f"Company: {EmployeeManagement.company_name}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")
        print("-" * 40)
    
    @classmethod
    def get_company_info(cls):
        print(f"Company: {cls.company_name}")
        print(f"Total Employees: {cls.employee_count}")
    
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name


# Create employee objects
print("Creating employees...\n")

emp1 = EmployeeManagement("John Doe", "E001", "Manager", 75000)
emp1.display_employee_info()

emp2 = EmployeeManagement("Sarah Williams", "E002", "Developer", 65000)
emp2.display_employee_info()

emp3 = EmployeeManagement("Mike Johnson", "E003", "Designer", 60000)
emp3.display_employee_info()

emp4 = EmployeeManagement("Emma Davis", "E004", "Analyst", 55000)
emp4.display_employee_info()

emp5 = EmployeeManagement("Robert Brown", "E005", "Developer", 65000)
emp5.display_employee_info()

# Display company information
print("\n--- Company Information ---")
EmployeeManagement.get_company_info()

# Create more employees
print("\n--- Adding More Employees ---")
emp6 = EmployeeManagement("Lisa Anderson", "E006", "HR Manager", 70000)
emp7 = EmployeeManagement("Tom Martinez", "E007", "QA Engineer", 62000)

print("\n--- Updated Company Information ---")
EmployeeManagement.get_company_info()

# Change company name
print("\n--- Changing Company Name ---")
EmployeeManagement.change_company_name("Tech Innovations Inc.")
EmployeeManagement.get_company_info()
