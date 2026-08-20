from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id

    @abstractmethod
    def process_payment(self):
        pass


class UPI(Payment):
    def process_payment(self):
        return f"UPI payment of Rs. {self.amount} processed."


class CreditCard(Payment):
    def process_payment(self):
        return f"Credit card payment of Rs. {self.amount} processed."


class NetBanking(Payment):
    def process_payment(self):
        return f"Net banking payment of Rs. {self.amount} processed."


payments = [
    UPI(500, "UPI001"),
    CreditCard(1200, "CARD002"),
    NetBanking(2500, "NET003"),
]
for payment in payments:
    print(payment.transaction_id, payment.process_payment())
