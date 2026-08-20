# Question 10: Create a Course class with a class variable institute_name
# and instance variables course_name and duration.

class Course:
    institute_name = "Premier Learning Institute"
    
    def __init__(self, course_name, course_code, duration, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.duration = duration  # in weeks
        self.instructor = instructor
    
    def display_course_info(self):
        print(f"Institute: {Course.institute_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Duration: {self.duration} weeks")
        print(f"Instructor: {self.instructor}")
        print("-" * 50)
    
    def get_course_name(self):
        return self.course_name
    
    def get_duration(self):
        return self.duration
    
    def update_duration(self, new_duration):
        self.duration = new_duration
        print(f"Course duration updated to {new_duration} weeks")
    
    @classmethod
    def change_institute_name(cls, new_institute):
        cls.institute_name = new_institute
    
    @classmethod
    def get_institute_name(cls):
        return cls.institute_name


# Create course objects
print(f"Institute: {Course.institute_name}\n")

course1 = Course("Python Programming", "CS101", 12, "Dr. Sarah Chen")
course1.display_course_info()

course2 = Course("Web Development", "CS102", 16, "Mr. John Smith")
course2.display_course_info()

course3 = Course("Data Science Basics", "DS201", 10, "Dr. Emma Watson")
course3.display_course_info()

course4 = Course("Machine Learning", "AI301", 14, "Prof. Alex Johnson")
course4.display_course_info()

course5 = Course("Mobile App Development", "CS203", 12, "Ms. Lisa Brown")
course5.display_course_info()

# Display course instance variables
print("\n--- Course Details ---")
print(f"Course 1: {course1.get_course_name()} ({course1.get_duration()} weeks)")
print(f"Course 2: {course2.get_course_name()} ({course2.get_duration()} weeks)")
print(f"Course 3: {course3.get_course_name()} ({course3.get_duration()} weeks)")
print(f"Course 4: {course4.get_course_name()} ({course4.get_duration()} weeks)")
print(f"Course 5: {course5.get_course_name()} ({course5.get_duration()} weeks)")

# Update course duration
print("\n--- Updating Course Duration ---")
course1.update_duration(14)

# Change institute name
print("\n--- Changing Institute Name ---")
Course.change_institute_name("Advanced Tech Training Academy")
print(f"New Institute Name: {Course.get_institute_name()}")

print("\n--- Updated Course Info ---")
course1.display_course_info()
course2.display_course_info()
