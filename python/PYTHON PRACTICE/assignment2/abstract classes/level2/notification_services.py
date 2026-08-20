from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def schedule(self, message, time):
        pass


class Email(Notification):
    def send(self, message):
        return f"Email sent: {message}"

    def schedule(self, message, time):
        return f"Email scheduled for {time}: {message}"


class SMS(Notification):
    def send(self, message):
        return f"SMS sent: {message}"

    def schedule(self, message, time):
        return f"SMS scheduled for {time}: {message}"


class WhatsApp(Notification):
    def send(self, message):
        return f"WhatsApp message sent: {message}"

    def schedule(self, message, time):
        return f"WhatsApp message scheduled for {time}: {message}"


for notification in (Email(), SMS(), WhatsApp()):
    print(notification.send("Meeting at 10 AM"))
    print(notification.schedule("Meeting at 10 AM", "tomorrow"))
