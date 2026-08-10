import csv

file = open("students.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow(["Name", "Course", "City"])
writer.writerow(["Bhavya", "Python", "Visakhapatnam"])

file.close()