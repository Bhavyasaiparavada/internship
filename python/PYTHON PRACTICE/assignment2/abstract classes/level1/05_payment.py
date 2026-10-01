from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class UPIPayment(Payment):
    def pay(self):
        return "Payment made using UPI."


class CardPayment(Payment):
    def pay(self):
        return "Payment made using a card."


print(UPIPayment().pay())
print(CardPayment().pay())