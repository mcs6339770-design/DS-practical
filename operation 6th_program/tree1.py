def prim(graph, n):
    selected = [False] * n
    selected[0] = True
    total = 0

    print("\nMinimum Spanning Tree:")

    for _ in range(n - 1):
        minimum = float('inf')
        u = v = -1

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            u = i
                            v = j

        print(u, "--", v, "=", minimum)
        total += minimum
        selected[v] = True

    print("Minimum Cost =", total)


n = int(input("Enter number of vertices: "))

print("Enter weighted adjacency matrix:")
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

prim(graph, n)