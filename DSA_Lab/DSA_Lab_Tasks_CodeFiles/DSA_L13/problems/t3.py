def has_self_loop_matrix(adj_matrix):
    for i in range(len(adj_matrix)):
        if adj_matrix[i][i] == 1:
            return True
    return False

# Example usage:
adj_matrix = [
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 1]  # self-loop at node 2
]

print("Self-loop exists?", has_self_loop_matrix(adj_matrix))
