class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def remove_student(self, name):
        if not self.head:
            print("List is empty.")
            return

        if self.head.name == name:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next and temp.next.name != name:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next
        else:
            print("Student not found.")

    def display_students(self):
        temp = self.head
        while temp:
            print(temp.name, end=" -> ")
            temp = temp.next
        print("None")

# Example Usage
students = StudentList()
students.add_student("Ali")
students.add_student("Ayesha")
students.add_student("Ahmed")
students.display_students()

students.remove_student("Ayesha")
students.display_students()
