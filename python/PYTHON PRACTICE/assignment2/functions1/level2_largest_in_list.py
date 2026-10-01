def largest_in_list(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


print(largest_in_list([3, 9, 4, 7]))
