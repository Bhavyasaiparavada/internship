class EmailNotification:
    def send(self):
        print("Email sent")


class SMSNotification:
    def send(self):
        print("SMS sent")


def send_notification(notification):
    notification.send()


send_notification(EmailNotification())
send_notification(SMSNotification())