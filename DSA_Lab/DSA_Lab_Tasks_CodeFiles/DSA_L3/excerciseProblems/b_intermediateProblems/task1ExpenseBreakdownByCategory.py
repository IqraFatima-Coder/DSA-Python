# Problem 1: Expense Breakdown by Category
class ExpenseTracker:
    def __init__(self):
        self.categories = {}
    
    def add_expense(self, category, amount):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(amount)
    
    def total_expense(self, category):
        return sum(self.categories.get(category, []))
    
    def view_expenses(self):
        for category, expenses in self.categories.items():
            print(f"{category}: {sum(expenses)}")

# Testing ExpenseTracker
expense_tracker = ExpenseTracker()
expense_tracker.add_expense("Food", 100)
expense_tracker.add_expense("Travel", 50)
expense_tracker.add_expense("Food", 200)
expense_tracker.view_expenses()
print("Total Food Expenses:", expense_tracker.total_expense("Food"))
