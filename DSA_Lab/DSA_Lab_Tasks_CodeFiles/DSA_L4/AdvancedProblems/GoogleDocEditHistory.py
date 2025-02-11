class DocumentNode:
    def __init__(self, version, content):
        self.version = version
        self.content = content
        self.next = None

class GoogleDocsHistory:
    def __init__(self):
        self.head = None

    def add_version(self, content):
        version = 1
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            version = temp.version + 1
        new_version = DocumentNode(version, content)
        if not self.head:
            self.head = new_version
        else:
            temp.next = new_version
        print(f'Version {version} added.')

    def display_history(self):
        if not self.head:
            print("No version history available.")
            return

        temp = self.head
        while temp:
            print(f'Version {temp.version}: {temp.content}')
            temp = temp.next

# Example Usage
docs = GoogleDocsHistory()
docs.add_version("First version of the document.")
docs.add_version("Added introduction section.")
docs.add_version("Corrected some grammatical errors.")

docs.display_history()
