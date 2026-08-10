subjects = ["Python", "Java", "C", "HTML", "SQL"]

try:
    index = int(input("Enter Index: "))
    print(subjects[index])

except ValueError:
    print("Invalid Input")

except IndexError:
    print("Invalid Index")