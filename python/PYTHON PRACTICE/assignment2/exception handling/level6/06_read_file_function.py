def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found:", file_name)
    except PermissionError:
        print("Permission denied:", file_name)
    return None


contents = read_file("notes.txt")
if contents is not None:
    print(contents)