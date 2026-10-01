class Doctor:
    def __init__(self, name):
        self.name = name


class Patient:
    def __init__(self, name):
        self.name = name


class BillingService:
    def bill(self, patient):
        print("Bill created for", patient)


class Hospital:
    def __init__(self):
        self.doctors = [Doctor("Dr. Lee")]
        self.patients = [Patient("Asha")]

    def bill_patient(self, service):
        service.bill(self.patients[0].name)


hospital = Hospital()
print("Doctor:", hospital.doctors[0].name)
hospital.bill_patient(BillingService())
