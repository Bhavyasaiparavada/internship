class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


people = [
    Person("Arjun Nair", 28, "Bengaluru"),
    Person("Kavya Singh", 25, "Pune"),
]

for person in people:
    print("Name:", person.name)
    print("Age:", person.age)
    print("City:", person.city)
    print()
