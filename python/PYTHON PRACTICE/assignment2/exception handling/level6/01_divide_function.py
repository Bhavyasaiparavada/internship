def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None


print(divide(10, 2))
print(divide(10, 0))