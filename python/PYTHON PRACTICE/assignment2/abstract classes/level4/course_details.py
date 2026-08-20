from abc import ABC, abstractmethod


class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def start_course(self):
        pass


class OnlineCourse(Course):
    def start_course(self):
        return f"{self.course_name} starts online and lasts {self.duration}."


class OfflineCourse(Course):
    def start_course(self):
        return f"{self.course_name} starts at the training center and lasts {self.duration}."


courses = [
    OnlineCourse("Python Programming", "8 weeks"),
    OfflineCourse("Data Science", "12 weeks"),
]
for course in courses:
    print(course.start_course())
