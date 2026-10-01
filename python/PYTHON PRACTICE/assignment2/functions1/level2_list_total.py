def list_total(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


print(list_total([2, 4, 6]))
