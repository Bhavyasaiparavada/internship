class Dog:
    def sound(self):
        print("Woof")


class Cat:
    def sound(self):
        print("Meow")


class Cow:
    def sound(self):
        print("Moo")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()
cow = Cow()
make_sound(dog)
make_sound(cat)
make_sound(cow)