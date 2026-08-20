from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class Manager(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def display_details(self):
        return f"Manager: {self.name}, Salary: Rs. {self.calculate_salary()}"


class Developer(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def display_details(self):
        return f"Developer: {self.name}, Salary: Rs. {self.calculate_salary()}"


print(Manager("Anita", 80000).display_details())
print(Developer("Rahul", 60000).display_details())
