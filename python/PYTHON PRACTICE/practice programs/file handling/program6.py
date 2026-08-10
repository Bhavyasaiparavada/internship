file = open("student.txt", "r")

data = file.read()

words = len(data.split())
characters = len(data)

print("Words:", words)
print("Characters:", characters)

file.close()