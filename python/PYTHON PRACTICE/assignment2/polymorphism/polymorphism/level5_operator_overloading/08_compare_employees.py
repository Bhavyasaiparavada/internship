class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


employee1 = Employee("Asha", 40000)
employee2 = Employee("Ravi", 35000)
print(employee1 > employee2)