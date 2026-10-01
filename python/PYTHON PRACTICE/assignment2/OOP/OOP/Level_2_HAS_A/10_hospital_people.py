class Doctor:
    def __init__(self, name):
        self.name = name


class Patient:
    def __init__(self, name):
        self.name = name


class Hospital:
    def __init__(self):
        self.doctors = [Doctor("Dr. Lee")]
        self.patients = [Patient("Asha"), Patient("Ravi")]


hospital = Hospital()
print("Doctors:", ", ".join(doctor.name for doctor in hospital.doctors))
print("Patients:", ", ".join(patient.name for patient in hospital.patients))
