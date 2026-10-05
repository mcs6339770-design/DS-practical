def solve(cost):
    n = len(cost)
    best = [float('inf'), []]

    def branch(row, used, total, assignment):

        if row == n:
            if total < best[0]:
                best[0] = total
                best[1] = assignment.copy()
            return

        # Calculate lower bound
        bound = total

        for i in range(row, n):
            minimum = min(
                cost[i][j]
                for j in range(n)
                if j not in used
            )
            bound += minimum

        if bound >= best[0]:
            return

        for job in range(n):
            if job not in used:

                used.add(job)
                assignment.append(job)

                branch(
                    row + 1,
                    used,
                    total + cost[row][job],
                    assignment
                )

                assignment.pop()
                used.remove(job)

    branch(0, set(), 0, [])

    return best


while True:
    print("\n--- JOB ALLOCATION SYSTEM ---")
    print("1. Find Minimum Cost")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        n = int(input("Enter number of employees: "))

        cost = []

        print("Enter cost matrix:")

        for i in range(n):
            row = list(map(int, input().split()))
            cost.append(row)

        result = solve(cost)

        print("\nBest Allocation:")

        for i, job in enumerate(result[1]):
            print(
                "Employee", i + 1,
                "-> Job", job + 1
            )

        print("Minimum Cost:", result[0])

    elif choice == "2":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")