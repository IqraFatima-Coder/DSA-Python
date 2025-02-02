class GradeTracker:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def highest_grade(self):
        return max(self.grades) if self.grades else 0

    def lowest_grade(self):
        return min(self.grades) if self.grades else 0

grades = GradeTracker()
grades.add_grade(85)
grades.add_grade(90)
grades.add_grade(78)
print("Average Grade:", grades.average_grade())
print("Highest Grade:", grades.highest_grade())
print("Lowest Grade:", grades.lowest_grade())
