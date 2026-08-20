from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid Rs. {amount} using UPI."


class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid Rs. {amount} using card."


print(UPIPayment().pay(500))
print(CardPayment().pay(750))
