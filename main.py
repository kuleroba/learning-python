class Patient:
    def __init__(self, name, appointment, vitals, treatments):
        self.name = name
        self.appointment = appointment
        self.vitals = vitals
        self.treatments = treatments

        print(f"Patient {self.name} has booked an appointment on {self.appointment}.")
