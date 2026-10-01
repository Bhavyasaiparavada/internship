class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name


patients = [
    Hospital("Asha", 25, "Flu", "Dr. Rao"),
    Hospital("Ravi", 40, "Cold", "Dr. Kim"),
    Hospital("Mina", 32, "Allergy", "Dr. Shah"),
]
for patient in patients:
    print(patient.patient_name, patient.age, patient.disease, patient.doctor_name)