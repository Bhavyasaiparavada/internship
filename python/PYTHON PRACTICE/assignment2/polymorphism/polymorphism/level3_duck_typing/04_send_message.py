class EmailService:
    def send(self):
        print("Email sent")


class SMSService:
    def send(self):
        print("SMS sent")


def send_message(service):
    service.send()


send_message(EmailService())
send_message(SMSService())