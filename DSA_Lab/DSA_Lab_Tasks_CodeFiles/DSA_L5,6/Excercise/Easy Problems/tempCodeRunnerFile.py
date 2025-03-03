class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

# Usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
print("Length:", dll.get_length())
