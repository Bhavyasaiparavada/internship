file = open("login.txt", "w")

username = input("Enter Username: ")
password = input("Enter Password: ")

file.write(username + "\n")
file.write(password)

file.close()

print("Registration Successful")