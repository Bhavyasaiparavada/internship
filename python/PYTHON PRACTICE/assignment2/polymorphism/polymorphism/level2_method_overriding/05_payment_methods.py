class Payment:
    def pay(self):
        print("Making a payment")


class UPI(Payment):
    def pay(self):
        print("Paid using UPI")


class CreditCard(Payment):
    def pay(self):
        print("Paid using a credit card")


class NetBanking(Payment):
    def pay(self):
        print("Paid using net banking")


upi = UPI()
credit_card = CreditCard()
net_banking = NetBanking()
upi.pay()
credit_card.pay()
net_banking.pay()