class Node:
    def __init__(self, message):
        self.message = message
        self.next = None
        self.prev = None

class ChatHistory:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_message(self, message):
        new_node = Node(message)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def show_history(self):
        temp = self.tail
        while temp:
            print(temp.message)
            temp = temp.prev

# Usage
chat = ChatHistory()
chat.add_message("Hello")
chat.add_message("How are you?")
chat.add_message("I'm good, thanks!")
chat.show_history()
