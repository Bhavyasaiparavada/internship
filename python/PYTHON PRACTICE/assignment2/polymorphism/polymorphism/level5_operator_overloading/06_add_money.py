class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)


money1 = Money(100)
money2 = Money(50)
total = money1 + money2
print("Total money:", total.amount)