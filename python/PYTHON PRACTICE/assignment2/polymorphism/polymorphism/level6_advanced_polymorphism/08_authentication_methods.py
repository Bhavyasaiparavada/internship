from abc import ABC, abstractmethod


class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass


class PasswordLogin(Authentication):
    def login(self):
        print("Logged in with a password")


class OTPLogin(Authentication):
    def login(self):
        print("Logged in with an OTP")


class BiometricLogin(Authentication):
    def login(self):
        print("Logged in with a fingerprint")


password_login = PasswordLogin()
otp_login = OTPLogin()
biometric_login = BiometricLogin()
password_login.login()
otp_login.login()
biometric_login.login()