class Employee:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self, working_days):
        daily_salary = self.monthly_salary / 30
        return daily_salary * working_days


employee = Employee(30000)
print("Salary:", employee.calculate_salary(22))