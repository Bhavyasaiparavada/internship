def largest_three(first_number, second_number, third_number):
    largest = first_number
    if second_number > largest:
        largest = second_number
    if third_number > largest:
        largest = third_number
    return largest


print(largest_three(8, 12, 5))
