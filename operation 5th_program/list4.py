vertices = int(input("Enter number of vertices: "))

graph = [[] for _ in range(vertices)]

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u, v = map(int, input("Enter edge (u v): ").split())

    graph[u].append(v)
    graph[v].append(u)

print("\nAdjacency List:")

for i in range(vertices):
    print(i, "->", graph[i])


def dfs(vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            dfs(neighbour, visited)


start = int(input("\nEnter starting vertex: "))

visited = [False] * vertices

print("DFS Traversal:", end=" ")
dfs(start, visited)