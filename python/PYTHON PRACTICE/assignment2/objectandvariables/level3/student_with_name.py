# Question 7: Create a Student class with a class variable representing the school/college name
# and an instance variable representing the student's name.

class StudentDetail:
    school_name = "Central High School"
    
    def __init__(self, student_name, student_id, grade):
        self.student_name = student_name
        self.student_id = student_id
        self.grade = grade
    
    def display_student_info(self):
        print(f"School: {StudentDetail.school_name}")
        print(f"Student Name: {self.student_name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grade: {self.grade}")
        print("-" * 40)
    
    @classmethod
    def change_school_name(cls, new_school_name):
        cls.school_name = new_school_name
        print(f"School name updated to: {cls.school_name}")
    
    def get_student_name(self):
        return self.student_name


# Create student objects
student1 = StudentDetail("Alice Johnson", "S001", "A")
student2 = StudentDetail("Bob Smith", "S002", "B")
student3 = StudentDetail("Charlie Brown", "S003", "A+")
student4 = StudentDetail("Diana Prince", "S004", "A")

# Display student information
print(f"School/College Name: {StudentDetail.school_name}\n")
student1.display_student_info()
student2.display_student_info()
student3.display_student_info()
student4.display_student_info()

# Display individual student names
print("\n--- Student Names (Instance Variables) ---")
print(f"Student 1: {student1.get_student_name()}")
print(f"Student 2: {student2.get_student_name()}")
print(f"Student 3: {student3.get_student_name()}")
print(f"Student 4: {student4.get_student_name()}")

# Change school name
print("\n--- Updating School Name ---")
StudentDetail.change_school_name("Xavier's School of Excellence")

print("\n--- Updated Student Info ---")
student1.display_student_info()
