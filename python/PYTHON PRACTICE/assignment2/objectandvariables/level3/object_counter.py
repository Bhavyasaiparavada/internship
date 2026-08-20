# Question 6: Create a class variable that counts the total number of objects created for a class.

class Counter:
    total_objects = 0
    
    def __init__(self, name):
        self.name = name
        Counter.total_objects += 1
    
    def display_info(self):
        print(f"Object Name: {self.name}, Total Objects Created: {Counter.total_objects}")
    
    @classmethod
    def get_total_objects(cls):
        return cls.total_objects
    
    @classmethod
    def reset_counter(cls):
        cls.total_objects = 0
        print("Counter has been reset to 0")


# Create objects and count them
print("Creating objects...\n")

obj1 = Counter("Object 1")
obj1.display_info()

obj2 = Counter("Object 2")
obj2.display_info()

obj3 = Counter("Object 3")
obj3.display_info()

obj4 = Counter("Object 4")
obj4.display_info()

obj5 = Counter("Object 5")
obj5.display_info()

# Display total using class method
print(f"\nTotal objects created: {Counter.get_total_objects()}")

# Create more objects
print("\nCreating more objects...")
obj6 = Counter("Object 6")
obj7 = Counter("Object 7")

print(f"Total objects created: {Counter.get_total_objects()}")
