class UndoRedo:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def do(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()
        print(f"Action performed: {action}")

    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)
            print(f"Undo: {action}")
        else:
            print("Nothing to undo!")

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)
            print(f"Redo: {action}")
        else:
            print("Nothing to redo!")

editor = UndoRedo()
editor.do("Type A")
editor.do("Type B")
editor.undo()
editor.redo()
