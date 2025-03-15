class StackQueue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        """Push data to inbound stack."""
        self.inbound_stack.append(data)

    def dequeue(self):
        """Move elements from inbound to outbound stack, then pop."""
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop() if self.outbound_stack else None

def reverse_queue(q):
    stack = []
    while True:
        item = q.dequeue()
        if item is None:
            break
        stack.append(item)
    for item in reversed(stack):
        q.enqueue(item)

# Example Usage
sq = StackQueue()
sq.enqueue(1)
sq.enqueue(2)
sq.enqueue(3)
reverse_queue(sq)
print("Dequeued:", sq.dequeue())  # 1 (reversed order)
