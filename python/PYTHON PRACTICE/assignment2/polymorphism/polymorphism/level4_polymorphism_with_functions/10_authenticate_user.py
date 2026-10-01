class PasswordLogin:
    def login(self):
        print("Logged in with a password")


class OTPLogin:
    def login(self):
        print("Logged in with an OTP")


def authenticate_user(user):
    user.login()


authenticate_user(PasswordLogin())
authenticate_user(OTPLogin())