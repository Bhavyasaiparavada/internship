# Question 9: Create an Employee class with a method to calculate annual salary.

class EmployeeSalary:
    def __init__(self, emp_name, emp_id, monthly_salary, designation, bonus_percentage=0):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.monthly_salary = monthly_salary
        self.designation = designation
        self.bonus_percentage = bonus_percentage
    
    def calculate_annual_salary(self):
        annual_salary = self.monthly_salary * 12
        return annual_salary
    
    def calculate_salary_with_bonus(self):
        annual_salary = self.calculate_annual_salary()
        bonus = (annual_salary * self.bonus_percentage) / 100
        total_salary = annual_salary + bonus
        return total_salary
    
    def calculate_monthly_with_bonus(self):
        monthly = self.monthly_salary
        bonus = (monthly * self.bonus_percentage) / 100
        return monthly + bonus
    
    def display_salary_info(self):
        print(f"\nEmployee Information:")
        print(f"{'='*50}")
        print(f"Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Designation: {self.designation}")
        print(f"Monthly Salary: ${self.monthly_salary:,.2f}")
        print(f"Bonus Percentage: {self.bonus_percentage}%")
        print(f"{'='*50}")
        print(f"Annual Salary (Base): ${self.calculate_annual_salary():,.2f}")
        print(f"Annual Salary (with Bonus): ${self.calculate_salary_with_bonus():,.2f}")
        print(f"Monthly Salary (with Bonus): ${self.calculate_monthly_with_bonus():,.2f}")
        if self.bonus_percentage > 0:
            bonus_amount = (self.calculate_annual_salary() * self.bonus_percentage) / 100
            print(f"Annual Bonus Amount: ${bonus_amount:,.2f}")
        print(f"{'='*50}\n")
    
    def set_bonus(self, bonus_percentage):
        self.bonus_percentage = bonus_percentage
        print(f"Bonus percentage updated to {bonus_percentage}% for {self.emp_name}")


# Create employee objects
emp1 = EmployeeSalary("John Doe", "E001", 5000, "Senior Manager", 15)
emp2 = EmployeeSalary("Sarah Williams", "E002", 4000, "Software Developer", 10)
emp3 = EmployeeSalary("Mike Johnson", "E003", 3500, "Analyst", 8)
emp4 = EmployeeSalary("Emma Davis", "E004", 3800, "Designer", 10)
emp5 = EmployeeSalary("Robert Brown", "E005", 3200, "Junior Developer", 5)

# Display salary information
print("EMPLOYEE SALARY INFORMATION")
print("=" * 50)

emp1.display_salary_info()
emp2.display_salary_info()
emp3.display_salary_info()
emp4.display_salary_info()
emp5.display_salary_info()

# Salary comparison
print("\nSALARY COMPARISON")
print("=" * 50)
print(f"{'Employee':<20} {'Annual Salary':<20} {'With Bonus':<20}")
print("-" * 60)
print(f"{emp1.emp_name:<20} ${emp1.calculate_annual_salary():<19,.2f} ${emp1.calculate_salary_with_bonus():<19,.2f}")
print(f"{emp2.emp_name:<20} ${emp2.calculate_annual_salary():<19,.2f} ${emp2.calculate_salary_with_bonus():<19,.2f}")
print(f"{emp3.emp_name:<20} ${emp3.calculate_annual_salary():<19,.2f} ${emp3.calculate_salary_with_bonus():<19,.2f}")
print(f"{emp4.emp_name:<20} ${emp4.calculate_annual_salary():<19,.2f} ${emp4.calculate_salary_with_bonus():<19,.2f}")
print(f"{emp5.emp_name:<20} ${emp5.calculate_annual_salary():<19,.2f} ${emp5.calculate_salary_with_bonus():<19,.2f}")

# Total payroll
total_annual = (emp1.calculate_annual_salary() + emp2.calculate_annual_salary() + 
                emp3.calculate_annual_salary() + emp4.calculate_annual_salary() + 
                emp5.calculate_annual_salary())
total_with_bonus = (emp1.calculate_salary_with_bonus() + emp2.calculate_salary_with_bonus() + 
                    emp3.calculate_salary_with_bonus() + emp4.calculate_salary_with_bonus() + 
                    emp5.calculate_salary_with_bonus())

print("-" * 60)
print(f"{'TOTAL PAYROLL':<20} ${total_annual:<19,.2f} ${total_with_bonus:<19,.2f}")
