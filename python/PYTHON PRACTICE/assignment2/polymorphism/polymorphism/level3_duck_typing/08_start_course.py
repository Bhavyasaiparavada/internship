class OnlineCourse:
    def start(self):
        print("Online course started")


class OfflineCourse:
    def start(self):
        print("Classroom course started")


def start_course(course):
    course.start()


start_course(OnlineCourse())
start_course(OfflineCourse())