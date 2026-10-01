def remove_duplicates(values):
    new_values = []
    for value in values:
        if value not in new_values:
            new_values.append(value)
    return new_values


print(remove_duplicates([1, 2, 2, 3, 1, 4]))
