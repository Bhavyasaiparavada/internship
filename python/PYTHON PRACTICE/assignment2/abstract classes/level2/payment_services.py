from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        return f"Paid Rs. {amount} using UPI."

    def refund(self, amount):
        return f"Refunded Rs. {amount} through UPI."


class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid Rs. {amount} using credit card."

    def refund(self, amount):
        return f"Refunded Rs. {amount} to credit card."


class NetBanking(Payment):
    def pay(self, amount):
        return f"Paid Rs. {amount} using net banking."

    def refund(self, amount):
        return f"Refunded Rs. {amount} through net banking."


for payment in (UPI(), CreditCard(), NetBanking()):
    print(payment.pay(1000))
    print(payment.refund(1000))
