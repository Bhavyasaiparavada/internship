class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student = Student("Riya", 20, "Python Programming")
print("Student name:", student.name)
print("Age:", student.age)
print("Course:", student.course)
