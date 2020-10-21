grid = [[1,1,1,2],
        [2,3,6,5],
        [4,1,0,3],
        [6,8,2,4]]

def traverse_row_wise(grid):

    for row in range(len(grid)):
        print(grid[row])

print(traverse_row_wise(grid))


def traverse_col_wise(grid):

    for c in range(len(grid[0])):
        col = []
        for row in range(len(grid)):
            col.append(grid[row][c])
        print(col)

print(traverse_col_wise(grid))

#left to right
def traverse_diagonal_wise_pt1(grid):
    rows = len(grid)
    cols = len(grid[0])

    diags = []

    for k in range(rows):
        i = k
        j = 0
        diag = []
        while(i > -1):
            diag.append(grid[i][j])
            i -= 1
            j += 1
        diags.append(diag)

    for k in range(1, cols, 1):
        i = rows - 1
        j = k
        daig = []
        while(j < cols):
            daig.append(grid[i][j])
            i -= 1
            j += 1
        diags.append(daig)

    return diags

print(traverse_diagonal_wise_pt1(grid))

#up to down
def traverse_diagonal_wise_pt2(grid):
    rows = len(grid)
    cols = len(grid[0])

    diags = []

    for k in range(rows):
        i = k
        j = 0
        diag = []
        while(i < rows):
            diag.append(grid[i][j])
            i += 1
            j += 1
        diags.append(diag)

    for k in range(1, cols, 1):
        i = 0
        j = k
        daig = []
        while(j < cols):
            daig.append(grid[i][j])
            i += 1
            j += 1
        diags.append(daig)

    return diags

print(traverse_diagonal_wise_pt2(grid))