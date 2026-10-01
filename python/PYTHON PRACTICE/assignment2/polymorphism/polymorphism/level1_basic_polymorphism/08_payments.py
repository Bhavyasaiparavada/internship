class UPIPayment:
    def pay(self):
        print("Paid using UPI")


class CardPayment:
    def pay(self):
        print("Paid using a card")


class CashPayment:
    def pay(self):
        print("Paid using cash")


upi = UPIPayment()
card = CardPayment()
cash = CashPayment()
upi.pay()
card.pay()
cash.pay()