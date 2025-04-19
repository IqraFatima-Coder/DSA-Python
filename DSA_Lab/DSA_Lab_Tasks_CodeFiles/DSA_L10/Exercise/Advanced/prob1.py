class BookNode:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.left = None
        self.right = None

def insert_book(root, title, isbn):
    if root is None:
        return BookNode(title, isbn)
    if title < root.title:
        root.left = insert_book(root.left, title, isbn)
    elif title > root.title:
        root.right = insert_book(root.right, title, isbn)
    return root

def delete_book(root, title):
    if root is None:
        return root
    if title < root.title:
        root.left = delete_book(root.left, title)
    elif title > root.title:
        root.right = delete_book(root.right, title)
    else:
        # Node to be deleted is found
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.title = temp.title
        root.isbn = temp.isbn
        root.right = delete_book(root.right, temp.title)
    return root

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(f"Title: {root.title}, ISBN: {root.isbn}")
        inorder_traversal(root.right)

# Example Usage
root = None
root = insert_book(root, "Harry Potter", "9780747532743")
root = insert_book(root, "The Hobbit", "9780547928227")
root = insert_book(root, "Pride and Prejudice", "9781503290563")
root = insert_book(root, "1984", "9780451524935")

print("Books in Alphabetical Order:")
inorder_traversal(root)

print("\nDeleting 'The Hobbit'...")
root = delete_book(root, "The Hobbit")

print("\nBooks after Deletion:")
inorder_traversal(root)
