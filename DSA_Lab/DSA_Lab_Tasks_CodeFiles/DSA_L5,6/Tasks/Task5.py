class Story:
    def __init__(self, content):
        self.content = content
        self.next = None

class StoryViewer:
    def __init__(self):
        self.head = None
        self.current_story = None

    def add_story(self, content):
        """Adds a new story to the circular linked list."""
        story = Story(content)
        if self.head is None:
            self.head = story
            story.next = self.head  # Circular link
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = story
            story.next = self.head  # Pointing back to head
    def view_next_story(self):
        """Moves to the next story."""
        if self.current_story is None:
            self.current_story = self.head  # Start from the first story
        else:
            self.current_story = self.current_story.next  # Move to next
        print(f"Viewing Story: {self.current_story.content}")

    def display_stories(self):
        """Displays all stories."""
        if self.head is None:
            print("No stories available!")
            return
        temp = self.head
        while True:
            print(f"Story: {temp.content}")
            temp = temp.next
            if temp == self.head:
                break

# Example Usage
stories = StoryViewer()
stories.add_story("User1's Story")
stories.add_story("User2's Story")
stories.add_story("User3's Story")

print("\nAll Stories in Viewer:")
stories.display_stories()

print("\nSimulating Story Viewing:")
stories.view_next_story()  # Viewing: User1's Story
stories.view_next_story()  # Viewing: User2's Story
stories.view_next_story()  # Viewing: User3's Story
stories.view_next_story()  # Viewing: User1's Story (Cycle Restarts)
