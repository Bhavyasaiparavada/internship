def factorial(number):
    if number < 0:
        return None

    result = 1
    for value in range(1, number + 1):
        result = result * value
    return result


print(factorial(5))
