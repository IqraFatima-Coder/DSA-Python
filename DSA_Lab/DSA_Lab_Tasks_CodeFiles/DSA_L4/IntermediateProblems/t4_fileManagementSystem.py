class FileNode:
    def __init__(self, file_name):
        self.file_name = file_name
        self.next = None

class Directory:
    def __init__(self, directory_name):
        self.directory_name = directory_name
        self.files = None

    def create_file(self, file_name):
        new_file = FileNode(file_name)
        if not self.files:
            self.files = new_file
        else:
            temp = self.files
            while temp.next:
                temp = temp.next
            temp.next = new_file
        print(f'File "{file_name}" created in {self.directory_name}.')

    def delete_file(self, file_name):
        if not self.files:
            print("No files in this directory.")
            return

        if self.files.file_name == file_name:
            self.files = self.files.next
            print(f'File "{file_name}" deleted from {self.directory_name}.')
            return

        temp = self.files
        while temp.next and temp.next.file_name != file_name:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next
            print(f'File "{file_name}" deleted from {self.directory_name}.')
        else:
            print(f'File "{file_name}" not found in {self.directory_name}.')

    def display_files(self):
        if not self.files:
            print(f"No files in {self.directory_name}.")
            return

        print(f"Files in {self.directory_name}:")
        temp = self.files
        while temp:
            print(f'- {temp.file_name}')
            temp = temp.next

# Example Usage
directory = Directory("Documents")
directory.create_file("file1.txt")
directory.create_file("file2.txt")
directory.create_file("file3.txt")

directory.display_files()

directory.delete_file("file2.txt")
directory.display_files()
