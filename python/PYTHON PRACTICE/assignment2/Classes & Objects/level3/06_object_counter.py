class Item:
    object_count = 0

    def __init__(self):
        Item.object_count += 1


first_item = Item()
second_item = Item()
third_item = Item()
print("Objects created:", Item.object_count)