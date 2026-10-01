try:
    marks = float(input("Enter marks from 0 to 100: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    print("Marks:", marks)
except ValueError as error:
    print("Invalid marks:", error)