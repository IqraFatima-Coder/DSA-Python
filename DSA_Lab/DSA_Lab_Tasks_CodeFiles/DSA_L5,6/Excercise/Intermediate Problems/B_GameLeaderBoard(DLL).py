class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None
        self.prev = None

class Leaderboard:
    def __init__(self):
        self.head = None

    def add_score(self, name, score):
        new_node = Node(name, score)
        if not self.head or self.head.score < score:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.next and temp.next.score >= score:
            temp = temp.next
        new_node.next = temp.next
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

    def display_leaderboard(self):
        temp = self.head
        while temp:
            print(f"{temp.name}: {temp.score}")
            temp = temp.next

# Usage
board = Leaderboard()
board.add_score("Alice", 85)
board.add_score("Bob", 92)
board.add_score("Charlie", 78)
board.display_leaderboard()
