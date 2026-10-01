from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 50000

    def display_details(self):
        return "Manager: Alex"


class Developer(Employee):
    def calculate_salary(self):
        return 40000

    def display_details(self):
        return "Developer: Sam"


for employee in [Manager(), Developer()]:
    print(employee.display_details(), "Salary:", employee.calculate_salary())