class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


students = [
    Student("Ananya", 20, "Python Programming"),
    Student("Rohan", 21, "Data Science"),
    Student("Meera", 19, "Web Development"),
]

for student in students:
    print("Name:", student.name)
    print("Age:", student.age)
    print("Course:", student.course)
    print()
