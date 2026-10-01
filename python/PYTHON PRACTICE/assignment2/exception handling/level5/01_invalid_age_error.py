class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    print("Age accepted.")
except ValueError:
    print("Enter age as a whole number.")
except InvalidAgeError as error:
    print(error)