from abc import ABC, abstractmethod


class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass


class PasswordAuth(Authentication):
    def login(self):
        return "Logged in with password."


class OTPAuth(Authentication):
    def login(self):
        return "Logged in with OTP."


for method in [PasswordAuth(), OTPAuth()]:
    print(method.login())