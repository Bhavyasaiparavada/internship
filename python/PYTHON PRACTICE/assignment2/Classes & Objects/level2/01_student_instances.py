class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


students = [Student("Asha", 18, "Science"), Student("Ravi", 19, "Arts"), Student("Mina", 18, "Commerce")]
for student in students:
    print(student.name, student.age, student.course)