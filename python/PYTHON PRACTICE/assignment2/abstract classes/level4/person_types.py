from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def introduce(self):
        pass


class Student(Person):
    def introduce(self):
        return f"{self.name} is a {self.age}-year-old student."


class Teacher(Person):
    def introduce(self):
        return f"{self.name} is a {self.age}-year-old teacher."


class Doctor(Person):
    def introduce(self):
        return f"{self.name} is a {self.age}-year-old doctor."


people = [Student("Riya", 20), Teacher("Vikram", 35), Doctor("Neha", 42)]
for person in people:
    print(person.introduce())
