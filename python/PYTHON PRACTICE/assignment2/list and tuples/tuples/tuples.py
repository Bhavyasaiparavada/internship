# Tuples

# 1. Print all five colors
colors = ("red", "blue", "green", "yellow", "purple")
print("1. Colors:", colors)

# 2. Print the first and last elements
animals = ("cat", "dog", "rabbit", "horse")
print("2. First element:", animals[0])
print("   Last element:", animals[-1])

# 3. Print tuple elements using slicing
numbers = (1, 2, 3, 4, 5, 6)
print("3. Tuple slice:", numbers[1:4])

# 4. Find the length of a tuple
numbers = (10, 20, 30, 40, 50)
print("4. Tuple length:", len(numbers))

# 5. Count a value using count()
numbers = (1, 2, 3, 2, 4, 2, 5)
print("5. Number of times 2 appears:", numbers.count(2))

# 6. Find an element's index using index()
colors = ("red", "blue", "green", "yellow")
print("6. Index of green:", colors.index("green"))

# 7. Find the largest and smallest values
numbers = (14, 3, 27, 8, 19)
print("7. Largest value:", max(numbers))
print("   Smallest value:", min(numbers))

# 8. Access each student information element
student = ("Maya", 18, "Science", 92)
print("8. Name:", student[0])
print("   Age:", student[1])
print("   Course:", student[2])
print("   Marks:", student[3])

# 9. Unpack student information into separate variables
student = ("Maya", 18, "Science", 92)
name, age, course, marks = student
print("9. Name:", name)
print("   Age:", age)
print("   Course:", course)
print("   Marks:", marks)

# 10. Swap two values using tuple unpacking
first = 10
second = 20
first, second = second, first
print("10. After swapping:", first, second)
