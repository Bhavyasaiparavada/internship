class EducationalInstitution:
    def educate(self):
        print("Providing education")


class Department:
    def __init__(self, name):
        self.name = name


class ExaminationService:
    def conduct_exam(self):
        print("Examination conducted")


class University(EducationalInstitution):
    def __init__(self):
        self.departments = [Department("Science"), Department("Arts")]

    def hold_exam(self, service):
        service.conduct_exam()


university = University()
university.educate()
print("Departments:", ", ".join(department.name for department in university.departments))
university.hold_exam(ExaminationService())
