# Question 8: Create a Student class with methods to calculate total marks and average marks.

class StudentMarks:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.marks = {}  # Dictionary to store subject-wise marks
    
    def add_marks(self, subject, marks):
        if 0 <= marks <= 100:
            self.marks[subject] = marks
            print(f"✓ Marks added for {subject}: {marks}")
        else:
            print(f"Error: Marks must be between 0 and 100!")
    
    def calculate_total_marks(self):
        total = sum(self.marks.values())
        return total
    
    def calculate_average_marks(self):
        if len(self.marks) == 0:
            return 0
        return self.calculate_total_marks() / len(self.marks)
    
    def display_marks(self):
        print(f"\nStudent: {self.student_name}")
        print(f"Student ID: {self.student_id}")
        print("-" * 40)
        for subject, marks in self.marks.items():
            print(f"{subject}: {marks}")
        print("-" * 40)
        print(f"Total Marks: {self.calculate_total_marks()}")
        print(f"Average Marks: {self.calculate_average_marks():.2f}")
        num_subjects = len(self.marks)
        print(f"Number of Subjects: {num_subjects}")
        print()
    
    def get_performance_grade(self):
        avg = self.calculate_average_marks()
        if avg >= 90:
            return "A+ (Excellent)"
        elif avg >= 80:
            return "A (Very Good)"
        elif avg >= 70:
            return "B (Good)"
        elif avg >= 60:
            return "C (Average)"
        else:
            return "D (Below Average)"
    
    def display_report(self):
        self.display_marks()
        print(f"Performance Grade: {self.get_performance_grade()}")
        print("=" * 40 + "\n")


# Create student objects
student1 = StudentMarks("Alice Johnson", "S001")
student2 = StudentMarks("Bob Smith", "S002")
student3 = StudentMarks("Charlie Brown", "S003")

# Add marks for student1
print("Adding marks for Alice Johnson:")
student1.add_marks("English", 85)
student1.add_marks("Mathematics", 92)
student1.add_marks("Science", 88)
student1.add_marks("History", 80)
student1.add_marks("Computer Science", 95)

# Add marks for student2
print("\nAdding marks for Bob Smith:")
student2.add_marks("English", 78)
student2.add_marks("Mathematics", 82)
student2.add_marks("Science", 75)
student2.add_marks("History", 88)
student2.add_marks("Computer Science", 85)

# Add marks for student3
print("\nAdding marks for Charlie Brown:")
student3.add_marks("English", 92)
student3.add_marks("Mathematics", 88)
student3.add_marks("Science", 95)
student3.add_marks("History", 90)
student3.add_marks("Computer Science", 91)

# Display reports
print("\n" + "=" * 40)
print("STUDENT REPORTS")
print("=" * 40)

student1.display_report()
student2.display_report()
student3.display_report()

# Summary
print("SUMMARY")
print("-" * 40)
print(f"Average of all students:")
all_averages = [student1.calculate_average_marks(), 
                student2.calculate_average_marks(), 
                student3.calculate_average_marks()]
print(f"Class Average: {sum(all_averages) / len(all_averages):.2f}")
