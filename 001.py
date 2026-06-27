class Hospital:
    def __init__(self):
        self.patients = {}      # patient_name: details
        self.appointments = {}  # patient_name: doctor
        self.doctors = ["Dr. Ahmed", "Dr. Fatima", "Dr. Ali", "Dr. Sara"]
    
    def add_patient(self):
        name = input("Enter patient full name: ")
        if name in self.patients:
            print("Patient already exists!")
            return
        age = input("Enter age: ")
        disease = input("Enter disease/complaint: ")
        self.patients[name] = {"age": age, "disease": disease}
        print(f"Patient {name} added successfully!")
    
    def book_appointment(self):
        name = input("Enter patient name: ")
        if name not in self.patients:
            print("Patient not found! Add patient first.")
            return
        print("Available Doctors:")
        for i, doc in enumerate(self.doctors, 1):
            print(f"{i}. {doc}")
        try:
            doc_choice = int(input("Choose doctor number: ")) - 1
            doctor = self.doctors[doc_choice]
            self.appointments[name] = doctor
            print(f"Appointment booked with {doctor}")
        except:
            print("Invalid choice!")
    
    def show_patient_history(self):
        name = input("Enter patient name: ")
        if name in self.patients:
            print("\n--- Patient History ---")
            print(f"Name: {name}")
            print(f"Age: {self.patients[name]['age']}")
            print(f"Disease: {self.patients[name]['disease']}")
            if name in self.appointments:
                print(f"Appointment: {self.appointments[name]}")
        else:
            print("Patient not found!")
    
    def show_all_doctors(self):
        print("\n--- All Doctors ---")
        for doc in self.doctors:
            print(doc)
    
    def cancel_appointment(self):
        name = input("Enter patient name: ")
        if name in self.appointments:
            del self.appointments[name]
            print("Appointment cancelled successfully!")
        else:
            print("No appointment found for this patient!")


# Main Program
hospital = Hospital()   # Object banaya

while True:
    print("\n" + "="*40)
    print("1. Add Patient")
    print("2. Book Appointment")
    print("3. Show Patient History")
    print("4. Show All Doctors")
    print("5. Cancel Appointment")
    print("6. Exit")
    print("="*40)
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        hospital.add_patient()
    elif choice == "2":
        hospital.book_appointment()
    elif choice == "3":
        hospital.show_patient_history()
    elif choice == "4":
        hospital.show_all_doctors()
    elif choice == "5":
        hospital.cancel_appointment()
    elif choice == "6":
        print("Thank you! Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")