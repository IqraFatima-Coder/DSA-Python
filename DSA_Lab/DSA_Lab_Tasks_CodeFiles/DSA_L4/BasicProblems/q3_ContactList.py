class ContactNode:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

class ContactList:
    def __init__(self):
        self.head = None

    def add_contact(self, name, phone):
        new_node = ContactNode(name, phone)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f'Contact "{name}" added.')

    def search_contact(self, name):
        temp = self.head
        while temp:
            if temp.name.lower() == name.lower():
                print(f'Found: {temp.name} - {temp.phone}')
                return
            temp = temp.next
        print(f'Contact "{name}" not found.')

    def display_contacts(self):
        if not self.head:
            print("No contacts available.")
            return

        print("Contact List:")
        temp = self.head
        while temp:
            print(f"- {temp.name}: {temp.phone}")
            temp = temp.next

# Example Usage
contacts = ContactList()
contacts.add_contact("Ali", "03001234567")
contacts.add_contact("Ayesha", "03219876543")
contacts.add_contact("Ahmed", "03111223344")

contacts.display_contacts()
contacts.search_contact("Ayesha")
contacts.search_contact("Zain")
