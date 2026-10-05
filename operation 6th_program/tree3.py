def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]


def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

        return True

    return False


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter source, destination and weight:")

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parent = list(range(n))
rank = [0] * n

total = 0
count = 0

print("\nMinimum Spanning Tree:")

for weight, u, v in edges:

    if union(parent, rank, u, v):
        print(u, "--", v, "=", weight)

        total += weight
        count += 1

        if count == n - 1:
            break

print("Minimum Cost =", total)