class MessageQueue:
    def __init__(self):
        self.queue = []

    def send_message(self, sender, message):
        self.queue.insert(0, (sender, message))

    def receive_message(self):
        return self.queue.pop() if self.queue else "No messages."

# Example Usage
mq = MessageQueue()
mq.send_message("Alice", "Hello Bob!")
print(mq.receive_message())  # ('Alice', 'Hello Bob!')
