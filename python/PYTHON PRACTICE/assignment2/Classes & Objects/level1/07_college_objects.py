class College:
    def __init__(self, name, location, course):
        self.name = name
        self.location = location
        self.course = course


colleges = [
    College("City College", "Chennai", "Science"),
    College("Green College", "Delhi", "Arts"),
    College("Central College", "Mumbai", "Commerce"),
]
for college in colleges:
    print(college.name, college.location, college.course)