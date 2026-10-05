vertices = int(input("Enter number of vertices: "))

graph = [[0] * vertices for _ in range(vertices)]

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph[u][v] = 1
    graph[v][u] = 1

print("\nAdjacency Matrix:")
for row in graph:
    print(row)


def dfs(vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")

    for i in range(vertices):
        if graph[vertex][i] == 1 and not visited[i]:
            dfs(i, visited)


start = int(input("\nEnter starting vertex for DFS: "))

visited = [False] * vertices

print("DFS Traversal:", end=" ")
dfs(start, visited)