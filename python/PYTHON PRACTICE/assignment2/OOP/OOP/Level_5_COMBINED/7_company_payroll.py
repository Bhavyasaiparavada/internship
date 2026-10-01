class Employee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, name):
        self.name = name


class PayrollService:
    def pay(self, employee):
        print("Paid", employee.name)


class Company:
    def __init__(self):
        self.departments = [Department("IT")]
        self.employees = [Employee("Ravi")]

    def pay_employees(self, service):
        for employee in self.employees:
            service.pay(employee)


company = Company()
print("Department:", company.departments[0].name)
company.pay_employees(PayrollService())
