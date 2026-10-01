# Level 3: Lists and Tuples

# 1. Display students who scored above 75
students = [("Asha", 82), ("Ben", 68), ("Chloe", 91), ("David", 75), ("Eva", 79)]
print("1. Students who scored above 75:")
for student in students:
    if student[1] > 75:
        print(student[0], student[1])

# 2. Calculate the total value of each product
products = [("Pen", 2, 10), ("Notebook", 5, 4), ("Bag", 25, 2)]
print("2. Product values:")
for product in products:
    name = product[0]
    price = product[1]
    quantity = product[2]
    total_value = price * quantity
    print(name, "total value:", total_value)

# 3. Find the employee with the highest salary
employees = [("Asha", "Developer", 60000), ("Ben", "Designer", 52000), ("Chloe", "Manager", 75000)]
highest_paid = employees[0]
for employee in employees:
    if employee[2] > highest_paid[2]:
        highest_paid = employee
print("3. Highest-paid employee:", highest_paid[0], highest_paid[2])

# 4. Calculate each student's total and average marks
students = [["Asha", 80, 75, 90], ["Ben", 65, 70, 72], ["Chloe", 92, 88, 95]]
print("4. Student totals and averages:")
for student in students:
    total = student[1] + student[2] + student[3]
    average = total / 3
    print(student[0], "total:", total, "average:", average)

# 5. Access and modify values inside lists stored in a tuple
class_data = (["Asha", "Ben"], [80, 90])
print("5. First student:", class_data[0][0])
class_data[0][1] = "Brian"
class_data[1][0] = 85
print("   Updated tuple:", class_data)

# 6. Convert a list into a tuple
numbers = [1, 2, 3, 4, 5]
numbers_tuple = tuple(numbers)
print("6. Tuple:", numbers_tuple)

# 7. Convert a tuple into a list and add three numbers
numbers = (1, 2, 3)
numbers_list = list(numbers)
numbers_list.append(4)
numbers_list.append(5)
numbers_list.append(6)
print("7. Updated list:", numbers_list)

# 8. Combine two lists
first_list = [1, 2, 3]
second_list = [4, 5, 6]
combined_list = first_list + second_list
print("8. Combined list:", combined_list)

# 9. Combine two tuples
first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
combined_tuple = first_tuple + second_tuple
print("9. Combined tuple:", combined_tuple)

# 10. Search for a student by name
students = [("Asha", 82), ("Ben", 68), ("Chloe", 91)]
search_name = "Ben"
found = False
for student in students:
    if student[0] == search_name:
        print("10. Student found:", student[0], "marks:", student[1])
        found = True
if not found:
    print("10. Student not found:", search_name)
