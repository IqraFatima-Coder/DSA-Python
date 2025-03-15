class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return removed_data

def is_palindrome(string):
    q = LinkedQueue()
    for char in string:
        q.enqueue(char)

    stack = []
    temp = q.head
    while temp:
        stack.append(temp.data)
        temp = temp.next

    temp = q.head
    while temp:
        if temp.data != stack.pop():
            return False
        temp = temp.next
    return True

# Example Usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
