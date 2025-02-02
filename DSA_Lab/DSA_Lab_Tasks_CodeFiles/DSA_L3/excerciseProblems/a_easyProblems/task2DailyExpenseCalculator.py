class ExpenseCalculator:
    def __init__(self):
        self.expenses = []  # List to store daily expenses

    def add_expense(self, amount):
        """Add a daily expense amount."""
        self.expenses.append(amount)

    def total_first_week(self):
        """Calculate total expenses for the first 7 days."""
        return sum(self.expenses[:7])  # Sum of first 7 elements

    def view_expenses(self):
        """Display all stored expenses."""
        print("Daily Expenses:", self.expenses)

# Testing Daily Expense Calculator
tracker = ExpenseCalculator()
tracker.add_expense(200)
tracker.add_expense(150)
tracker.add_expense(300)
tracker.add_expense(400)
tracker.add_expense(500)
tracker.add_expense(250)
tracker.add_expense(350)
tracker.add_expense(600)  # Extra expense (8th day, should not be included)

tracker.view_expenses()
print("Total expenses for the first 7 days:", tracker.total_first_week())