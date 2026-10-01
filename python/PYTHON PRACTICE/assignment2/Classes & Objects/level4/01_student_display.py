class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(self.name, self.age, self.course)


student = Student("Asha", 18, "Science")
student.display()