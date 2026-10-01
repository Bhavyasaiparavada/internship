class DebitCard:
    def pay(self):
        print("Paid using a debit card")


class CreditCard:
    def pay(self):
        print("Paid using a credit card")


def pay_by_card(card):
    card.pay()


pay_by_card(DebitCard())
pay_by_card(CreditCard())