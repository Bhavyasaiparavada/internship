from abc import ABC, abstractmethod


class Course(ABC):
    @abstractmethod
    def start_course(self):
        pass

    @abstractmethod
    def get_duration(self):
        pass


class OnlineCourse(Course):
    def start_course(self):
        return "Online course starts through a virtual classroom."

    def get_duration(self):
        return "Duration: 8 weeks"


class OfflineCourse(Course):
    def start_course(self):
        return "Offline course starts at the training center."

    def get_duration(self):
        return "Duration: 12 weeks"


for course in (OnlineCourse(), OfflineCourse()):
    print(course.start_course())
    print(course.get_duration())
