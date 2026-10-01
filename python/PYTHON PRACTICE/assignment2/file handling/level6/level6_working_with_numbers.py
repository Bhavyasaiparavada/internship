# Level 6: Working with Numbers

# 1. Create a file containing 20 numbers and calculate their total.
number_list = [12, -5, 0, 8, 12, 3, -2, 15, 7, 0, 20, 4, -5, 9, 1, 6, 11, 2, 14, 5]
with open("numbers.txt", "w") as file:
    for number in number_list:
        file.write(str(number) + "\n")

with open("numbers.txt", "r") as file:
    numbers = [int(line) for line in file]

print("1. Total:", sum(numbers))

# 2. Calculate the average.
print("2. Average:", sum(numbers) / len(numbers))

# 3. Find the largest number.
print("3. Largest number:", max(numbers))

# 4. Find the smallest number.
print("4. Smallest number:", min(numbers))

# 5. Put even and odd numbers into separate files.
with open("even_numbers.txt", "w") as even_file:
    with open("odd_numbers.txt", "w") as odd_file:
        for number in numbers:
            if number % 2 == 0:
                even_file.write(str(number) + "\n")
            else:
                odd_file.write(str(number) + "\n")

# 6. Create a file containing the squares.
with open("squares.txt", "w") as file:
    for number in numbers:
        file.write(str(number * number) + "\n")

# 7. Create a file containing the cubes.
with open("cubes.txt", "w") as file:
    for number in numbers:
        file.write(str(number * number * number) + "\n")

# 8. Count positive, negative, and zero values.
positive_count = sum(1 for number in numbers if number > 0)
negative_count = sum(1 for number in numbers if number < 0)
zero_count = sum(1 for number in numbers if number == 0)
print("8. Positive:", positive_count)
print("   Negative:", negative_count)
print("   Zero:", zero_count)

# 9. Find duplicate numbers.
duplicates = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)
print("9. Duplicate numbers:", duplicates)

# 10. Sort the numbers and write them to another file.
with open("sorted_numbers.txt", "w") as file:
    for number in sorted(numbers):
        file.write(str(number) + "\n")
