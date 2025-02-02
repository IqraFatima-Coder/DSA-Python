# Problem 3: Matrix Addition
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def add(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)
    
    def display(self):
        for row in self.matrix:
            print(row)

# Testing Matrix Addition
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
result_matrix = matrix1.add(matrix2)
result_matrix.display()
DeprecationWarning