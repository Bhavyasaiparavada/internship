def total_price(price, tax_percent=5):
    tax = price * tax_percent / 100
    return price + tax


print(total_price(100))
