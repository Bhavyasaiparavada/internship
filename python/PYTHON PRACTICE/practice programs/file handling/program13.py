file = open("students.txt", "w")

name = input("Enter Name: ")
course = input("Enter Course: ")
city = input("Enter City: ")

file.write("Name: " + name + "\n")
file.write("Course: " + course + "\n")
file.write("City: " + city + "\n")

file.close()

print("Student Registered Successfully")