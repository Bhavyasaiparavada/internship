from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, monthly_salary, bonus):
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.monthly_salary + self.bonus


class Developer(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


employees = [Manager(80000, 10000), Developer(60000)]
for employee in employees:
    print("Salary: Rs.", employee.calculate_salary())
