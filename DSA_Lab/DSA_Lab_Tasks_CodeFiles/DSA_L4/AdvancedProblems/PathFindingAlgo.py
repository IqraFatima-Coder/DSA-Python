class LocationNode:
    def __init__(self, location_name):
        self.location_name = location_name
        self.next = None

class Pathfinding:
    def __init__(self):
        self.head = None

    def add_location(self, location_name):
        new_location = LocationNode(location_name)
        if not self.head:
            self.head = new_location
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_location
        print(f'Location "{location_name}" added.')

    def find_path(self, start_location, end_location):
        temp = self.head
        path = []
        while temp:
            path.append(temp.location_name)
            if temp.location_name == end_location:
                break
            temp = temp.next
        
        if end_location not in path:
            print("Path not found.")
            return
        
        print("Path found:")
        for loc in path:
            print(f'- {loc}')

# Example Usage
path = Pathfinding()
path.add_location("City Center")
path.add_location("Park")
path.add_location("Library")
path.add_location("Museum")

path.find_path("Park", "Museum")
