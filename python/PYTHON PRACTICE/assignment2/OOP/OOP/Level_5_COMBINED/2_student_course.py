class Person:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, title):
        self.title = title


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course


student = Student("Asha", Course("Python"))
print(student.name, "studies", student.course.title)
