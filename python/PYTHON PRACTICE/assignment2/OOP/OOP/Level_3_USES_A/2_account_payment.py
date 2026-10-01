class PaymentService:
    def pay(self, amount):
        print("Paid $", amount)


class BankAccount:
    def make_payment(self, service, amount):
        service.pay(amount)


BankAccount().make_payment(PaymentService(), 50)
