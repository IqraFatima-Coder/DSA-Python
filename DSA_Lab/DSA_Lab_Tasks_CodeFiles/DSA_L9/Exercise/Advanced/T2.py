class Person:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def find_ancestors(self):
        ancestors = []
        current = self.parent
        while current:
            ancestors.append(current.name)
            current = current.parent
        return ancestors


# Sample usage
grandpa = Person("John")
dad = Person("Mike")
child = Person("Sara")

grandpa.add_child(dad)
dad.add_child(child)

print("Ancestors of Sara:", child.find_ancestors())
