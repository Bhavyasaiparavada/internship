class InvalidSalaryError(Exception):
    pass

try:
    salary = int(input("Enter Salary: "))

    if salary < 10000:
        raise InvalidSalaryError

    print("Valid Salary")

except InvalidSalaryError:
    print("Salary Must Be at Least ₹10,000")