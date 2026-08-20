# Question 1: Create a Student class with a method display() to display student details.

class Student:
    def __init__(self, name, student_id, grade, email):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.email = email
    
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grade: {self.grade}")
        print(f"Email: {self.email}")
        print("-" * 40)


# Create student objects and display details
student1 = Student("Alice Johnson", "S001", "A", "alice@example.com")
student2 = Student("Bob Smith", "S002", "B+", "bob@example.com")
student3 = Student("Charlie Brown", "S003", "A+", "charlie@example.com")

print("Student Details:\n")
student1.display()
student2.display()
student3.display()
