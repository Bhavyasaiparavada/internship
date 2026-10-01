from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id

    @abstractmethod
    def make_payment(self):
        pass


class CardPayment(Payment):
    def make_payment(self):
        return "Paid using card."


class UPIPayment(Payment):
    def make_payment(self):
        return "Paid using UPI."


for payment in [CardPayment(500, "T101"), UPIPayment(250, "T102")]:
    print(payment.transaction_id, payment.amount, payment.make_payment())