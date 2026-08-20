# Question 2: Create an Employee class using __init__() to initialize employee ID, name, department, and salary.

class Employee:
    def __init__(self, emp_id, name, department, salary):
        """Initialize employee attributes"""
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
    
    def display_info(self):
        """Display employee information"""
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:,.2f}")
        print("-" * 40)
    
    def calculate_annual_salary(self):
        """Calculate annual salary"""
        return self.salary * 12
    
    def give_raise(self, raise_percentage):
        """Give salary raise"""
        raise_amount = (self.salary * raise_percentage) / 100
        self.salary += raise_amount
        print(f"✓ Raise of {raise_percentage}% given to {self.name}")
        print(f"  New Salary: ${self.salary:,.2f}")
    
    def display_summary(self):
        """Display employee summary"""
        print(f"\n{self.name} ({self.emp_id})")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: ${self.salary:,.2f}")
        print(f"Annual Salary: ${self.calculate_annual_salary():,.2f}")


# Create employee objects using __init__()
print("EMPLOYEE INFORMATION\n")

emp1 = Employee("E001", "John Doe", "IT", 5000)
emp2 = Employee("E002", "Sarah Williams", "HR", 4500)
emp3 = Employee("E003", "Mike Johnson", "Finance", 5500)
emp4 = Employee("E004", "Emma Davis", "Marketing", 4200)
emp5 = Employee("E005", "Robert Brown", "IT", 4800)

# Display information
emp1.display_info()
emp2.display_info()
emp3.display_info()
emp4.display_info()
emp5.display_info()

# Display summaries
print("\nEMPLOYEE SUMMARY")
print("=" * 40)
emp1.display_summary()
emp2.display_summary()
emp3.display_summary()

# Give raises
print("\n" + "=" * 40)
print("SALARY INCREMENT")
print("=" * 40 + "\n")
emp1.give_raise(10)
emp2.give_raise(8)
emp3.give_raise(12)

# Display updated summaries
print("\nUPDATED SUMMARIES")
print("=" * 40)
emp1.display_summary()
emp2.display_summary()
emp3.display_summary()
