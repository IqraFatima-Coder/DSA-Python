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

def count_single_child_nodes(root):
    if root is None:
        return 0
    count = 0
    if (root.left and not root.right) or (not root.left and root.right):
        count = 1
    return count + count_single_child_nodes(root.left) + count_single_child_nodes(root.right)

# Create BST
values = [40, 20, 60, 10, 30, 50]
root = None
for val in values:
    root = insert(root, val)

print("Nodes with One Child:", count_single_child_nodes(root))
