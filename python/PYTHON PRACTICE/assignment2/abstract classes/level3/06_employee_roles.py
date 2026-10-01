from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def job_title(self):
        pass


class Manager(Employee):
    def job_title(self):
        return "Manager"


class Developer(Employee):
    def job_title(self):
        return "Developer"


class Tester(Employee):
    def job_title(self):
        return "Tester"


for employee in [Manager("Mia", 50000), Developer("Noah", 40000), Tester("Ava", 35000)]:
    print(employee.name, employee.job_title(), employee.salary)