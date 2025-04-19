class Node:
    def __init__(self, key):
        self.data = key
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

def find_lca(root, n1, n2):
    if not root:
        return None
    if n1 < root.data and n2 < root.data:
        return find_lca(root.left, n1, n2)
    elif n1 > root.data and n2 > root.data:
        return find_lca(root.right, n1, n2)
    else:
        return root

# Create BST
values = [40, 20, 10, 30, 60, 50, 70]
root = None
for val in values:
    root = insert(root, val)

# Example: Find LCA of 10 and 30
n1, n2 = 10, 30
lca = find_lca(root, n1, n2)
print(f"LCA of {n1} and {n2} is:", lca.data if lca else "Not Found")

# Example: Find LCA of 10 and 70
n3, n4 = 10, 70
lca2 = find_lca(root, n3, n4)
print(f"LCA of {n3} and {n4} is:", lca2.data if lca2 else "Not Found")
