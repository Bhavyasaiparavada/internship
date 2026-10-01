try:
    password = input("Enter a password: ")
    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")
    print("Password accepted.")
except ValueError as error:
    print("Invalid password:", error)