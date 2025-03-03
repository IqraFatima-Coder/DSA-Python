class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        """Inserts a node at the beginning of the DLL."""
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_at_position(self, data, pos):
        """Inserts a node at a specific position in the DLL."""
        node = Node(data)
        if pos == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        for _ in range(pos - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next

        if current is None:
            print("Position out of bounds")
            return

        node.next = current.next
        if current.next:
            current.next.prev = node
        current.next = node
        node.prev = current
    
    def display_forward(self):
        """Displays the DLL from head to tail."""
        current = self.head
        while current:
            print(current.data, "<->", end=" ")
            current = current.next
        print("None")

# Example Usage
dll = DoublyLinkedList()
dll.insert_at_beginning(50)
dll.insert_at_position(25, 1)
dll.display_forward()  # Output: 50 <-> 25 <-> None
