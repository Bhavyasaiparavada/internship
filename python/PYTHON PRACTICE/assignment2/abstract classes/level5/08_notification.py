from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self):
        pass

    def display_message(self):
        return "Message: " + self.message


class EmailNotification(Notification):
    def send(self):
        return "Email sent."


notification = EmailNotification("Your order is ready.")
print(notification.display_message())
print(notification.send())