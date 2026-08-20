from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        return f"Email sent: {message}"


class SMSNotification(Notification):
    def send(self, message):
        return f"SMS sent: {message}"


print(EmailNotification().send("Welcome!"))
print(SMSNotification().send("Your code is 1234."))
