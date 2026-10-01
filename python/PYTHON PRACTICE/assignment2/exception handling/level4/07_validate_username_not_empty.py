try:
    username = input("Enter a username: ")
    if not username.strip():
        raise ValueError("Username cannot be empty.")
    print("Username accepted:", username)
except ValueError as error:
    print("Invalid username:", error)