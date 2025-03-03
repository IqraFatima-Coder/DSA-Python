class SpecialStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        self.max_stack = []
    def push(self, x):
        self.main_stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
    def pop(self):

        if self.main_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        if self.main_stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.main_stack.pop()
    def get_min(self):
        return self.min_stack[-1]
    
    def get_max(self):
        return self.max_stack[-1]
    
s = SpecialStack()
s.push(5)
s.push(1)
s.push(3)
print(s.get_min())  # 1
print(s.get_max())  # 5