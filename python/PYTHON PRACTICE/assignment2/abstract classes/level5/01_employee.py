from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    def display_company(self):
        return "Company: ABC Technologies"


class Developer(Employee):
    def calculate_salary(self):
        return 40000


developer = Developer()
print(developer.display_company())
print("Salary:", developer.calculate_salary())