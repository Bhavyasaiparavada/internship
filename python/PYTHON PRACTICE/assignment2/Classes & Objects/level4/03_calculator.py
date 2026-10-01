class Calculator:
    def add(self, first, second):
        return first + second

    def subtract(self, first, second):
        return first - second

    def multiply(self, first, second):
        return first * second

    def divide(self, first, second):
        return first / second


calculator = Calculator()
print(calculator.add(8, 4))
print(calculator.subtract(8, 4))
print(calculator.multiply(8, 4))
print(calculator.divide(8, 4))