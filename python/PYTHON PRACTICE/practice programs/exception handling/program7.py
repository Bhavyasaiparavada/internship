try:
    marks = int(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        raise ValueError

    print("Valid Marks")

except ValueError:
    print("Invalid Marks")