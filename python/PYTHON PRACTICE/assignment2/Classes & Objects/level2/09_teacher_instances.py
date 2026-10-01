class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience


teachers = [Teacher("Maya", "Math", 8), Teacher("John", "Science", 12), Teacher("Sara", "English", 5)]
for teacher in teachers:
    print(teacher.name, teacher.subject, teacher.experience, "years")