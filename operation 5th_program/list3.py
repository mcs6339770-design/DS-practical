from collections import deque

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


def bfs(start):
    visited = [False] * vertices
    queue = deque()

    visited[start] = True
    queue.append(start)

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)


start = int(input("\nEnter starting vertex: "))

bfs(start)