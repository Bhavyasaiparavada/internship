from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id)
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


class Developer(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def calculate_salary(self):
        return self.salary


employees = [
    Manager("Anita", "M101", 80000, 10000),
    Developer("Rahul", "D202", 60000),
]
for employee in employees:
    print(employee.name, employee.employee_id, "Salary: Rs.", employee.calculate_salary())
