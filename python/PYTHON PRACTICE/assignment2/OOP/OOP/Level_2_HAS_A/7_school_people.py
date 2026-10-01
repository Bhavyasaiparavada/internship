class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self):
        self.teacher = Teacher("Ms. Lee")
        self.students = [Student("Asha"), Student("Ravi")]


school = School()
print("Teacher:", school.teacher.name)
print("Students:", ", ".join(student.name for student in school.students))
