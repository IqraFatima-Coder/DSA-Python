class Comment:
    def __init__(self, id, text):
        self.id = id
        self.text = text
        self.replies = []

    def add_reply(self, reply):
        self.replies.append(reply)

    def display(self, level=0):
        print("  " * level + f"{self.id}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)

    def count_replies(self):
        return sum(reply.count_replies() + 1 for reply in self.replies)


# Sample usage
root = Comment(1, "This is the original post")
reply1 = Comment(2, "First reply")
reply2 = Comment(3, "Second reply")
reply1_1 = Comment(4, "Reply to first reply")

root.add_reply(reply1)
root.add_reply(reply2)
reply1.add_reply(reply1_1)

print("Thread:")
root.display()

print("\nTotal replies to comment 1:", root.count_replies())
