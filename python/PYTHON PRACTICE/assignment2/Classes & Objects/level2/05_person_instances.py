class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


people = [Person("Asha", 25, "Chennai"), Person("Ravi", 30, "Delhi")]
for person in people:
    print(person.name, person.age, person.city)