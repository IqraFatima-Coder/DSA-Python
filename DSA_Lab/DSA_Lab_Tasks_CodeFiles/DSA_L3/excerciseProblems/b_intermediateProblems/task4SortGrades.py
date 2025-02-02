# Problem 4: Sort Grades
class GradeSorter:
    def __init__(self, grades):
        self.grades = grades
    
    def sort_grades(self):
        return sorted(self.grades, reverse=True)
    
    def display(self):
        print("Sorted Grades:", self.sort_grades())

# Testing GradeSorter
grades = GradeSorter([85, 92, 78, 90, 88])
grades.display()
