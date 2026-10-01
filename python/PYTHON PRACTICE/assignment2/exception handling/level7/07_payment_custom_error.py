class InvalidPaymentAmountError(Exception):
    pass


class Payment:
    def make_payment(self, amount):
        if amount <= 0:
            raise InvalidPaymentAmountError("Payment must be greater than zero.")
        return "Payment accepted."


try:
    payment = Payment()
    print(payment.make_payment(25))
except InvalidPaymentAmountError as error:
    print(error)