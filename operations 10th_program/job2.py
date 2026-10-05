def calculate_bound(cost, row, used):
    n = len(cost)
    bound = 0

    for i in range(row, n):
        minimum = float('inf')

        for j in range(n):
            if j not in used:
                minimum = min(minimum, cost[i][j])

        bound += minimum

    return bound


def solve(cost):
    n = len(cost)
    best_cost = float('inf')
    best_assignment = []

    def branch(row, used, current, assignment):
        nonlocal best_cost, best_assignment

        if row == n:
            if current < best_cost:
                best_cost = current
                best_assignment = assignment.copy()
            return

        bound = current + calculate_bound(cost, row, used)

        if bound >= best_cost:
            return

        for job in range(n):
            if job not in used:
                used.add(job)
                assignment.append(job)

                branch(
                    row + 1,
                    used,
                    current + cost[row][job],
                    assignment
                )

                assignment.pop()
                used.remove(job)

    branch(0, set(), 0, [])

    return best_cost, best_assignment


cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

cost_value, assignment = solve(cost)

print("Optimal Assignment:")

for employee, job in enumerate(assignment):
    print("Employee", employee + 1,
          "-> Job", job + 1)

print("Minimum Cost:", cost_value)