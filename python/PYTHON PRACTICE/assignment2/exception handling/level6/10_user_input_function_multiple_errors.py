def get_division_from_user():
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        return first / second
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    return None


result = get_division_from_user()
if result is not None:
    print("Result:", result)