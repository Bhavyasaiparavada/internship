class InvalidUsernameError(Exception):
    pass


try:
    username = input("Enter a username: ")
    if not username.strip():
        raise InvalidUsernameError("Username cannot be empty.")
    print("Username accepted:", username)
except InvalidUsernameError as error:
    print(error)