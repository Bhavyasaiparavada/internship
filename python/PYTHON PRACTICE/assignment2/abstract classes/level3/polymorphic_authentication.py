from abc import ABC, abstractmethod


class Authentication(ABC):
    @abstractmethod
    def login(self, username):
        pass


class PasswordAuth(Authentication):
    def login(self, username):
        return f"{username} logged in using a password."


class OTPAuth(Authentication):
    def login(self, username):
        return f"{username} logged in using an OTP."


class BiometricAuth(Authentication):
    def login(self, username):
        return f"{username} logged in using biometric authentication."


authentication_methods = [PasswordAuth(), OTPAuth(), BiometricAuth()]
for authentication in authentication_methods:
    print(authentication.login("Riya"))
