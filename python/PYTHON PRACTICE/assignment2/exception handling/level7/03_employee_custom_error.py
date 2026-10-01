class InvalidSalaryError(Exception):
    pass


class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError("Salary cannot be negative.")
        self.name = name
        self.salary = salary


try:
    employee = Employee("Arun", 30000)
    print(employee.name, "salary:", employee.salary)
except InvalidSalaryError as error:
    print(error)