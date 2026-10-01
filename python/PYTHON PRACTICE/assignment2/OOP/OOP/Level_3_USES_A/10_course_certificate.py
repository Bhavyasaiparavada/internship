class CertificateGenerator:
    def generate(self, student, course):
        print("Certificate:", student, "completed", course)


class Course:
    def __init__(self, name):
        self.name = name

    def give_certificate(self, generator, student):
        generator.generate(student, self.name)


Course("Python").give_certificate(CertificateGenerator(), "Asha")
