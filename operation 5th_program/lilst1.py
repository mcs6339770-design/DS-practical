from collections import deque

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

start = int(input("\nEnter starting vertex for BFS: "))

visited = [False] * vertices
queue = deque([start])
visited[start] = True

print("BFS Traversal:", end=" ")

while queue:
    vertex = queue.popleft()
    print(vertex, end=" ")

    for i in range(vertices):
        if graph[vertex][i] == 1 and not visited[i]:
            visited[i] = True
            queue.append(i)