from abc import ABC, abstractmethod


class Authentication(ABC):
    @abstractmethod
    def login(self, user):
        pass

    @abstractmethod
    def logout(self, user):
        pass


class PasswordAuth(Authentication):
    def login(self, user):
        return f"{user} logged in using a password."

    def logout(self, user):
        return f"{user} logged out from password authentication."


class OTPAuth(Authentication):
    def login(self, user):
        return f"{user} logged in using an OTP."

    def logout(self, user):
        return f"{user} logged out from OTP authentication."


for authentication in (PasswordAuth(), OTPAuth()):
    print(authentication.login("Riya"))
    print(authentication.logout("Riya"))
