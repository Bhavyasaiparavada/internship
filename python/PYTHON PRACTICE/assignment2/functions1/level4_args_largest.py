def largest_number(*numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


print(largest_number(4, 9, 2, 7))
