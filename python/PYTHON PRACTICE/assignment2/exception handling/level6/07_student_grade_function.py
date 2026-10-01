def calculate_grade(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 50:
        return "C"
    return "F"


try:
    marks = float(input("Enter marks: "))
    print("Grade:", calculate_grade(marks))
except ValueError as error:
    print("Invalid marks:", error)