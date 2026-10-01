def separate_even_odd(*numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers


print(separate_even_odd(1, 2, 3, 4, 5, 6))
