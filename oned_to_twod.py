def oned_to_twod(array, n, m):

    if len(array) == 0:
        return [[]]
    if len(array) != n*m:
        return None

    two_d = [[0 for _ in range(m)] for _ in range(n)]

    for r in range(n):
        for c in range(m):
            two_d[r][c] = array[r * m + c]

    return two_d


print(oned_to_twod([1,2,3,4,5,6], 2, 3))


