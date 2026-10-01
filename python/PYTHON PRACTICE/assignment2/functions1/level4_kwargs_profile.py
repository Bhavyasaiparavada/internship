def create_profile(**profile):
    for key, value in profile.items():
        print(key, ":", value)
    return profile


create_profile(name="Alex", city="London", hobby="reading")
