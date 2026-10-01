def second_largest(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    if len(unique_numbers) < 2:
        return None

    largest = unique_numbers[0]
    second = None
    for number in unique_numbers[1:]:
        if number > largest:
            second = largest
            largest = number
        elif second is None or number > second:
            second = number
    return second


print(second_largest([4, 8, 2, 8, 6]))
