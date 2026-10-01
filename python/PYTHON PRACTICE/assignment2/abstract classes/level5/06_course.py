from abc import ABC, abstractmethod


class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def start(self):
        pass

    def display_course_details(self):
        return self.course_name + " - " + self.duration


class OnlineCourse(Course):
    def start(self):
        return "Course started online."


course = OnlineCourse("Python", "8 weeks")
print(course.display_course_details())
print(course.start())