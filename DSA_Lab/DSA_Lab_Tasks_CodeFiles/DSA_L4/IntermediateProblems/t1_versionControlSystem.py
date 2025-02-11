class CommitNode:
    def __init__(self, commit_id, message):
        self.commit_id = commit_id
        self.message = message
        self.next = None

class VersionControlSystem:
    def __init__(self):
        self.head = None
        self.commit_count = 0

    def add_commit(self, message):
        self.commit_count += 1
        new_node = CommitNode(self.commit_count, message)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f'Commit {self.commit_count}: "{message}" added.')

    def display_commits(self):
        if not self.head:
            print("No commits found.")
            return

        print("Commit History:")
        temp = self.head
        while temp:
            print(f'Commit {temp.commit_id}: {temp.message}')
            temp = temp.next

# Example Usage
vcs = VersionControlSystem()
vcs.add_commit("Initial commit")
vcs.add_commit("Added login feature")
vcs.add_commit("Fixed logout bug")

vcs.display_commits()
