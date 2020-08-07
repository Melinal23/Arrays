def find_islands(grid):
    if len(grid) == 0:  # means the grid is all water
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
                dfs(grid, i, j)
    return count


def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
        return  # because you are at out of bounds or 0

    grid[i][j] = 0 # to avoid double counting
    dfs(grid, i + 1, j)  # right neighbor
    dfs(grid, i - 1, j)  # left neighbor
    dfs(grid, i, j + 1)  # upper neighbor
    dfs(grid, i, j - 1)  # lower neighbor