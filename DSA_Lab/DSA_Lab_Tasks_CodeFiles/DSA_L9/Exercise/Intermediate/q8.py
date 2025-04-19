class TreeNode2:
        def __init__(self, value):
            self.value = value
            self.children = []

        def add_child(self, child):
            self.children.append(child)

        def remove_child(self, child_value):
            self.children = [child for child in self.children if child.value != child_value]

        def display(self, level=0):
            print("  " * level + str(self.value))
            for child in self.children:
                child.display(level + 1)

    # Demonstration:
if __name__ == "__main__":
    root2 = TreeNode2("root")
    child_a = TreeNode2("child_a")
    child_b = TreeNode2("child_b")
    root2.add_child(child_a)
    root2.add_child(child_b)
    print("Tree before removal (children of root2):")
    root2.display()
    root2.remove_child("child_a")
    print("   Tree after removing 'child_a':")
    root2.display()