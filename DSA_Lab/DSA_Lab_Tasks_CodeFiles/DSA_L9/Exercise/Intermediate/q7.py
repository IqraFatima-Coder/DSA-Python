class Folder:
    def __init__(self, name):
        self.name = name
        self.subfolders = []

    def display_folder_tree(self, level=0):
        print("  " * level + self.name)
        for sub in self.subfolders:
            sub.display_folder_tree(level + 1)

root_folder = Folder("Root")
docs = Folder("Documents")
photos = Folder("Photos")
root_folder.subfolders.extend([docs, photos])
work = Folder("Work")
personal = Folder("Personal")
docs.subfolders.extend([work, personal])
print("Folder structure:")
root_folder.display_folder_tree()