text = "hello"

try:
    text.not_a_real_method()
except AttributeError:
    print("That object does not have this attribute or method.")