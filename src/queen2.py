"""
def queen(n):
    cols = [None]*n
    k = 0

    def diagonal(row, col):
        for r in range(row):
            if cols[r] == col or abs(cols[r] - col) == abs(
                r - row
            ):  # вертикаль или диагональ совпадают
                return 0
        return 1

    def solve(row=0):
        nonlocal k
        if row == n:
            k += 1
            return
        for col in range(n):
            if diagonal(row, col):
                cols[row] = col  # ставим ферзя
                solve(row + 1)  # идём в следующую строку

    solve()
    return k
"""


def queens(n):
    def backtrack(row, queens):
        if row == n:
            return 1
        k = 0
        for col in range(n):
            if all(
                col != c and abs(row - r) != abs(col - c) for r, c in enumerate(queens)
            ):
                k += backtrack(row + 1, queens + [col])
        return k

    return backtrack(0, [])


print(queens(8))
