file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")
file3 = open("merged.txt", "w")

file3.write(file1.read())
file3.write(file2.read())

file1.close()
file2.close()
file3.close()