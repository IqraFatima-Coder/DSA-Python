class Node:
    def __init__(self, text):
        self.text = text
        self.next = None
        self.prev = None

class TextEditor:
    def __init__(self):
        self.head = None
        self.current = None

    def write(self, text):
        new_node = Node(text)
        if not self.head:
            self.head = new_node
            self.current = new_node
        else:
            new_node.prev = self.current
            self.current.next = new_node
            self.current = new_node

    def undo(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
        print("Current Text:", self.current.text if self.current else "Empty")

    def redo(self):
        if self.current and self.current.next:
            self.current = self.current.next
        print("Current Text:", self.current.text if self.current else "Empty")

# Usage
editor = TextEditor()
editor.write("Hello")
editor.write("World")
editor.undo()
editor.redo()
