class CallCenter:
    def __init__(self):
        self.calls = []

    def receive_call(self, caller):
        self.calls.insert(0, caller)

    def answer_call(self):
        if self.calls:
            return f"Answering call from {self.calls.pop()}"
        return "No calls in the queue."

# Example Usage
cc = CallCenter()
cc.receive_call("Customer 1")
cc.receive_call("Customer 2")
print(cc.answer_call())  # Customer 1
