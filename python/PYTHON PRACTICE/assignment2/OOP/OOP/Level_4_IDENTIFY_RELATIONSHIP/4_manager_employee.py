class Employee:
    pass


class Manager(Employee):
    pass


print("IS-A: Manager is an Employee")
print(isinstance(Manager(), Employee))
