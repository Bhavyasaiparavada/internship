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
        return "Online course started."

    def get_duration(self):
        return "8 weeks"


class OfflineCourse(Course):
    def start_course(self):
        return "Offline course started."

    def get_duration(self):
        return "12 weeks"


for course in [OnlineCourse(), OfflineCourse()]:
    print(course.start_course(), "Duration:", course.get_duration())