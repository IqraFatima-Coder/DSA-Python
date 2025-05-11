def greedy_coloring(graph):
    result = {}
    for node in sorted(graph):
        used = {result[neighbor] for neighbor in graph[node] if neighbor in result}
        color = 0
        while color in used:
            color += 1
        result[node] = color
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}

print("Node coloring:", greedy_coloring(graph))
