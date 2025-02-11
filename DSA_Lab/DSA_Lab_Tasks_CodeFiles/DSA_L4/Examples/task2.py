class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
        
class SinglyLinkedList: 
    def insert_at_beginning(self, data): 
        """Insert a node at the beginning of the linked list.""" 
        node = Node(data) 
        node.next = self.head 
        self.head = node
    def insert_at_position(self, data, pos): 
        """Insert a node at a specific position.""" 
        node = Node(data) 
        current = self.head 
        for _ in range(pos - 1): 
            if current.next is None: 
                break 
            current = current.next 
        node.next = current.next 
        current.next = node 
 


# Example Usage 
sll = SinglyLinkedList() 
sll.insert_at_beginning(5) 
sll.insert_at_position(15, 2) 
