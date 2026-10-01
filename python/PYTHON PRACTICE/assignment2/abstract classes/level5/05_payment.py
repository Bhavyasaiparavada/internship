from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

    def display_amount(self):
        return "Amount: " + str(self.amount)


class CardPayment(Payment):
    def pay(self):
        return "Payment completed by card."


payment = CardPayment(750)
print(payment.display_amount())
print(payment.pay())