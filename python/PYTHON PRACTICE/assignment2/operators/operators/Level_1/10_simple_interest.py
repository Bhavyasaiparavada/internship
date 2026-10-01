# 10. Write a program to calculate simple interest using arithmetic operators.
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)
