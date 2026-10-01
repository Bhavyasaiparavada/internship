def odd_numbers(numbers):
    odd_values = []
    for number in numbers:
        if number % 2 != 0:
            odd_values.append(number)
    return odd_values


print(odd_numbers([1, 2, 3, 4, 5, 6]))
