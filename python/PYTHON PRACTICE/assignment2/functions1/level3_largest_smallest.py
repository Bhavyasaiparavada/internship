def largest_and_smallest(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]
    smallest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    return largest, smallest


print(largest_and_smallest([4, 8, 2, 6]))
