# Level 1: Lists

# 1. Print all five fruits
fruits = ["apple", "banana", "mango", "orange", "grapes"]
print("1. Fruits:", fruits)

# 2. Print the first and last numbers
numbers = [10, 20, 30, 40, 50]
print("2. First number:", numbers[0])
print("   Last number:", numbers[-1])

# 3. Print the first five numbers using slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("3. First five numbers:", numbers[:5])

# 4. Print the last five numbers using slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("4. Last five numbers:", numbers[-5:])

# 5. Find the number of students
students = ["Asha", "Ben", "Chloe", "David"]
print("5. Number of students:", len(students))

# 6. Add a number using append()
numbers = [2, 4, 6]
numbers.append(8)
print("6. After append:", numbers)

# 7. Insert a name at the second position
names = ["Asha", "Ben", "Chloe"]
names.insert(1, "Daniel")
print("7. After insert:", names)

# 8. Remove a specific number using remove()
numbers = [10, 20, 30, 40]
numbers.remove(30)
print("8. After remove:", numbers)

# 9. Remove the last number using pop()
numbers = [10, 20, 30, 40]
numbers.pop()
print("9. After pop:", numbers)

# 10. Sort numbers in ascending order
numbers = [5, 2, 8, 1, 3]
numbers.sort()
print("10. Ascending order:", numbers)

# 11. Sort numbers in descending order
numbers = [5, 2, 8, 1, 3]
numbers.sort(reverse=True)
print("11. Descending order:", numbers)

# 12. Reverse the list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print("12. Reversed list:", numbers)

# 13. Check whether a student exists
students = ["Asha", "Ben", "Chloe"]
print("13. Is Ben in the list?", "Ben" in students)

# 14. Count how many times a value appears
numbers = [2, 4, 2, 6, 2, 8]
print("14. Number of times 2 appears:", numbers.count(2))

# 15. Find the index of a number
numbers = [10, 20, 30, 40]
print("15. Index of 30:", numbers.index(30))
