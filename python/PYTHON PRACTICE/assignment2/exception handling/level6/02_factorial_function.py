def factorial(number):
    if number < 0:
        raise ValueError("Number cannot be negative.")
    answer = 1
    for value in range(1, number + 1):
        answer *= value
    return answer


try:
    number = int(input("Enter a whole number: "))
    print("Factorial:", factorial(number))
except ValueError as error:
    print("Invalid input:", error)