class Person:
    def role(self):
        print("Person")


class Student(Person):
    def role(self):
        print("I am a student")


class Teacher(Person):
    def role(self):
        print("I am a teacher")


class Doctor(Person):
    def role(self):
        print("I am a doctor")


student = Student()
teacher = Teacher()
doctor = Doctor()
student.role()
teacher.role()
doctor.role()