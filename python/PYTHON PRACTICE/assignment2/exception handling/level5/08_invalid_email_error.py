class InvalidEmailError(Exception):
    pass


try:
    email = input("Enter an email address: ")
    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmailError("Enter an email in the form name@example.com.")
    print("Email accepted:", email)
except InvalidEmailError as error:
    print(error)