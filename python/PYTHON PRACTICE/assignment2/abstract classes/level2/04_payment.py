from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass


class UPI(Payment):
    def pay(self):
        return "Paid using UPI."

    def refund(self):
        return "UPI payment refunded."


class CreditCard(Payment):
    def pay(self):
        return "Paid using credit card."

    def refund(self):
        return "Credit card payment refunded."


class NetBanking(Payment):
    def pay(self):
        return "Paid using net banking."

    def refund(self):
        return "Net banking payment refunded."


for payment in [UPI(), CreditCard(), NetBanking()]:
    print(payment.pay(), payment.refund())