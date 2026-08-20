class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience


teachers = [
    Teacher("Sanjay Rao", "Mathematics", 12),
    Teacher("Pooja Menon", "English", 8),
    Teacher("Deepak Joshi", "Computer Science", 10),
]

for teacher in teachers:
    print("Name:", teacher.name)
    print("Subject:", teacher.subject)
    print("Experience:", teacher.experience, "years")
    print()
