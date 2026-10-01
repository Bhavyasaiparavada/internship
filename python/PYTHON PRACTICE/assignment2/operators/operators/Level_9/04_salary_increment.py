# 4. Write a program to calculate an employee's salary after applying a percentage increment.
salary = float(input("Enter salary: "))
increment = 10
new_salary = salary + (salary * increment / 100)
print("New salary =", new_salary)
