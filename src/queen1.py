from itertools import permutations


def diagonal(col):
    n = len(col)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) == abs(col[i] - col[j]):
                return 0
    return 1


def queen(n):
    k = 0
    for perm in permutations(range(n)):
        if diagonal(perm):
            k += 1
    return k


print(queen(4))
