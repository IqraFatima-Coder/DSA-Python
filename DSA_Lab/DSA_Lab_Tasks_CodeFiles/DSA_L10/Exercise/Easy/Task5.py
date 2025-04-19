class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def find_min(root):
    while root.left:
        root = root.left
    return root.data

def find_max(root):
    while root.right:
        root = root.right
    return root.data

# Create BST
values = [40, 20, 60, 10, 30, 50, 70]
root = None
for val in values:
    root = insert(root, val)

print("Minimum:", find_min(root))
print("Maximum:", find_max(root))
