
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
    elif key > root.data:
        root.right = insert(root.right, key)
    return root


def root_to_leaf_paths(root, path=[]):
    if not root:
        return
    path.append(root.data)
    if not root.left and not root.right:
        print(" -> ".join(map(str, path)))
    else:
        root_to_leaf_paths(root.left, path[:])
        root_to_leaf_paths(root.right, path[:])


# Example Usage
values = [50, 30, 70, 20, 40, 60, 80]
root = None
for v in values:
    root = insert(root, v)


root_to_leaf_paths(root)
