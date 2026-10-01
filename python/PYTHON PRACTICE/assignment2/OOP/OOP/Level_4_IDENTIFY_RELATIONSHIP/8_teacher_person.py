class Person:
    pass


class Teacher(Person):
    pass


print("IS-A: Teacher is a Person")
print(isinstance(Teacher(), Person))
