class ProfileNode:
    def __init__(self, username):
        self.username = username
        self.connections = []  # لیسٹ میں کنکشنز رکھے جائیں گے
        self.next = None

class LinkedInNetwork:
    def __init__(self):
        self.head = None

    def add_profile(self, username):
        new_profile = ProfileNode(username)
        if not self.head:
            self.head = new_profile
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_profile
        print(f'Profile "{username}" added to the network.')

    def add_connection(self, username, connection_username):
        temp = self.head
        while temp:
            if temp.username == username:
                temp.connections.append(connection_username)
                print(f'Connection between {username} and {connection_username} added.')
                return
            temp = temp.next
        print(f'Profile {username} not found.')

    def display_network(self):
        if not self.head:
            print("No profiles in the network.")
            return

        temp = self.head
        while temp:
            print(f'Profile: {temp.username} | Connections: {", ".join(temp.connections)}')
            temp = temp.next

# Example Usage
network = LinkedInNetwork()
network.add_profile("john_doe")
network.add_profile("alice_smith")
network.add_profile("bob_jones")

network.add_connection("john_doe", "alice_smith")
network.add_connection("alice_smith", "bob_jones")

network.display_network()
