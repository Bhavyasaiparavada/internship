# Level 2: Lists with Loops

# 1. Print only the even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("1. Even numbers:")
for number in numbers:
    if number % 2 == 0:
        print(number)

# 2. Print only the odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("2. Odd numbers:")
for number in numbers:
    if number % 2 != 0:
        print(number)

# 3. Calculate the total without using sum()
numbers = [5, 10, 15, 20]
total = 0
for number in numbers:
    total = total + number
print("3. Total:", total)

# 4. Find the largest number without using max()
numbers = [12, 7, 25, 4, 18]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("4. Largest number:", largest)

# 5. Find the smallest number without using min()
numbers = [12, 7, 25, 4, 18]
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print("5. Smallest number:", smallest)

# 6. Calculate the average
numbers = [10, 20, 30, 40]
total = 0
for number in numbers:
    total = total + number
average = total / len(numbers)
print("6. Average:", average)

# 7. Count numbers greater than 50
numbers = [25, 60, 75, 40, 90, 50]
count = 0
for number in numbers:
    if number > 50:
        count = count + 1
print("7. Numbers greater than 50:", count)

# 8. Create separate lists for even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = []
odd_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print("8. Even numbers:", even_numbers)
print("   Odd numbers:", odd_numbers)

# 9. Make a list without duplicates, without using set()
numbers = [1, 2, 2, 3, 4, 3, 5, 1]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print("9. List without duplicates:", unique_numbers)

# 10. Create a list containing the squares
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number * number)
print("10. Squares:", squares)
