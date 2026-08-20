from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class UPI(Payment):
    def process_payment(self, amount):
        return f"Processed Rs. {amount} through UPI."


class CreditCard(Payment):
    def process_payment(self, amount):
        return f"Processed Rs. {amount} through credit card."


class NetBanking(Payment):
    def process_payment(self, amount):
        return f"Processed Rs. {amount} through net banking."


payment_methods = [UPI(), CreditCard(), NetBanking()]
for payment in payment_methods:
    print(payment.process_payment(1500))
