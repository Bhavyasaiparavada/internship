file = open("student.txt", "r")

count = 0

for line in file:
    count += 1

print("Number of Lines:", count)

file.close()