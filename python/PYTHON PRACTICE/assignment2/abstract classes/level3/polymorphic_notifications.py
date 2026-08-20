from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class Email(Notification):
    def send(self, message):
        return f"Email notification sent: {message}"


class SMS(Notification):
    def send(self, message):
        return f"SMS notification sent: {message}"


class WhatsApp(Notification):
    def send(self, message):
        return f"WhatsApp notification sent: {message}"


notifications = [Email(), SMS(), WhatsApp()]
for notification in notifications:
    print(notification.send("Your order has been shipped."))
