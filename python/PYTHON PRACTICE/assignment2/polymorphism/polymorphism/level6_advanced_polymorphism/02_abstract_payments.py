from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):
    def pay(self):
        print("Paid using UPI")


class Card(Payment):
    def pay(self):
        print("Paid using a card")


class NetBanking(Payment):
    def pay(self):
        print("Paid using net banking")


upi = UPI()
card = Card()
net_banking = NetBanking()
upi.pay()
card.pay()
net_banking.pay()