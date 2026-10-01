try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
    print("Age accepted.")
except ValueError as error:
    print("Invalid age:", error)