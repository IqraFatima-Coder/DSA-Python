class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def delete(self, data):
        """Deletes a node by value in a Circular Linked List."""
        if self.head is None:
            print("List is empty!")
            return

        current = self.head
        prev = None
        while True:
            if current.data == data:
                if prev is not None:
                    prev.next = current.next
                else:
                    # If only one node is in the list
                    if current.next == self.head:
                        self.head = None
                    else:
                        self.head = current.next
                        temp = self.head
                        while temp.next != current:
                            temp = temp.next
                        temp.next = self.head
                return

            prev = current
            current = current.next
            if current == self.head:
                break
        print("Element not found!")
    
    def display(self):
        """Displays the Circular Linked List."""
        if self.head is None:
            print("List is empty!")
            return
        current = self.head
        while True:
            print(current.data, "->", end=" ")
            current = current.next
            if current == self.head:
                break
        print("(Back to head)")

# Example Usage
cll = CircularLinkedList()
# Assume we have a method to add elements before deleting
dummy_node = Node(10)
dummy_node.next = dummy_node  # Pointing to itself to create a circular link
cll.head = dummy_node

cll.delete(10)
cll.display()  # Output: List is empty!
