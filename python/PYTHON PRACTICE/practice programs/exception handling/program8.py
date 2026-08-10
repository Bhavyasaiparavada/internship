try:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "" or password == "":
        raise ValueError

    print("Login Successful")

except ValueError:
    print("Username or Password Cannot Be Empty")