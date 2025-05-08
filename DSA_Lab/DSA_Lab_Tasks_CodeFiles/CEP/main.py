# Student Admission Ranking System using BST

class Student:
    def __init__(self, name, app_id, score):
        self.name = name
        self.app_id = app_id
        self.score = score

class BSTNode:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

class StudentBST:
    def __init__(self):
        self.root = None

    def insert(self, student):
        if self.root is None:
            self.root = BSTNode(student)
            print(f"Inserted: {student.name} ({student.score})")
        else:
            self._insert_recursive(self.root, student)

    def _insert_recursive(self, node, student):
        if student.score < node.student.score:
            if node.left is None:
                node.left = BSTNode(student)
                print(f"Inserted: {student.name} ({student.score})")
            else:
                self._insert_recursive(node.left, student)
        elif student.score > node.student.score:
            if node.right is None:
                node.right = BSTNode(student)
                print(f"Inserted: {student.name} ({student.score})")
            else:
                self._insert_recursive(node.right, student)
        else:
            print(f"Duplicate score {student.score} not allowed.")

    def in_order_traversal(self):
        print("Students in ascending order of scores:")
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        if node:
            self._in_order_recursive(node.left)
            print(f"{node.student.name} | ID: {node.student.app_id} | Score: {node.student.score}")
            self._in_order_recursive(node.right)

    def search(self, score):
        return self._search_recursive(self.root, score)

    def _search_recursive(self, node, score):
        if node is None:
            return None
        if score == node.student.score:
            return node.student
        elif score < node.student.score:
            return self._search_recursive(node.left, score)
        else:
            return self._search_recursive(node.right, score)

    def print_range(self, x, y):
        print(f"Students with scores between {x} and {y}:")
        self._print_range_recursive(self.root, x, y)

    def _print_range_recursive(self, node, x, y):
        if node:
            if x < node.student.score:
                self._print_range_recursive(node.left, x, y)
            if x <= node.student.score <= y:
                print(f"{node.student.name} | ID: {node.student.app_id} | Score: {node.student.score}")
            if node.student.score < y:
                self._print_range_recursive(node.right, x, y)

    def print_rank(self, score):
        rank = self._count_less(self.root, score)
        print(f"{rank} students scored less than {score}.")

    def _count_less(self, node, score):
        if node is None:
            return 0
        if score <= node.student.score:
            return self._count_less(node.left, score)
        else:
            return 1 + self._size(node.left) + self._count_less(node.right, score)

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

def load_students_from_file(filename, bst):
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name, app_id, score = parts[0], parts[1], int(parts[2])
                    bst.insert(Student(name, app_id, score))
        print("Students loaded from file successfully.")
    except FileNotFoundError:
        print(f"File {filename} not found. Continuing without loading.")

# Sample students (only if file is missing)
sample_students = [
    ("Alice", "A001", 85),
    ("Bob", "A002", 78),
    ("Charlie", "A003", 92),
    ("David", "A004", 88),
    ("Eva", "A005", 95),
    ("Frank", "A006", 72),
    ("Grace", "A007", 80),
    ("Hannah", "A008", 68),
    ("Ian", "A009", 90),
    ("Jack", "A010", 82),
    ("Karen", "A011", 76),
    ("Leo", "A012", 87),
    ("Mona", "A013", 91),
    ("Nina", "A014", 84),
    ("Oscar", "A015", 89)
]

def main():
    bst = StudentBST()

    # Load from file
    load_students_from_file('students.txt', bst)

    # Load from sample if file missing
    if bst.root is None:
        for name, app_id, score in sample_students:
            bst.insert(Student(name, app_id, score))

    while True:
        print("\n--- Student Admission Ranking System ---")
        print("1. Insert New Student")
        print("2. View Students (Sorted)")
        print("3. Search Student by Score")
        print("4. Print Students in Score Range")
        print("5. Print Rank of a Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            app_id = input("Enter application ID: ")
            score = int(input("Enter admission score: "))
            bst.insert(Student(name, app_id, score))
        elif choice == '2':
            bst.in_order_traversal()
        elif choice == '3':
            score = int(input("Enter score to search: "))
            student = bst.search(score)
            if student:
                print(f"Found: {student.name} | ID: {student.app_id} | Score: {student.score}")
            else:
                print("Student with given score not found.")
        elif choice == '4':
            x = int(input("Enter lower score bound: "))
            y = int(input("Enter upper score bound: "))
            bst.print_range(x, y)
        elif choice == '5':
            score = int(input("Enter score to find rank: "))
            bst.print_rank(score)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
