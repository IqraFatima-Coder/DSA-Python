
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

def count_nodes(node):
    count = 1  # Count current node
    for child in node.children:
        count += count_nodes(child)
    return count

# Example Usage
print("Total number of nodes in tree:", count_nodes(root))

CEO = TreeNode("CEO")
head_sales = TreeNode("Head of Sales")
head_hr = TreeNode("Head of HR")
sales_exec1 = TreeNode("Sales Executive 1")
sales_exec2 = TreeNode("Sales Executive 2")
hr_exec1 = TreeNode("HR Executive 1")

CEO.add_child(head_sales)
CEO.add_child(head_hr)
head_sales.add_child(sales_exec1)
head_sales.add_child(sales_exec2)
head_hr.add_child(hr_exec1)
print("\nCompany Hierarchy:")
CEO.display()
