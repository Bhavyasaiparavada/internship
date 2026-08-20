# Question 1: Create a Student class with a class variable college_name
# Create three student objects and display the college name.

class Student:
    college_name = "XYZ University"
    
    def __init__(self, name):
        self.name = name
    
    def display_college_name(self):
        print(f"Student: {self.name}, College: {Student.college_name}")


# Create three student objects
student1 = Student("Alice")
student2 = Student("Bob")
student3 = Student("Charlie")

# Display college name using different objects
student1.display_college_name()
student2.display_college_name()
student3.display_college_name()

# Display directly using class variable
print(f"\nDirect access - College Name: {Student.college_name}")
