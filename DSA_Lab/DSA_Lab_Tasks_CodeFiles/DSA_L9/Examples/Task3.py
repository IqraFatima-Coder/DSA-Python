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
       

def search_tree(node, target):
    if node.data == target:
        return True
    for child in node.children:
        if search_tree(child, target):
            return True
    return False

# Example Usage
print("Is 'Child2' in the tree?", search_tree(root, "Child2"))
print("Is 'ChildX' in the tree?", search_tree(root, "ChildX"))


