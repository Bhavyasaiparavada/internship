def is_positive(number):
    if number > 0:
        return "Positive"
    if number < 0:
        return "Negative"
    return "Zero"


print(is_positive(-2))
