class Student:
    college_name = "Central College"

    def __init__(self, name):
        self.name = name


students = [Student("Asha"), Student("Ravi"), Student("Mina")]
for student in students:
    print(student.name, student.college_name)