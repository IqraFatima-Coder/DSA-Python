class ChatQueue:
    def __init__(self):
        self.queue = []

    def send_message(self, sender, message):
        self.queue.insert(0, (sender, message))

    def receive_messages(self):
        while self.queue:
            print(self.queue.pop())

# Example Usage
chat = ChatQueue()
chat.send_message("User1", "Hello!")
chat.send_message("User2", "Hi, how are you?")
chat.receive_messages()
