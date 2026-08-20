from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def get_role(self):
        pass


class Manager(Employee):
    def get_role(self):
        return "Manager"


class Developer(Employee):
    def get_role(self):
        return "Developer"


class Tester(Employee):
    def get_role(self):
        return "Tester"


employees = [
    Manager("Anita", 80000),
    Developer("Rahul", 60000),
    Tester("Meera", 55000),
]
for employee in employees:
    print(employee.name, "is a", employee.get_role(), "earning Rs.", employee.salary)
