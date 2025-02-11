class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title):
        new_node = SongNode(title)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f'Song "{title}" added to the playlist.')

    def remove_song(self, title):
        if not self.head:
            print("Playlist is empty.")
            return

        if self.head.title == title:
            self.head = self.head.next
            print(f'Song "{title}" removed from the playlist.')
            return

        temp = self.head
        while temp.next and temp.next.title != title:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next
            print(f'Song "{title}" removed from the playlist.')
        else:
            print(f'Song "{title}" not found in the playlist.')

    def display_playlist(self):
        if not self.head:
            print("No songs in the playlist.")
            return

        print("Playlist:")
        temp = self.head
        while temp:
            print(f"- {temp.title}")
            temp = temp.next

# Example Usage
playlist = Playlist()
playlist.add_song("Shape of You")
playlist.add_song("Believer")
playlist.add_song("Senorita")

playlist.display_playlist()

playlist.remove_song("Believer")
playlist.display_playlist()
