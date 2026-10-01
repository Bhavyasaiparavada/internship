def smallest_three(first_number, second_number, third_number):
    smallest = first_number
    if second_number < smallest:
        smallest = second_number
    if third_number < smallest:
        smallest = third_number
    return smallest


print(smallest_three(8, 12, 5))
