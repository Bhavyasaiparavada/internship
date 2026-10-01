class Student:
    def __init__(self, name):
        self.name = name


class College:
    def __init__(self):
        self.students = [Student("Asha"), Student("Ravi")]


college = College()
for student in college.students:
    print(student.name)
