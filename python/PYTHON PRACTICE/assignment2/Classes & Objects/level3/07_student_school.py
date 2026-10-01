class Student:
    school_name = "Green Valley School"

    def __init__(self, name):
        self.name = name


student = Student("Asha")
print(student.name, student.school_name)