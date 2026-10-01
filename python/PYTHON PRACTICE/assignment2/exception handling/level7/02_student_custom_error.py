class InvalidMarksError(Exception):
    pass


class Student:
    def __init__(self, name, marks):
        if marks < 0 or marks > 100:
            raise InvalidMarksError("Marks must be between 0 and 100.")
        self.name = name
        self.marks = marks


try:
    student = Student("Mina", 85)
    print(student.name, "has marks", student.marks)
except InvalidMarksError as error:
    print(error)