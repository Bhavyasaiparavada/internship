class EmailService:
    def send(self, address, message):
        print("Email to", address + ":", message)


class Order:
    def __init__(self, number, email):
        self.number = number
        self.email = email

    def send_confirmation(self, service):
        service.send(self.email, "Order " + str(self.number) + " confirmed")


Order(101, "asha@example.com").send_confirmation(EmailService())
