#Create a string containing only numbers and check it using isdigit().
#Create a string containing alphabets and numbers and check it using isalnum().
#Create a string containing spaces and check it using isspace().
#Create a string and check whether it contains lowercase letters using islower().
#Create a string and check whether it contains uppercase letters using isupper().
#Create a string and check whether it is in title case using istitle().
#Ask the user to enter a username and check whether it contains only alphabets and numbers.
#Ask the user to enter a password and check whether it contains at least one digit.
#Ask the user to enter a string and check whether it is empty or contains characters.
#Ask the user to enter an email address and check whether it contains "@" and ".".
name="12345"
print(name.isdigit())

name="1234sfg5@#"
print(name.isalnum())

name="  bhavya sai"
name1=" "
print(name.isspace())
print(name1.isspace())

name="bhavya"
print(name.islower())

name="B"
print(name.isupper())

name="Bhavya SAI Is In The CLass"
name1="Bhavya Sai Is In The Class"
print(name1.istitle())
print(name.istitle())

uname=input("Enter username:")
print(uname.isalnum())

password=input("Enter password:")
for x in password:
    if x.isdigit():
        print("password has number")
        break
    else:
        print("no number in password") 

uname=input("Enter string:")
if uname.strip()==" ":
       print("empty")
       break
 else:
       print("contains characters") 
       break













