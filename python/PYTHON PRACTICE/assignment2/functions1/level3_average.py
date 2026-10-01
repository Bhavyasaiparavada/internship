def average(numbers):
    if len(numbers) == 0:
        return None

    total = 0
    for number in numbers:
        total = total + number
    return total / len(numbers)


print(average([4, 6, 8]))
