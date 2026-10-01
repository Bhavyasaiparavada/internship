from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class UPIPayment(Payment):
    def pay(self):
        return "Processed UPI payment."


class CardPayment(Payment):
    def pay(self):
        return "Processed card payment."


for payment in [UPIPayment(), CardPayment()]:
    print(payment.pay())