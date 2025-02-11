class SinglyLinkedList: 
    def reverse(self): 
        """Reverse the linked list.""" 
        prev = None 
        current = self.head 
        while current: 
            next_node = current.next 
            current.next = prev 
            prev = current 
            current = next_node 
        self.head = prev 
 
# Example Usage 
sll = SinglyLinkedList() 
sll.reverse() 
sll.display() 