from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Dog says woof."


class Cat(Animal):
    def sound(self):
        return "Cat says meow."


print(Dog().sound())
print(Cat().sound())