from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def schedule(self):
        pass


class Email(Notification):
    def send(self):
        return "Email sent."

    def schedule(self):
        return "Email scheduled."


class SMS(Notification):
    def send(self):
        return "SMS sent."

    def schedule(self):
        return "SMS scheduled."


class WhatsApp(Notification):
    def send(self):
        return "WhatsApp message sent."

    def schedule(self):
        return "WhatsApp message scheduled."


for notification in [Email(), SMS(), WhatsApp()]:
    print(notification.send(), notification.schedule())