class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print(" " * level * 4 + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)

# Example Usage
root = TreeNode("Root")
child1 = TreeNode("Child1")
child2 = TreeNode("Child2")

root.add_child(child1)
root.add_child(child2)

child1.add_child(TreeNode("GrandChild1"))
child2.add_child(TreeNode("GrandChild2"))

root.display()
       



def traverse_preorder(node, result=None):
    if result is None:
        result = []
    result.append(node.data)
    for child in node.children:
        traverse_preorder(child, result)
    return result

# Example Usage
print("Pre-order Traversal:", traverse_preorder(root))

