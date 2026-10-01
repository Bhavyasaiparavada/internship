class InvalidSalaryError(Exception):
    pass


try:
    salary = float(input("Enter salary: "))
    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative.")
    print("Salary accepted:", salary)
except ValueError:
    print("Enter salary as a number.")
except InvalidSalaryError as error:
    print(error)