def average_numbers(*numbers):
    if len(numbers) == 0:
        return None

    total = 0
    for number in numbers:
        total = total + number
    return total / len(numbers)


print(average_numbers(4, 6, 8))
