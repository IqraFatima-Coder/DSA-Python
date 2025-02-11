class SinglyLinkedList: 
    def delete(self, data): 
        """Delete a node by value.""" 
        current = self.head 
        prev = None 
 
        while current: 
            if current.data == data: 
                if prev: 
                    prev.next = current.next 
                else: 
                    self.head = current.next 
                return 
            prev = current 
            current = current.next 
 
# Example Usage 
sll = SinglyLinkedList() 
sll.delete(20)  # Deletes 20 from the list 
sll.display()