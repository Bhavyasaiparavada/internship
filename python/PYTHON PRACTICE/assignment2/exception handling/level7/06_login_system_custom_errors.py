class InvalidUsernameError(Exception):
    pass


class InvalidPasswordError(Exception):
    pass


class LoginSystem:
    def login(self, username, password):
        if username != "student":
            raise InvalidUsernameError("Username not found.")
        if password != "python123":
            raise InvalidPasswordError("Password is incorrect.")
        return "Login successful."


system = LoginSystem()
try:
    print(system.login(input("Username: "), input("Password: ")))
except InvalidUsernameError as error:
    print(error)
except InvalidPasswordError as error:
    print(error)