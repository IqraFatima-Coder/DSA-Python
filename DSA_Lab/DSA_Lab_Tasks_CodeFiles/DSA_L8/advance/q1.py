class ChatQueue:
    def __init__(self):
        self.queue = []

    def send_message(self, sender, message):
        """Add a new message to the queue."""
        self.queue.insert(0, (sender, message))

    def receive_messages(self):
        """Retrieve messages in FIFO order."""
        while self.queue:
            sender, message = self.queue.pop()
            print(f"{sender}: {message}")

# Example Usage
chat = ChatQueue()
chat.send_message("Alice", "Hello!")
chat.send_message("Bob", "Hi Alice, how are you?")
chat.receive_messages()
