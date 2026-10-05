def n_queens(n):
    board = [-1] * n
    solutions = []

    def safe(row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


n = int(input("Enter N: "))
solutions = n_queens(n)

print("\nNumber of Solutions:", len(solutions))

for no, solution in enumerate(solutions, 1):
    print("\nSolution", no)

    for col in solution:
        print(". " * col + "Q " + ". " * (n - col - 1))