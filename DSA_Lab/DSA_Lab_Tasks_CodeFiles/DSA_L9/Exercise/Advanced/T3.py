class MenuItem:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_item(self, item):
        self.children.append(item)

    def display(self, level=0):
        print("  " * level + self.name)
        for child in self.children:
            child.display(level + 1)

    def search(self, keyword):
        results = []
        if keyword.lower() in self.name.lower():
            results.append(self.name)
        for child in self.children:
            results.extend(child.search(keyword))
        return results


# Sample usage
home = MenuItem("Home")
about = MenuItem("About Us")
services = MenuItem("Services")
web = MenuItem("Web Development")
app = MenuItem("App Development")
services.add_item(web)
services.add_item(app)

home.add_item(about)
home.add_item(services)

print("Menu:")
home.display()

print("\nSearch results for 'App':", home.search("App"))
