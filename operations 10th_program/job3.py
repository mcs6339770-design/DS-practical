def job_allocation(cost):
    n = len(cost)
    best_cost = float('inf')
    best_assignment = []

    def bound(row, used):
        total = 0

        for i in range(row, n):
            values = [
                cost[i][j]
                for j in range(n)
                if j not in used
            ]
            total += min(values)

        return total

    def branch(row, used, total, assignment):
        nonlocal best_cost, best_assignment

        if row == n:
            if total < best_cost:
                best_cost = total
                best_assignment = assignment.copy()
            return

        if total + bound(row, used) >= best_cost:
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

    return best_cost, best_assignment


n = int(input("Enter number of employees/jobs: "))

cost = []

print("Enter cost matrix:")

for i in range(n):
    row = list(map(int, input(
        f"Employee {i + 1}: "
    ).split()))
    cost.append(row)

minimum, assignment = job_allocation(cost)

print("\nOptimal Job Allocation:")

for i, job in enumerate(assignment):
    print("Employee", i + 1, "-> Job", job + 1,
          "Cost =", cost[i][job])

print("Minimum Total Cost:", minimum)