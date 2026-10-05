def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def kruskal(vertices, edges):

    parent = list(range(vertices))
    mst = []
    total = 0

    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:

        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:
            mst.append((u, v, weight))
            total += weight
            parent[root_u] = root_v

            if len(mst) == vertices - 1:
                break

    print("\nMinimum Spanning Tree:")

    for u, v, weight in mst:
        print(u, "--", v, "=", weight)

    print("Minimum Cost =", total)


vertices = int(input("Enter number of vertices: "))
edges = []

while True:

    print("\n--- MENU ---")
    print("1. Add Edge")
    print("2. Display Edges")
    print("3. Construct MST")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        u = int(input("Enter source: "))
        v = int(input("Enter destination: "))
        w = int(input("Enter weight: "))

        edges.append((u, v, w))

    elif choice == 2:
        print("\nEdges:")

        for u, v, w in edges:
            print(u, "--", v, "=", w)

    elif choice == 3:
        kruskal(vertices, edges.copy())

    elif choice == 4:
        break

    else:
        print("Invalid choice")