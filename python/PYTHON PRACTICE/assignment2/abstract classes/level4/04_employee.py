from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 50000


class Developer(Employee):
    def calculate_salary(self):
        return 40000


for employee in [Manager(), Developer()]:
    print("Salary:", employee.calculate_salary())