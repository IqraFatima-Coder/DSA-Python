

from collections import deque, defaultdict

def bfs_levels(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    level_dict = defaultdict(list)

    while queue:
        node, level = queue.popleft()
        if node not in visited:
            visited.add(node)
            level_dict[level].append(node)
            for neighbor in graph[node]:
                queue.append((neighbor, level + 1))

    return dict(level_dict)

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

print(bfs_levels(graph, 'A'))
