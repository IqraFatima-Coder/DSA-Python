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
# 3. Count the number of direct children of the root node.
    
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    root.children.extend([child1, child2])
    # Grandchildren for child1
    child1.children.extend([TreeNode(4), TreeNode(5)])
    # Grandchild for child2
    child2.children.append(TreeNode(6))
    
    def count_direct_children(node):
        if node is None:
            return 0
        return len(node.children)

    print("Direct children of the root:", count_direct_children(root))
    print("-" * 40)