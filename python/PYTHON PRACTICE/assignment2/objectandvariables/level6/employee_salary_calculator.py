# Question 6: Create an Employee class with a method that accepts working days and calculates salary.

class Employee:
    def __init__(self, emp_id, name, daily_rate):
        """Initialize employee"""
        self.emp_id = emp_id
        self.name = name
        self.daily_rate = daily_rate
    
    def calculate_salary(self, working_days):
        """
        Accept working days and calculate salary
        Method accepts working days as parameter and returns salary
        """
        if working_days < 0:
            print("Error: Working days cannot be negative!")
            return 0
        
        salary = self.daily_rate * working_days
        return salary
    
    def calculate_salary_with_overtime(self, working_days, overtime_hours=0):
        """Calculate salary with overtime"""
        base_salary = self.calculate_salary(working_days)
        overtime_rate = self.daily_rate / 8  # Assuming 8 hour workday
        overtime_pay = overtime_hours * overtime_rate * 1.5  # 1.5x rate for overtime
        total_salary = base_salary + overtime_pay
        return total_salary, overtime_pay
    
    def calculate_salary_with_deductions(self, working_days, deduction_percentage=0):
        """Calculate salary with deductions"""
        base_salary = self.calculate_salary(working_days)
        deduction = (base_salary * deduction_percentage) / 100
        net_salary = base_salary - deduction
        return net_salary, deduction
    
    def calculate_salary_with_bonus(self, working_days, bonus_percentage=0):
        """Calculate salary with bonus"""
        base_salary = self.calculate_salary(working_days)
        bonus = (base_salary * bonus_percentage) / 100
        total_salary = base_salary + bonus
        return total_salary, bonus
    
    def display_salary_details(self, working_days):
        """Display detailed salary information"""
        base_salary = self.calculate_salary(working_days)
        
        print(f"\n{'='*60}")
        print(f"SALARY CALCULATION")
        print(f"{'='*60}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Daily Rate: ${self.daily_rate:,.2f}")
        print(f"Working Days: {working_days}")
        print(f"{'='*60}")
        print(f"Base Salary: ${base_salary:,.2f}")
        print(f"{'='*60}\n")
    
    def display_salary_breakdown(self, working_days, overtime_hours=0, deduction=0, bonus=0):
        """Display complete salary breakdown"""
        base_salary = self.calculate_salary(working_days)
        
        overtime_rate = self.daily_rate / 8
        overtime_pay = overtime_hours * overtime_rate * 1.5
        
        deduction_amount = (base_salary * deduction) / 100
        bonus_amount = (base_salary * bonus) / 100
        
        total = base_salary + overtime_pay - deduction_amount + bonus_amount
        
        print(f"\n{'='*60}")
        print(f"DETAILED SALARY BREAKDOWN - {self.name}")
        print(f"{'='*60}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Daily Rate: ${self.daily_rate:,.2f}")
        print(f"{'='*60}")
        print(f"Base Salary ({working_days} days): ${base_salary:,.2f}")
        if overtime_hours > 0:
            print(f"Overtime ({overtime_hours}h @ 1.5x): ${overtime_pay:,.2f}")
        if bonus > 0:
            print(f"Bonus ({bonus}%): ${bonus_amount:,.2f}")
        if deduction > 0:
            print(f"Deductions ({deduction}%): -${deduction_amount:,.2f}")
        print(f"{'='*60}")
        print(f"Net Salary: ${total:,.2f}")
        print(f"{'='*60}\n")


# Create employee objects
print("EMPLOYEE SALARY CALCULATOR\n")

emp1 = Employee("E001", "John Doe", 200.00)
emp2 = Employee("E002", "Sarah Williams", 250.00)
emp3 = Employee("E003", "Mike Johnson", 180.00)

# Calculate salary for different working days
print("SALARY CALCULATIONS")
print("=" * 60)

emp1.display_salary_details(20)
emp2.display_salary_details(22)
emp3.display_salary_details(18)

# Salary for different working days
print("\nSALARY FOR DIFFERENT WORKING DAYS")
print("=" * 60)
print(f"\n{emp1.name} (Daily Rate: ${emp1.daily_rate}):")
for days in [15, 20, 22, 25]:
    salary = emp1.calculate_salary(days)
    print(f"  {days} days: ${salary:,.2f}")

# Salary with overtime
print("\n\nSALARY WITH OVERTIME")
print("=" * 60)
emp1.display_salary_breakdown(20, overtime_hours=10)
emp2.display_salary_breakdown(22, overtime_hours=5)

# Salary with deductions and bonus
print("\nSALARY WITH DEDUCTIONS AND BONUS")
print("=" * 60)
emp1.display_salary_breakdown(20, deduction=5, bonus=10)
emp3.display_salary_breakdown(18, overtime_hours=8, deduction=5, bonus=5)

# Complete breakdown
print("\nCOMPLETE SALARY SCENARIOS")
print("=" * 60)
emp2.display_salary_breakdown(22, overtime_hours=12, deduction=8, bonus=15)

# Salary comparison
print("\nSALARY COMPARISON TABLE")
print("=" * 60)
print(f"{'Employee':<20} {'Daily Rate':<15} {'20 Days':<15} {'22 Days':<15}")
print("-" * 65)
print(f"{emp1.name:<20} ${emp1.daily_rate:<14,.2f} ${emp1.calculate_salary(20):<14,.2f} ${emp1.calculate_salary(22):<14,.2f}")
print(f"{emp2.name:<20} ${emp2.daily_rate:<14,.2f} ${emp2.calculate_salary(20):<14,.2f} ${emp2.calculate_salary(22):<14,.2f}")
print(f"{emp3.name:<20} ${emp3.daily_rate:<14,.2f} ${emp3.calculate_salary(20):<14,.2f} ${emp3.calculate_salary(22):<14,.2f}")
