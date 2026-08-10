import json

file = open("student.json", "r")

data = json.load(file)

print(data)

file.close()