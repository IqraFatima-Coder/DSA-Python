class Move:
    def __init__(self, n, source, auxiliary, destination):
        self.n = n
        self.source = source
        self.auxiliary = auxiliary
        self.destination = destination

def tower_of_hanoi_stack(n):
    stack = []
    moves = []

    # Push initial move onto the stack
    stack.append(Move(n, 'A', 'B', 'C'))

    while stack:
        move = stack.pop()

        if move.n == 1:
            # Base case: Move a single disk
            moves.append(f"Move disk 1 from {move.source} to {move.destination}")
        else:
            # Push moves in reverse order to simulate recursion using stack
            stack.append(Move(move.n - 1, move.auxiliary, move.source, move.destination))
            stack.append(Move(1, move.source, move.auxiliary, move.destination))  # Move largest disk
            stack.append(Move(move.n - 1, move.source, move.destination, move.auxiliary))

    return moves

# Example: Solve Tower of Hanoi for 3 disks
moves = tower_of_hanoi_stack(3)
for step in moves:
    print(step)
