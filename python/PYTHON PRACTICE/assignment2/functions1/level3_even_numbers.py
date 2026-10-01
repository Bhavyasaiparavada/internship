def even_numbers(numbers):
    even_values = []
    for number in numbers:
        if number % 2 == 0:
            even_values.append(number)
    return even_values


print(even_numbers([1, 2, 3, 4, 5, 6]))
