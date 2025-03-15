class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []

    def visit(self, site):
        print(f"Visiting: {site}")
        self.back_stack.append(site)
        self.forward_stack.clear()

    def back(self):
        if len(self.back_stack) > 1:
            self.forward_stack.append(self.back_stack.pop())
            print(f"Back to: {self.back_stack[-1]}")
        else:
            print("No more history to go back!")

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.forward_stack.pop())
            print(f"Forward to: {self.back_stack[-1]}")
        else:
            print("No forward history!")

browser = BrowserHistory()
browser.visit("google.com")
browser.visit("youtube.com")
browser.back()
browser.forward()
