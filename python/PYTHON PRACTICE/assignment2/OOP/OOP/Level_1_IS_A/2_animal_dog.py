class Animal:
    def eat(self):
        print("The animal is eating")


class Dog(Animal):
    def bark(self):
        print("Woof!")


dog = Dog()
dog.eat()
dog.bark()
