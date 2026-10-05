def knapsack(weights, values, capacity):

    n = len(weights)

    dp = [[0] * (capacity + 1)
          for _ in range(n + 1)]

    for i in range(1, n + 1):

        for w in range(capacity + 1):

            if weights[i - 1] <= w:

                dp[i][w] = max(
                    values[i - 1] +
                    dp[i - 1][w - weights[i - 1]],

                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    w = capacity
    selected = []

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected.append(i)
            w -= weights[i - 1]

    print("Maximum Value =", dp[n][capacity])

    print("Selected Items:")

    for item in reversed(selected):
        print(
            "Item", item,
            "Weight =", weights[item - 1],
            "Value =", values[item - 1]
        )


weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

knapsack(weights, values, capacity)
