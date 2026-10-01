from abc import ABC, abstractmethod


class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass


class PasswordAuth(Authentication):
    def login(self):
        return "Logged in with password."

    def logout(self):
        return "Password user logged out."


class OTPAuth(Authentication):
    def login(self):
        return "Logged in with OTP."

    def logout(self):
        return "OTP user logged out."


for method in [PasswordAuth(), OTPAuth()]:
    print(method.login(), method.logout())