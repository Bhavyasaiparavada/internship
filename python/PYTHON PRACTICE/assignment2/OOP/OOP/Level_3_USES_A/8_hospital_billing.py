class BillingService:
    def create_bill(self, patient, amount):
        print("Bill for", patient, ": $", amount)


class Hospital:
    def bill_patient(self, service, patient, amount):
        service.create_bill(patient, amount)


Hospital().bill_patient(BillingService(), "Asha", 120)
