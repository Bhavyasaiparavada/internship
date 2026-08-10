try:
    age = int(input("Enter Age: "))

    if age < 0 or age > 100:
        raise ValueError

    print("Valid Age")

except ValueError:
    print("Invalid Age")