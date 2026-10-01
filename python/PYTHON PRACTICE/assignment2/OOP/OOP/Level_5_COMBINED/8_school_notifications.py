class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name):
        self.name = name


class NotificationService:
    def send(self, student):
        print("Notification sent to", student)


class School:
    def __init__(self):
        self.teachers = [Teacher("Ms. Lee")]
        self.students = [Student("Asha")]

    def notify_students(self, service):
        for student in self.students:
            service.send(student.name)


school = School()
print("Teacher:", school.teachers[0].name)
school.notify_students(NotificationService())
