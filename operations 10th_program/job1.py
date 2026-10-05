def branch_bound(cost, employee, assigned, current_cost, assignment):
    n = len(cost)

    if employee == n:
        print("Assignment:", assignment)
        print("Minimum Cost:", current_cost)
        return current_cost

    min_cost = float('inf')

    for job in range(n):
        if job not in assigned:
            new_cost = current_cost + cost[employee][job]

            if new_cost < min_cost:
                assigned.add(job)
                assignment.append(job)

                result = branch_bound(
                    cost, employee + 1, assigned,
                    new_cost, assignment
                )

                min_cost = min(min_cost, result)

                assignment.pop()
                assigned.remove(job)

    return min_cost


cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

result = branch_bound(cost, 0, set(), 0, [])

print("Minimum Cost:", result)