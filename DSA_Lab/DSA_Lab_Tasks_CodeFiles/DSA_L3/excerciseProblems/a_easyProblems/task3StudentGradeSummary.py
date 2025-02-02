class GradeSummary:
    def __init__(self):
        self.grades = []  # List to store grades

    def add_grade(self, grade):
        """Add a new grade to the list."""
        self.grades.append(grade)

    def calculate_average(self):
        """Calculate the average grade."""
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def filter_above_average(self):
        """Return grades that are greater than or equal to the class average."""
        avg = self.calculate_average()
        return [grade for grade in self.grades if grade >= avg]

    def view_grades(self):
        """Display all stored grades."""
        print("Grades:", self.grades)

# Testing Student Grade Summary
summary = GradeSummary()
summary.add_grade(85)
summary.add_grade(90)
summary.add_grade(78)
summary.add_grade(88)
summary.add_grade(92)

summary.view_grades()
print("Class Average:", summary.calculate_average())
print("Grades >= Class Average:", summary.filter_above_average())
