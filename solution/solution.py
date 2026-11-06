
# HOSPITAL PATIENT MANAGEMENT SYSTEM
# Treatment Plan (used inside Patient)
class TreatmentPlan:
    def __init__(self, description, medication, duration_days):
        self.description = description
        self.medication = medication
        self.duration_days = duration_days

    def to_dict(self):
        return {
            "description": self.description,
            "medication": self.medication,
            "duration_days": self.duration_days
        }


# Patient with encapsulated medical data + composition
class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

        # Encapsulated medical fields
        self.__vitals = {}
        self.__diagnosis = ""

        # Composition
        self.treatment_plans = []

    def add_vitals(self, vitals_dict):
        self.__vitals = vitals_dict

    def set_diagnosis(self, diagnosis):
        self.__diagnosis = diagnosis

    def add_treatment_plan(self, plan: TreatmentPlan):
        self.treatment_plans.append(plan)

    def medical_summary(self):
        return {
            "vitals": self.__vitals,
            "diagnosis": self.__diagnosis,
            "treatments": [t.to_dict() for t in self.treatment_plans]
        }

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "medical": self.medical_summary()
        }


# Doctor class
class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

    def to_dict(self):
        return {
            "doctor_id": self.doctor_id,
            "name": self.name,
            "specialty": self.specialty
        }


# Base appointment (polymorphism parent)
class Appointment:
    def __init__(self, app_id, patient_id, doctor_id, date):
        self.app_id = app_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date

    def calculate_bill(self):
        return 0   # Overridden by subclasses

    def to_dict(self):
        return {
            "app_id": self.app_id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date": self.date,
            "bill": self.calculate_bill()
        }


# Polymorphism subclasses
class RegularAppointment(Appointment):
    def calculate_bill(self):
        return 1000


class EmergencyAppointment(Appointment):
    def calculate_bill(self):
        return 3000


class SurgeryAppointment(Appointment):
    def calculate_bill(self):
        return 15000


# ---------------------------------------
# TEST SAMPLE (optional)
# ---------------------------------------
if __name__ == "__main__":
    # Create patient
    p1 = Patient(1, "John Doe", 32)
    p1.add_vitals({"bp": "120/80", "temp": 37.0})
    p1.set_diagnosis("Migraine")
    p1.add_treatment_plan(TreatmentPlan("Pain relief", "Panadol", 5))

    # Create doctor
    d1 = Doctor(1, "Dr. Patel", "Neurology")

    # Appointments (polymorphism)
    a1 = RegularAppointment(1, p1.patient_id, d1.doctor_id, "2025-01-15")
    a2 = EmergencyAppointment(2, p1.patient_id, d1.doctor_id, "2025-01-16")
    a3 = SurgeryAppointment(3, p1.patient_id, d1.doctor_id, "2025-01-20")

    print("Patient Data:", p1.to_dict())
    print("Regular Appointment Bill:", a1.calculate_bill())
    print("Emergency Appointment Bill:", a2.calculate_bill())
    print("Surgery Appointment Bill:", a3.calculate_bill())

