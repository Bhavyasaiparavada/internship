class InvalidPasswordError(Exception):
    pass


def validate_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Password must have at least 8 characters.")
    return True


try:
    validate_password(input("Enter a password: "))
    print("Password accepted.")
except InvalidPasswordError as error:
    print(error)