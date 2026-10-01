class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(self.name, "is", self.age, "years old")


class Student(Person):
    def learn(self):
        print(self.name, "is learning")


class Teacher(Person):
    def teach(self):
        print(self.name, "is teaching")


Student("Asha", 18).learn()
Teacher("Mr. Lee", 35).teach()
