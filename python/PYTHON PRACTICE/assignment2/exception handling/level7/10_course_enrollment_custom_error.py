class InvalidEnrollmentError(Exception):
    pass


class Course:
    def __init__(self, name, available_seats):
        self.name = name
        self.available_seats = available_seats

    def enroll(self, student_name):
        if not student_name.strip():
            raise InvalidEnrollmentError("Student name cannot be empty.")
        if self.available_seats <= 0:
            raise InvalidEnrollmentError("There are no seats available.")
        self.available_seats -= 1
        return student_name + " enrolled in " + self.name


course = Course("Python", 2)
try:
    print(course.enroll("Leah"))
except InvalidEnrollmentError as error:
    print(error)