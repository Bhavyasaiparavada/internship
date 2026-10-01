class Notification:
    def send(self):
        print("Sending a notification")


class Email(Notification):
    def send(self):
        print("Sending an email")


class SMS(Notification):
    def send(self):
        print("Sending an SMS")


class WhatsApp(Notification):
    def send(self):
        print("Sending a WhatsApp message")


email = Email()
sms = SMS()
whatsapp = WhatsApp()
email.send()
sms.send()
whatsapp.send()