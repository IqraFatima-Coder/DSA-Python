from datetime import datetime

class MessageNode:
    def __init__(self, message, timestamp):
        self.message = message
        self.timestamp = timestamp
        self.next = None

class ChatHistory:
    def __init__(self):
        self.head = None

    def send_message(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_message = MessageNode(message, timestamp)
        if not self.head:
            self.head = new_message
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_message
        print(f'Message sent at {timestamp}: "{message}"')

    def display_chat(self):
        if not self.head:
            print("No chat history.")
            return

        print("Chat History:")
        temp = self.head
        while temp:
            print(f'{temp.timestamp} - {temp.message}')
            temp = temp.next

# Example Usage
chat = ChatHistory()
chat.send_message("Hello, how are you?")
chat.send_message("I am doing well, thank you!")
chat.send_message("What's up?")

chat.display_chat()
