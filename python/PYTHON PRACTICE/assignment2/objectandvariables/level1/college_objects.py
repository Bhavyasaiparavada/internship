class College:
    def __init__(self, college_name, location, course):
        self.college_name = college_name
        self.location = location
        self.course = course


colleges = [
    College("IIT Madras", "Chennai", "Computer Science"),
    College("IIT Delhi", "New Delhi", "Mechanical Engineering"),
    College("IIT Bombay", "Mumbai", "Electrical Engineering"),
]

for college in colleges:
    print(college.college_name, "-", college.location, "-", college.course)
