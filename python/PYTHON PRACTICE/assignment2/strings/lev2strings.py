#Create a string and convert it to uppercase using upper().
#Create a string and convert it to lowercase using lower().
#Create a string and convert the first character to uppercase using capitalize().
#Create a sentence and convert the first letter of every word to uppercase using title().
#Create a string and swap uppercase characters to lowercase and lowercase characters to uppercase using swapcase().
#Create a string containing extra spaces and remove the spaces using strip().
#Create a string with spaces at the beginning and remove them using lstrip().
#Create a string with spaces at the end and remove them using rstrip().
#Create a string and replace one word with another using replace().
#Create a string and count how many times a particular character appears using count().
#Create a string and find the position of a particular character using find().
#Create a string and find the position of a particular word using index().
#Create a string and check whether it starts with a particular word using startswith().
#Create a string and check whether it ends with a particular word using endswith().
#Create a string containing only alphabets and check it using isalpha().

name="bhavya"
print(name.upper())

name="BHAVYA"
print(name.lower())

name="bhavya"
print(name.capitalize())

name=""" my name is bhavya sai
         pursing diploma"""
print(name.title())

name=""" My name IS BHavya Sai HELLo bhavya SAI"""
print(name.swapcase())

name="   hello saii whatsappp  "
print(name.strip())

name="   hello saii whatsappp  "
print(name.lstrip())

name="   hello saii whatsappp  "
print(name.rstrip())

name="Bhavya sai"
print(name.replace("Bhavya","babbu"))

name="Bhavya sai"
print(name.count('a'))

name="Bhavya sai"
print(name.find('B'))
print(name.index("sai"))

name="Bhavya sai"
print(name.startswith("Bhavya"))
print(name.startswith("Bh"))

name="Bhavya sai"
print(name.endswith("Bh"))
print(name.endswith("sai"))

name="Bhavyasai"
print(name.isalpha())





