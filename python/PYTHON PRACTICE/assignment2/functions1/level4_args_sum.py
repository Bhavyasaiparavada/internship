def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


print(add_numbers(2, 4, 6))
