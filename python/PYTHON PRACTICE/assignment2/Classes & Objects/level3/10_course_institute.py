class Course:
    institute_name = "Learning Center"

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration


course = Course("Python", "8 weeks")
print(course.institute_name, course.course_name, course.duration)