def find_value(data, key):
    try:
        return data[key]
    except KeyError:
        print("The key was not found.")
        return None


print(find_value({"city": "Delhi"}, "city"))
print(find_value({"city": "Delhi"}, "country"))