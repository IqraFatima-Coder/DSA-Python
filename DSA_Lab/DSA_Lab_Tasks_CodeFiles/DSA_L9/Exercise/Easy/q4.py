class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# Pretty-print tree recursively with indentation.
def display_tree(node, level=0):
    if node is None:
        return
    print("  " * level + str(node.value))
    for child in node.children:
        display_tree(child, level + 1)


if __name__ == "__main__":
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    root.children.extend([child1, child2])
    # Grandchildren for child1
    child1.children.extend([TreeNode(4), TreeNode(5)])
    # Grandchild for child2
    child2.children.append(TreeNode(6))
    
    def find_depth(node, target, current_depth=0):
        if node is None:
            return -1
        if node.value == target:
            return current_depth
        for child in node.children:
            res = find_depth(child, target, current_depth + 1)
            if res != -1:
                return res
        return -1

    target = 5
    depth = find_depth(root, target)
    if depth != -1:
        print(f" Depth of node {target} is {depth}")
    else:
        print(f"4. Node {target} not found")
