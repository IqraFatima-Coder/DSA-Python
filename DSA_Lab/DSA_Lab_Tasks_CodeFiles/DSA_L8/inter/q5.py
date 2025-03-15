class RideQueue:
    def __init__(self):
        self.queue = []

    def request_ride(self, passenger):
        self.queue.insert(0, passenger)

    def assign_ride(self, driver):
        if self.queue:
            return f"{self.queue.pop()} is assigned to {driver}."
        return "No passengers waiting."

# Example Usage
rq = RideQueue()
rq.request_ride("Alice")
print(rq.assign_ride("Driver1"))  # Alice is assigned to Driver1
