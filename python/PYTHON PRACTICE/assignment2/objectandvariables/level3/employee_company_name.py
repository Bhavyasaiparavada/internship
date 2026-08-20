# Question 2: Create an Employee class with a class variable company_name
# Display the company name for multiple employees.

class Employee:
    company_name = "TechCorp Inc."
    
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name
    
    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.emp_name}, Company: {Employee.company_name}")
    
    @classmethod
    def get_company_name(cls):
        return cls.company_name


# Create multiple employee objects
emp1 = Employee(101, "John")
emp2 = Employee(102, "Sarah")
emp3 = Employee(103, "Mike")
emp4 = Employee(104, "Emma")

# Display company name for each employee
emp1.display_info()
emp2.display_info()
emp3.display_info()
emp4.display_info()

# Display company name using class method
print(f"\nCompany Name (using class method): {Employee.get_company_name()}")
