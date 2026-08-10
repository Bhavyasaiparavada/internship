source = open("image.jpg", "rb")
destination = open("copy.jpg", "wb")

data = source.read()
destination.write(data)

source.close()
destination.close()

print("Image Copied Successfully")