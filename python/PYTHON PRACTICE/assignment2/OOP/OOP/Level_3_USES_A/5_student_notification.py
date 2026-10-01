class NotificationService:
    def send(self, message):
        print("Notification:", message)


class Student:
    def __init__(self, name):
        self.name = name

    def notify(self, service):
        service.send("Hello, " + self.name)


Student("Asha").notify(NotificationService())
