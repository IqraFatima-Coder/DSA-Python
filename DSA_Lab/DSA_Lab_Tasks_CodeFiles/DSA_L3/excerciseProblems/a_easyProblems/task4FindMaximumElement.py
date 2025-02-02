# Problem 4: Find the Maximum Element
class MaxFinder:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def find_max(self):
        return max(self.numbers) if self.numbers else None

    def view_numbers(self):
        print("Numbers:", self.numbers)
# Testing MaxFinder
max_finder = MaxFinder()
numbers = [12, 45, 78, 23, 89, 56]
for num in numbers:
    max_finder.add_number(num)

max_finder.view_numbers()
print("Maximum Number:", max_finder.find_max())
