class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    def add_expense(self, amount):
        self.expenses.append(amount)
    def total_expenses(self):
        return sum(self.expenses)
    def max_expense(self):
        return max(self.expenses) if self.expenses else 0
    def min_expense(self):
        return min(self.expenses) if self.expenses else 0
expense_tracker = ExpenseTracker()
expense_tracker.add_expense(20.5)
expense_tracker.add_expense(100.75)
print("Total Expenses:", expense_tracker.total_expenses())
print("Max Expense:", expense_tracker.max_expense())
print("Min Expense:", expense_tracker.min_expense())
