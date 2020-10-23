"""
Given a non-neg integer numRows, generate the first numRows of Pascal's triangle.
"""


def pascals_triangle(numRows):

    triangle = []

    if numRows == 0:
        return triangle


    first_row = [1]
    triangle.append(first_row)


    for i in range(1, numRows, 1):
        prev_row = triangle[i-1]
        new_row = []

        new_row.append(1)

        for j in range(1,i,1):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

print(pascals_triangle(5))
print(pascals_triangle(2))