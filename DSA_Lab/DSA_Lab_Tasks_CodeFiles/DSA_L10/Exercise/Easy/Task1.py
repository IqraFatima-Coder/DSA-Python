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

def inorder(root):
    return inorder(root.left) + [root.data] + inorder(root.right) if root else []

def preorder(root):
    return [root.data] + preorder(root.left) + preorder(root.right) if root else []

def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.data] if root else []

# Example BST
values = [40, 20, 60, 10, 30, 50, 70]
root = None
for val in values:
    root = insert(root, val)

# Perform traversals
print("In-order:", inorder(root))
print("Pre-order:", preorder(root))
print("Post-order:", postorder(root))
