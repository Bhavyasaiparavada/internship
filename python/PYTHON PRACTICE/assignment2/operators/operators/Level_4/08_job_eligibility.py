# 8. Check whether a person is eligible for a job based on age and qualification.
age = int(input("Enter age: "))
qualification = input("Has degree? (yes/no): ")
print(age >= 21 and qualification.lower() == 'yes')
