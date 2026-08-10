file = open("attendance.txt", "a")

name = input("Enter Student Name: ")
status = input("Enter Attendance (Present/Absent): ")

file.write(name + " - " + status + "\n")

file.close()

print("Attendance Recorded")