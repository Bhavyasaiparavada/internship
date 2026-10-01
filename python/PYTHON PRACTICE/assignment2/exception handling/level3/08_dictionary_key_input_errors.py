colors = {"r": "red", "g": "green", "b": "blue"}

try:
    key = input("Enter a color key (r, g, or b): ")
    if not key:
        raise ValueError("The key cannot be empty.")
    print(colors[key])
except ValueError as error:
    print("Invalid input:", error)
except KeyError:
    print("That key is not in the dictionary.")