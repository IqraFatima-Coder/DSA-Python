class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def display(self, level=0):
        print("  " * level + self.name)
        for child in self.children:
            child.display(level + 1)


def dicts_to_tree(data_list):
    def build_node(data):
        for key, value in data.items():
            node = TreeNode(key)
            if isinstance(value, list):
                for child in value:
                    node.add_child(build_node(child))
            return node

    root = TreeNode("Root")
    for item in data_list:
        root.add_child(build_node(item))
    return root
