# ----- Task 5: Convert a List of Nested Dictionaries into a Tree -----

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

def build_tree_from_dict_list(dict_list):
    nodes = []
    for d in dict_list:
        node = TreeNode(d["name"])
        # If the dictionary has children, build them recursively.
        if d.get("children"):
            node.children = build_tree_from_dict_list(d["children"])
        nodes.append(node)
    return nodes

def display_tree(nodes, level=0):
    for node in nodes:
        print("  " * level + node.name)
        display_tree(node.children, level + 1)

if __name__ == "__main__":
    # Sample input: a list with one nested dictionary.
    nested_dicts = [
        {
            "name": "A",
            "children": [
                {"name": "B", "children": []},
                {"name": "C", "children": [
                    {"name": "D", "children": []},
                    {"name": "E", "children": []}
                ]}
            ]
        }
    ]

    tree = build_tree_from_dict_list(nested_dicts)
    print("Output: Tree built from nested dictionaries:")
    display_tree(tree)
