def get_item(items, index):
    try:
        return items[index]
    except IndexError:
        print("That index is outside the list.")
        return None


print(get_item(["cat", "dog", "bird"], 1))
print(get_item(["cat", "dog", "bird"], 5))