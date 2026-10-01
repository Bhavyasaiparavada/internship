from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        return "Email sent."


class SMSNotification(Notification):
    def send(self):
        return "SMS sent."


for notification in [EmailNotification(), SMSNotification()]:
    print(notification.send())