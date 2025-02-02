
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    
    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
        else:
            print("Invalid Move!")
    
    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None
    
    def display(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

# Testing TicTacToe
game = TicTacToe()
game.make_move(0, 0, 'X')
game.make_move(1, 1, 'O')
game.make_move(0, 1, 'X')
game.make_move(2, 2, 'O')
game.make_move(0, 2, 'X')
game.display()
winner = game.check_winner()
if winner:
    print("Winner:", winner)
else:
    print("No Winner Yet!")
