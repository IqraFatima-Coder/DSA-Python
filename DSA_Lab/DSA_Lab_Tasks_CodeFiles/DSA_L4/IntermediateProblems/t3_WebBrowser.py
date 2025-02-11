class PageNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserNavigation:
    def __init__(self):
        self.current_page = None
        self.history = None

    def visit_page(self, url):
        new_page = PageNode(url)
        if not self.current_page:
            self.history = self.current_page = new_page
        else:
            self.current_page.next = new_page
            new_page.prev = self.current_page
            self.current_page = new_page
        print(f'Visited: {url}')

    def go_back(self):
        if not self.current_page or not self.current_page.prev:
            print("No previous page.")
            return
        self.current_page = self.current_page.prev
        print(f'Back to: {self.current_page.url}')

    def go_forward(self):
        if not self.current_page or not self.current_page.next:
            print("No forward page.")
            return
        self.current_page = self.current_page.next
        print(f'Forward to: {self.current_page.url}')

    def display_history(self):
        if not self.history:
            print("No browsing history.")
            return

        print("Browsing History:")
        temp = self.history
        while temp:
            print(f'- {temp.url}')
            temp = temp.next

# Example Usage
browser = BrowserNavigation()
browser.visit_page("www.google.com")
browser.visit_page("www.facebook.com")
browser.visit_page("www.github.com")

browser.display_history()

browser.go_back()
browser.go_back()
browser.go_forward()
