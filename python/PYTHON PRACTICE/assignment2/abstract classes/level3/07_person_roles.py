from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def role(self):
        pass


class Student(Person):
    def role(self):
        return "Student"


class Teacher(Person):
    def role(self):
        return "Teacher"


class Doctor(Person):
    def role(self):
        return "Doctor"


for person in [Student("Liam", 18), Teacher("Emma", 35), Doctor("Omar", 40)]:
    print(person.name, person.age, person.role())