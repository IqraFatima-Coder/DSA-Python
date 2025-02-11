class SinglyLinkedList: 
    def search(self, data): 
        """Search for an element in the linked list.""" 
        current = self.head 
        while current: 
            if current.data == data: 
                return True 
            current = current.next 
        return False 
 
# Example Usage 
sll = SinglyLinkedList() 
print(sll.search(15))  # True
print(sll.search(100))  # False 