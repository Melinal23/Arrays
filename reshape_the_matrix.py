"""
In MATLAB, there is a very useful function called, "reshape," which can reshape a matrix into a new one with
different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing
the row number and the column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing
order as they were.

if the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix;
otherwise, output the original matrix
"""

def reshape_the_matrix(nums, r, c):

    nums_row_count = len(nums)
    nums_col_count = len(nums[0])

    if (nums_col_count * nums_row_count) != (r*c):
        return nums

    result = [[0 for j in range(c)] for i in range(r)]
    result_row = 0
    result_col = 0

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            result[result_row][result_col] = nums[i][j]
            result_col += 1
            if(result_col == c):
                result_col = 0
                result_row += 1

    return result

"""
Time Complexity: O(m*n) where m is the number of rows in nums and n is the number of cols in nums
Space Complexity: O(n) where n is the number of elements in nums
"""


print(reshape_the_matrix([[1,2],[3,4]], 1, 4))