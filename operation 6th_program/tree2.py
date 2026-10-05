import heapq

def prim(graph, n):
    visited = [False] * n
    pq = [(0, 0, -1)]
    total = 0

    print("\nMinimum Spanning Tree:")

    while pq:
        weight, vertex, parent = heapq.heappop(pq)

        if visited[vertex]:
            continue

        visited[vertex] = True

        if parent != -1:
            print(parent, "--", vertex, "=", weight)
            total += weight

        for neighbour, edge_weight in graph[vertex]:
            if not visited[neighbour]:
                heapq.heappush(
                    pq, (edge_weight, neighbour, vertex)
                )

    print("Minimum Cost =", total)


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

print("Enter source, destination and weight:")

for _ in range(e):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))

prim(graph, n)