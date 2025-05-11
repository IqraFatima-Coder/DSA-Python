class Department:
    def __init__(self, name):
        self.name = name
        self.subdepartments = []

    def add_sub(self, dept):
        self.subdepartments.append(dept)

    def remove_sub(self, dept):
        self.subdepartments.remove(dept)

    def display(self, level=0):
        print("  " * level + self.name)
        for sub in self.subdepartments:
            sub.display(level + 1)

    def find(self, name):
        if self.name == name:
            return self
        for sub in self.subdepartments:
            result = sub.find(name)
            if result:
                return result
        return None


# Sample usage
corp = Department("Corporate")
hr = Department("HR")
it = Department("IT")
infra = Department("Infrastructure")
software = Department("Software")

corp.add_sub(hr)
corp.add_sub(it)
it.add_sub(infra)
it.add_sub(software)

print("Before Move:")
corp.display()

# Move 'Infrastructure' under 'HR'
it.remove_sub(infra)
hr.add_sub(infra)

print("\nAfter Move:")
corp.display()
