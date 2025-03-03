class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def delete_node(self, key):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        prev = None
        while True:
            if temp.data == key:
                if prev:
                    prev.next = temp.next
                else:
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    self.head = temp.next
                    last.next = self.head
                return
            prev, temp = temp, temp.next
            if temp == self.head:
                break
        print("Node not found")

    def traverse(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

# Usage
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.traverse()
cll.delete_node(2)
cll.traverse()
