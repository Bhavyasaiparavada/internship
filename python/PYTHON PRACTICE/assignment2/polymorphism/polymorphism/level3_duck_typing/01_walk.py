class Duck:
    def walk(self):
        print("Duck walks")


class Dog:
    def walk(self):
        print("Dog walks")


def make_walk(obj):
    obj.walk()


make_walk(Duck())
make_walk(Dog())