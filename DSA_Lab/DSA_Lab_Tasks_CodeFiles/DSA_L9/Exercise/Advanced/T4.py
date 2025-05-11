class Topic:
    def __init__(self, title):
        self.title = title
        self.subtopics = []

    def add_subtopic(self, topic):
        self.subtopics.append(topic)

    def search(self, keyword):
        results = []
        if keyword.lower() in self.title.lower():
            results.append(self.title)
        for sub in self.subtopics:
            results.extend(sub.search(keyword))
        return results


# Sample usage
python = Topic("Python")
ds = Topic("Data Structures")
trees = Topic("Trees")
lists = Topic("Linked Lists")

ds.add_subtopic(trees)
ds.add_subtopic(lists)
python.add_subtopic(ds)

print("Search results for 'tree':", python.search("tree"))
