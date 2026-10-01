from abc import ABC, abstractmethod


class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def course_type(self):
        pass


class OnlineCourse(Course):
    def course_type(self):
        return "Online"


class OfflineCourse(Course):
    def course_type(self):
        return "Offline"


for course in [OnlineCourse("Python", "8 weeks"), OfflineCourse("Databases", "10 weeks")]:
    print(course.course_type(), course.course_name, course.duration)