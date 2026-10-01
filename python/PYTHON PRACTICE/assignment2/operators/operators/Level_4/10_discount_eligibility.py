# 10. Check whether a user is eligible for a discount based on age or membership status.
age = int(input("Enter age: "))
member = input("Member? (yes/no): ")
print(age >= 60 or member.lower() == 'yes')
