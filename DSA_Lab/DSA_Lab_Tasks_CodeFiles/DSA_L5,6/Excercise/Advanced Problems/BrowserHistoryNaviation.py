class Node:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self):
        self.current = None

    def visit(self, url):
        new_node = Node(url)
        if not self.current:
            self.current = new_node
        else:
            new_node.prev = self.current
            self.current.next = new_node
            self.current = new_node

    def back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
        print("Current Page:", self.current.url if self.current else "No history")

    def forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
        print("Current Page:", self.current.url if self.current else "No forward history")

# Usage
browser = BrowserHistory()
browser.visit("google.com")
browser.visit("facebook.com")
browser.back()
browser.forward()
