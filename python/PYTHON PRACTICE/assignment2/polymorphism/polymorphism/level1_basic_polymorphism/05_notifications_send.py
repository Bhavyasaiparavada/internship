class EmailNotification:
    def send(self):
        print("Sending an email notification")


class SMSNotification:
    def send(self):
        print("Sending an SMS notification")


email = EmailNotification()
sms = SMSNotification()
email.send()
sms.send()