class InvalidMarksError(Exception):
    pass


try:
    marks = float(input("Enter marks from 0 to 100: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    print("Marks accepted:", marks)
except ValueError:
    print("Enter marks as a number.")
except InvalidMarksError as error:
    print(error)