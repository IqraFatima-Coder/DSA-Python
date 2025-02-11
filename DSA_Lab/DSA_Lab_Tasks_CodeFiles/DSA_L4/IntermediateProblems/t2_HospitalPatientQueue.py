class PatientNode:
    def __init__(self, name, age, condition):
        self.name = name
        self.age = age
        self.condition = condition
        self.next = None

class HospitalQueue:
    def __init__(self):
        self.front = None  # Queue کا پہلا مریض
        self.rear = None   # Queue کا آخری مریض

    def add_patient(self, name, age, condition):
        new_node = PatientNode(name, age, condition)
        if not self.rear:  # اگر queue خالی ہے
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f'Patient "{name}" added to the queue.')

    def treat_patient(self):
        if not self.front:
            print("No patients in the queue.")
            return

        print(f'Treating patient: {self.front.name}, Condition: {self.front.condition}')
        self.front = self.front.next  # اگلا مریض queue میں آئے گا

        if not self.front:  # اگر queue خالی ہو جائے
            self.rear = None

    def display_patients(self):
        if not self.front:
            print("No patients in the queue.")
            return

        print("Patients in Queue:")
        temp = self.front
        while temp:
            print(f'- {temp.name}, Age: {temp.age}, Condition: {temp.condition}')
            temp = temp.next

# Example Usage
hospital = HospitalQueue()
hospital.add_patient("Ali", 30, "Fever")
hospital.add_patient("Ayesha", 25, "Flu")
hospital.add_patient("Ahmed", 40, "Headache")

hospital.display_patients()

hospital.treat_patient()
hospital.display_patients()
