class ActionNode:
    def __init__(self, action):
        self.action = action
        self.next = None

class UndoFeature:
    def __init__(self):
        self.top = None  # Stack کے لیے ٹاپ پوائنٹر

    def perform_action(self, action):
        new_node = ActionNode(action)
        new_node.next = self.top
        self.top = new_node
        print(f'Action performed: {action}')

    def undo(self):
        if not self.top:
            print("No actions to undo.")
            return

        print(f'Undoing: {self.top.action}')
        self.top = self.top.next  # پچھلے ایکشن پر واپس جانا

    def display_actions(self):
        if not self.top:
            print("No actions recorded.")
            return

        print("Action History:")
        temp = self.top
        while temp:
            print(f"- {temp.action}")
            temp = temp.next

# Example Usage
editor = UndoFeature()
editor.perform_action("Typed 'Hello'")
editor.perform_action("Bolded text")
editor.perform_action("Deleted a word")

editor.display_actions()

editor.undo()
editor.display_actions()
