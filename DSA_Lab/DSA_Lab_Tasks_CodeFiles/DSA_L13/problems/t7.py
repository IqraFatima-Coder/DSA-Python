from collections import deque

def bidirectional_bfs(graph, start, goal):
    if start == goal:
        return [start]
    
    front = {start}
    back = {goal}
    visited_front = {start: None}
    visited_back = {goal: None}

    while front and back:
        if front & back:
            meet = (front & back).pop()
            path = []
            while meet:
                path.append(meet)
                meet = visited_front[meet]
            path.reverse()
            meet = visited_back[path[-1]]
            while meet:
                path.append(meet)
                meet = visited_back[meet]
            return path

        front = expand(graph, front, visited_front, visited_back)
        back = expand(graph, back, visited_back, visited_front)
    return None

def expand(graph, frontier, visited_self, visited_other):
    next_front = set()
    for node in frontier:
        for neighbor in graph[node]:
            if neighbor not in visited_self:
                visited_self[neighbor] = node
                next_front.add(neighbor)
    return next_front

graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}

print("Shortest path (bidirectional BFS):", bidirectional_bfs(graph, 'A', 'E'))
