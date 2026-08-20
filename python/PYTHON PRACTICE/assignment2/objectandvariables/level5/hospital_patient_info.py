# Question 10: Create a HospitalPatient class using __init__() and a method to display patient information.

class HospitalPatient:
    def __init__(self, patient_id, name, age, gender, contact_number, medical_condition, admission_date, doctor_name):
        """Initialize hospital patient attributes"""
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number
        self.medical_condition = medical_condition
        self.admission_date = admission_date
        self.doctor_name = doctor_name
        self.medications = []
        self.vital_signs = {}
    
    def display_patient_info(self):
        """Display complete patient information"""
        print(f"\n{'='*60}")
        print(f"PATIENT INFORMATION")
        print(f"{'='*60}")
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years")
        print(f"Gender: {self.gender}")
        print(f"Contact: {self.contact_number}")
        print(f"Medical Condition: {self.medical_condition}")
        print(f"Admission Date: {self.admission_date}")
        print(f"Doctor Assigned: {self.doctor_name}")
        print(f"{'='*60}\n")
    
    def display_brief_info(self):
        """Display brief patient information"""
        print(f"{self.patient_id:8} | {self.name:20} | Age: {self.age:3} | {self.medical_condition:20} | Dr. {self.doctor_name}")
    
    def add_medication(self, medication_name, dosage, frequency):
        """Add medication to patient's treatment"""
        medication = {
            "name": medication_name,
            "dosage": dosage,
            "frequency": frequency
        }
        self.medications.append(medication)
        print(f"✓ Medication added: {medication_name} - {dosage} {frequency}")
    
    def display_medications(self):
        """Display patient's medications"""
        print(f"\nMedications for {self.name}:")
        print("-" * 60)
        if len(self.medications) == 0:
            print("  No medications assigned")
        else:
            for i, med in enumerate(self.medications, 1):
                print(f"  {i}. {med['name']}")
                print(f"     Dosage: {med['dosage']}")
                print(f"     Frequency: {med['frequency']}")
        print()
    
    def record_vital_signs(self, blood_pressure, temperature, heart_rate, oxygen_level):
        """Record patient's vital signs"""
        self.vital_signs = {
            "blood_pressure": blood_pressure,
            "temperature": temperature,
            "heart_rate": heart_rate,
            "oxygen_level": oxygen_level
        }
        print(f"✓ Vital signs recorded for {self.name}")
    
    def display_vital_signs(self):
        """Display patient's vital signs"""
        print(f"\nVital Signs for {self.name}:")
        print("-" * 60)
        if len(self.vital_signs) == 0:
            print("  No vital signs recorded")
        else:
            print(f"  Blood Pressure: {self.vital_signs.get('blood_pressure', 'N/A')}")
            print(f"  Temperature: {self.vital_signs.get('temperature', 'N/A')} °C")
            print(f"  Heart Rate: {self.vital_signs.get('heart_rate', 'N/A')} bpm")
            print(f"  Oxygen Level: {self.vital_signs.get('oxygen_level', 'N/A')} %")
        print()
    
    def get_health_status(self):
        """Get patient's health status based on vital signs"""
        if len(self.vital_signs) == 0:
            return "Status Unknown"
        
        hr = self.vital_signs.get('heart_rate', 0)
        temp = self.vital_signs.get('temperature', 36.5)
        
        if 60 <= hr <= 100 and 36.5 <= temp <= 37.5:
            return "Stable"
        elif hr > 100 or temp > 37.5:
            return "Critical"
        else:
            return "Needs Monitoring"
    
    def display_detailed_report(self):
        """Display complete patient report"""
        print(f"\n{'='*60}")
        print(f"COMPLETE PATIENT REPORT")
        print(f"{'='*60}")
        self.display_patient_info()
        self.display_medications()
        self.display_vital_signs()
        print(f"Health Status: {self.get_health_status()}")
        print(f"{'='*60}\n")
    
    def update_patient_condition(self, new_condition):
        """Update patient's medical condition"""
        old_condition = self.medical_condition
        self.medical_condition = new_condition
        print(f"✓ Medical condition updated for {self.name}")
        print(f"  From: {old_condition}")
        print(f"  To: {new_condition}")


# Create hospital patient objects using __init__()
print("HOSPITAL PATIENT MANAGEMENT SYSTEM\n")

patient1 = HospitalPatient("P001", "John Smith", 45, "Male", "555-0101", "Hypertension", "2024-08-18", "Dr. Sarah Johnson")
patient2 = HospitalPatient("P002", "Mary Johnson", 62, "Female", "555-0102", "Diabetes", "2024-08-17", "Dr. Michael Brown")
patient3 = HospitalPatient("P003", "Robert Davis", 38, "Male", "555-0103", "Pneumonia", "2024-08-19", "Dr. Lisa Chen")
patient4 = HospitalPatient("P004", "Emily Wilson", 55, "Female", "555-0104", "Heart Disease", "2024-08-16", "Dr. James Lee")

# Display patient information
print("PATIENT REGISTRY")
print("=" * 60)
patient1.display_patient_info()
patient2.display_patient_info()
patient3.display_patient_info()

# Add medications
print("\nADDING MEDICATIONS")
print("=" * 60 + "\n")

print(f"For {patient1.name}:")
patient1.add_medication("Lisinopril", "10mg", "Once daily")
patient1.add_medication("Hydrochlorothiazide", "25mg", "Once daily")

print(f"\nFor {patient2.name}:")
patient2.add_medication("Metformin", "500mg", "Twice daily")
patient2.add_medication("Linagliptin", "5mg", "Once daily")

print(f"\nFor {patient3.name}:")
patient3.add_medication("Amoxicillin", "500mg", "Three times daily")
patient3.add_medication("Cough Syrup", "10ml", "As needed")

# Record vital signs
print("\n\nRECORDING VITAL SIGNS")
print("=" * 60 + "\n")

patient1.record_vital_signs("120/80", 36.8, 72, 98)
patient2.record_vital_signs("135/85", 37.2, 78, 96)
patient3.record_vital_signs("118/76", 38.5, 92, 94)
patient4.record_vital_signs("128/82", 36.9, 68, 99)

# Display brief patient list
print("\n\nPATIENT LIST")
print("=" * 60)
print(f"{'ID':<8} | {'Name':<20} | {'Age':<5} | {'Condition':<20} | {'Doctor':<20}")
print("-" * 80)
patient1.display_brief_info()
patient2.display_brief_info()
patient3.display_brief_info()
patient4.display_brief_info()

# Display detailed reports
print("\n\nDETAILED PATIENT REPORTS")
print("=" * 60)
patient1.display_detailed_report()
patient2.display_detailed_report()
patient3.display_detailed_report()

# Update patient condition
print("\nUPDATING PATIENT CONDITIONS")
print("=" * 60 + "\n")
patient3.update_patient_condition("Recovering from Pneumonia")
patient4.update_patient_condition("Heart Condition Improving")

# Display updated reports for changed patients
print("\n\nUPDATED PATIENT REPORTS")
print("=" * 60)
patient3.display_detailed_report()
patient4.display_detailed_report()

# Patient health summary
print("\nPATIENT HEALTH SUMMARY")
print("=" * 60)
all_patients = [patient1, patient2, patient3, patient4]
for patient in all_patients:
    status = patient.get_health_status()
    print(f"{patient.name:20} | Condition: {patient.medical_condition:25} | Status: {status}")
