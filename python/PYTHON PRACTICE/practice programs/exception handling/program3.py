employee = {
    "id": 101,
    "name": "Ravi",
    "salary": 30000
}

try:
    key = input("Enter Key: ")
    print(employee[key])

except KeyError:
    print("Key Not Found")