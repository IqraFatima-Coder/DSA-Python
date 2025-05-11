def adj_list_to_matrix(adj_list):
    nodes = sorted(adj_list.keys())
    size = len(nodes)
    index = {node: i for i, node in enumerate(nodes)}
    matrix = [[0]*size for _ in range(size)]

    for node in nodes:
        for neighbor in adj_list[node]:
            matrix[index[node]][index[neighbor]] = 1

    return matrix

# Sample adjacency list
adj_list = {'A': ['B'], 'B': ['C'], 'C': ['A']}
matrix = adj_list_to_matrix(adj_list)

# Output the matrix
print("Adjacency Matrix:")
for row in matrix:
    print(row)
