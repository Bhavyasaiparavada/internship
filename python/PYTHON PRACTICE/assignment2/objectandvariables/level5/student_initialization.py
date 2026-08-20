# Question 1: Create a Student class using __init__() to initialize name, age, course, and marks.

class Student:
    def __init__(self, name, age, course, marks):
        """Initialize student attributes"""
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
    
    def display_info(self):
        """Display student information"""
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print("-" * 40)
    
    def is_pass(self, pass_marks=40):
        """Check if student passed"""
        return "Passed" if self.marks >= pass_marks else "Failed"
    
    def get_performance(self):
        """Get performance level"""
        if self.marks >= 80:
            return "Excellent"
        elif self.marks >= 60:
            return "Good"
        elif self.marks >= 40:
            return "Average"
        else:
            return "Poor"


# Create student objects using __init__()
print("STUDENT INFORMATION\n")

student1 = Student("Alice Johnson", 20, "Computer Science", 92)
student2 = Student("Bob Smith", 19, "Engineering", 78)
student3 = Student("Charlie Brown", 21, "Commerce", 65)
student4 = Student("Diana Prince", 20, "Science", 88)

# Display information
student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()

# Check performance
print("Performance Analysis:\n")
print(f"{student1.name} - Marks: {student1.marks}, Status: {student1.is_pass()}, Performance: {student1.get_performance()}")
print(f"{student2.name} - Marks: {student2.marks}, Status: {student2.is_pass()}, Performance: {student2.get_performance()}")
print(f"{student3.name} - Marks: {student3.marks}, Status: {student3.is_pass()}, Performance: {student3.get_performance()}")
print(f"{student4.name} - Marks: {student4.marks}, Status: {student4.is_pass()}, Performance: {student4.get_performance()}")
