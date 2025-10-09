from itertools import permutations


# columns - перестановка номеров столбцов для каждой строки
def has_no_diagonal_conflict(columns):
    n = len(columns)
    for i in range(n):
        for j in range(i + 1, n):
            # проверяем, находятся ли два ферзя на одной диагонали
            if abs(i - j) == abs(columns[i] - columns[j]):
                return 0
    return 1


def count_queen_arrangements(n):
    count = 0
    for perm in permutations(range(n)):
        if has_no_diagonal_conflict(perm):
            count += 1
    return count


print(count_queen_arrangements(n=int(input())))
