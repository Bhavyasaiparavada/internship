class Animal:
    pass


class Dog(Animal):
    pass


print("IS-A: Dog is an Animal")
print(isinstance(Dog(), Animal))
