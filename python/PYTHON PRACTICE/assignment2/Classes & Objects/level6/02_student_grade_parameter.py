class Student:
    def grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 50:
            return "C"
        return "D"


student = Student()
print("Grade:", student.grade(82))