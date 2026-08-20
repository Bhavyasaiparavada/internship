# Question 7: Create a Student class using __init__() and a method to calculate grade based on marks.

class StudentGrade:
    def __init__(self, name, student_id, marks_list):
        """Initialize student attributes with list of marks"""
        self.name = name
        self.student_id = student_id
        self.marks_list = marks_list  # List of marks in different subjects
    
    def calculate_total_marks(self):
        """Calculate total marks"""
        return sum(self.marks_list)
    
    def calculate_average_marks(self):
        """Calculate average marks"""
        if len(self.marks_list) == 0:
            return 0
        return self.calculate_total_marks() / len(self.marks_list)
    
    def calculate_grade(self):
        """Calculate grade based on average marks"""
        average = self.calculate_average_marks()
        
        if average >= 90:
            return "A+"
        elif average >= 85:
            return "A"
        elif average >= 80:
            return "B+"
        elif average >= 75:
            return "B"
        elif average >= 70:
            return "C+"
        elif average >= 65:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    
    def get_performance_level(self):
        """Get performance level description"""
        grade = self.calculate_grade()
        performance_map = {
            "A+": "Exceptional",
            "A": "Excellent",
            "B+": "Very Good",
            "B": "Good",
            "C+": "Satisfactory",
            "C": "Average",
            "D": "Below Average",
            "F": "Fail"
        }
        return performance_map.get(grade, "Unknown")
    
    def display_student_report(self):
        """Display complete student report"""
        print(f"\n{'='*60}")
        print(f"STUDENT REPORT")
        print(f"{'='*60}")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Marks: {self.marks_list}")
        print(f"{'='*60}")
        print(f"Total Marks: {self.calculate_total_marks()}")
        print(f"Average Marks: {self.calculate_average_marks():.2f}")
        print(f"Grade: {self.calculate_grade()}")
        print(f"Performance Level: {self.get_performance_level()}")
        print(f"{'='*60}\n")
    
    def is_passed(self, pass_average=40):
        """Check if student passed"""
        return self.calculate_average_marks() >= pass_average
    
    def display_brief_report(self):
        """Display brief report"""
        status = "Passed" if self.is_passed() else "Failed"
        print(f"{self.name:20} | Avg: {self.calculate_average_marks():6.2f} | Grade: {self.calculate_grade():3} | {status}")


# Create student objects using __init__()
print("STUDENT GRADE MANAGEMENT SYSTEM\n")

# Creating students with marks in 5 subjects
student1 = StudentGrade("Alice Johnson", "S001", [92, 88, 95, 90, 87])
student2 = StudentGrade("Bob Smith", "S002", [78, 82, 75, 80, 76])
student3 = StudentGrade("Charlie Brown", "S003", [88, 90, 92, 89, 91])
student4 = StudentGrade("Diana Prince", "S004", [65, 68, 70, 62, 67])
student5 = StudentGrade("Eve Wilson", "S005", [45, 50, 48, 52, 46])

# Display detailed reports
print("DETAILED STUDENT REPORTS")
print("=" * 60)
student1.display_student_report()
student2.display_student_report()
student3.display_student_report()
student4.display_student_report()
student5.display_student_report()

# Display brief reports
print("\nBRIEF SUMMARY")
print("=" * 60)
print(f"{'Student Name':<20} | {'Average':<8} | {'Grade':<5} | {'Status':<10}")
print("-" * 60)
student1.display_brief_report()
student2.display_brief_report()
student3.display_brief_report()
student4.display_brief_report()
student5.display_brief_report()

# Grade distribution
print("\n\nGRADE DISTRIBUTION")
print("=" * 60)
students = [student1, student2, student3, student4, student5]
grade_count = {}

for student in students:
    grade = student.calculate_grade()
    grade_count[grade] = grade_count.get(grade, 0) + 1

for grade in sorted(grade_count.keys(), reverse=True):
    count = grade_count[grade]
    print(f"Grade {grade}: {count} student(s)")

# Pass/Fail statistics
passed = sum(1 for s in students if s.is_passed())
failed = len(students) - passed
print(f"\nTotal Students: {len(students)}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Pass Rate: {(passed/len(students))*100:.1f}%")
