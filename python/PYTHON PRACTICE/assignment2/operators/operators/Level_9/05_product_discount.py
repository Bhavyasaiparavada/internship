# 5. Write a program to calculate a product's price after applying a discount.
price = float(input("Enter price: "))
discount = 15
final_price = price - (price * discount / 100)
print("Final price =", final_price)
