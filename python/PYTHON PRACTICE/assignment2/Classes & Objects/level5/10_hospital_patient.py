class HospitalPatient:
    def __init__(self, name, age, disease, doctor_name):
        self.name = name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

    def display(self):
        print(self.name, self.age, self.disease, self.doctor_name)


patient = HospitalPatient("Ravi", 35, "Flu", "Dr. Rao")
patient.display()