from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 40000


employee = FullTimeEmployee("Riya", 101)
print(employee.name, employee.employee_id, employee.calculate_salary())