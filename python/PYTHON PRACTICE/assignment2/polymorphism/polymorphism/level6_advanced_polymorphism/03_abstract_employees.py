from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 40000


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 20000


full_time_employee = FullTimeEmployee()
part_time_employee = PartTimeEmployee()
print("Full-time salary:", full_time_employee.calculate_salary())
print("Part-time salary:", part_time_employee.calculate_salary())