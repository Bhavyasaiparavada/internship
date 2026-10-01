class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Woof!")


class Cat(Animal):
    def sound(self):
        print("Meow!")


Dog().sound()
Cat().sound()
