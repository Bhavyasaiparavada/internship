# Question 2: Create a Student class with a method that accepts marks and returns the grade.

class Student:
    def __init__(self, name, student_id):
        """Initialize student"""
        self.name = name
        self.student_id = student_id
        self.marks = []
    
    def add_marks(self, *subject_marks):
        """Add marks for different subjects"""
        for marks in subject_marks:
            if 0 <= marks <= 100:
                self.marks.append(marks)
            else:
                print(f"Error: Marks must be between 0 and 100. Got {marks}")
    
    def calculate_average(self):
        """Calculate average marks"""
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)
    
    def get_grade(self, marks):
        """
        Accept marks and return the grade
        Method accepts marks as parameter and returns grade
        """
        if marks >= 90:
            return "A+"
        elif marks >= 85:
            return "A"
        elif marks >= 80:
            return "B+"
        elif marks >= 75:
            return "B"
        elif marks >= 70:
            return "C+"
        elif marks >= 65:
            return "C"
        elif marks >= 60:
            return "D"
        else:
            return "F"
    
    def get_grade_description(self, marks):
        """Get grade description based on marks"""
        grade = self.get_grade(marks)
        descriptions = {
            "A+": "Exceptional Performance",
            "A": "Excellent",
            "B+": "Very Good",
            "B": "Good",
            "C+": "Satisfactory",
            "C": "Average",
            "D": "Below Average",
            "F": "Fail"
        }
        return descriptions.get(grade, "Unknown")
    
    def display_student_grades(self):
        """Display grades for all subjects"""
        print(f"\nStudent: {self.name} (ID: {self.student_id})")
        print("=" * 50)
        if len(self.marks) == 0:
            print("No marks recorded")
        else:
            for i, marks in enumerate(self.marks, 1):
                grade = self.get_grade(marks)
                description = self.get_grade_description(marks)
                print(f"Subject {i}: {marks} marks - Grade: {grade} ({description})")
            
            avg = self.calculate_average()
            overall_grade = self.get_grade(avg)
            print(f"\nOverall Average: {avg:.2f}")
            print(f"Overall Grade: {overall_grade}")
        print("=" * 50 + "\n")
    
    def is_passed(self, marks, pass_marks=40):
        """Check if student passed with given marks"""
        return marks >= pass_marks


# Create student objects
print("STUDENT GRADE CALCULATION\n")

student1 = Student("Alice Johnson", "S001")
student2 = Student("Bob Smith", "S002")
student3 = Student("Charlie Brown", "S003")

# Add marks for students
student1.add_marks(92, 88, 95, 90, 87)
student2.add_marks(78, 82, 75, 80, 76)
student3.add_marks(65, 68, 70, 62, 67)

# Display grades
student1.display_student_grades()
student2.display_student_grades()
student3.display_student_grades()

# Test get_grade method with different marks
print("GRADE LOOKUP TABLE")
print("=" * 50)
test_marks = [95, 88, 78, 72, 62, 55, 35]

for marks in test_marks:
    grade = student1.get_grade(marks)
    description = student1.get_grade_description(marks)
    status = "Passed" if student1.is_passed(marks) else "Failed"
    print(f"Marks: {marks:3} | Grade: {grade:3} | {description:25} | {status}")

print()
