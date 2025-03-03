class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # New previous pointer

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Points to the first node
        self.tail = None  # Points to the last node

    def append(self, data):
        """Appends a node at the end of the DLL."""
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail  # Linking the previous node
            self.tail = node  # Update tail to the new last node

    def display_forward(self):
        """Traverses the list from head to tail."""
        current = self.head
        while current:
            print(current.data, "<->", end=" ")
            current = current.next
        print("None")

    def display_backward(self):
        """Traverses the list from tail to head."""
        current = self.tail
        while current:
            print(current.data, "<->", end=" ")
            current = current.prev
        print("None")

# Example Usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display_forward()  # Output: 10 <-> 20 <-> 30 <-> None
dll.display_backward()  # Output: 30 <-> 20 <-> 10 <-> None



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

        node.next = current.next
        if current.next:
            current.next.prev = node
        current.next = node
        node.prev = current

dll = DoublyLinkedList()
dll.insert_at_beginning(50)
dll.insert_at_position(25, 1)
dll.display_forward()  # Output: 50 <-> 25 <-> None



