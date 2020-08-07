def findSubmatrix(matrix):

    width = 0
    height = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                height = 1 + dfs1(matrix, i - 1, j) + dfs1(matrix, i + 1, j)
                width = 1 + dfs2(matrix, i, j - 1) + dfs2(matrix, i, j + 1)

    return [width, height]


def dfs1(matrix, i, j):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j]:
        return 0

    if matrix[i][j] == 1:
        return 0

    return 1 + dfs1(matrix, i - 1, j) + dfs1(matrix, i + 1, j)


def dfs2(matrix, i, j):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j]:
        return 0

    if matrix[i][j] == 1:
        return 0

    return 1 + dfs2(matrix, i, j - 1) + dfs2(matrix, i, j + 1)



