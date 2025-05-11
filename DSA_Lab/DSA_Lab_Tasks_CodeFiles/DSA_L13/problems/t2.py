

def create_adjacency_list():
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))
    adj_list = {str(i): [] for i in range(vertices)}
    
    for _ in range(edges):
        u, v = input("Enter edge (u v): ").split()
        adj_list[u].append(v)
        adj_list[v].append(u)  # remove for directed graph
    
    return adj_list

create_adjacency_list()
