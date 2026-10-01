from abc import ABC, abstractmethod


class Tax(ABC):
    @abstractmethod
    def calculate_tax(self, amount):
        pass


class IncomeTax(Tax):
    def calculate_tax(self, amount):
        return amount * 0.10


class SalesTax(Tax):
    def calculate_tax(self, amount):
        return amount * 0.05


income_tax = IncomeTax()
sales_tax = SalesTax()
print("Income tax:", income_tax.calculate_tax(1000))
print("Sales tax:", sales_tax.calculate_tax(1000))