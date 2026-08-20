class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name


patients = [
    Hospital("Maya Patel", 34, "Dengue", "Dr. Ramesh Kumar"),
    Hospital("Aditya Shah", 47, "Diabetes", "Dr. Priya Nair"),
    Hospital("Sonal Gupta", 29, "Asthma", "Dr. Vivek Rao"),
]

for patient in patients:
    print("Patient name:", patient.patient_name)
    print("Age:", patient.age)
    print("Disease:", patient.disease)
    print("Doctor name:", patient.doctor_name)
    print()
